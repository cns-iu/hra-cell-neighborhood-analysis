'''
Graham Barlow September, 18 , 2018
'''

import pandas as pd
import os
import numpy as np
import warnings

    


def in_array(a1,a2):
    for i, n in enumerate(a2):
        if np.array_equal(a1,n):
            return float(i)
    return np.nan
        
def alloc_paths(paths,levels):
    arr = paths[levels].values.astype(int)
    _,i,counts = np.unique(arr,axis = 0,return_inverse = True,return_counts =  True)
    return i,counts
def concat(exps):
    for ex in exps:
        d=exps[ex]
        d["Exp"]=ex
        d["Clusterid"]=d["Clusterid"].astype("category")
    cats=[set(exps[ex]["Clusterid"].cat.categories.values) for ex in exps]
    intersection=set.intersection(*cats)
    #print (len(intersection), "cell types included in analysis")
    for ex in exps:
        d=exps[ex]
        d["Clusterid"]=d["Clusterid"].cat.set_categories(intersection,ordered=False) 
    df=pd.concat(exps.values())
    df["Exp"]=df["Exp"].astype("category")
    df.reset_index(inplace=True,drop=True)

    return df 
    

def mean_area (EXPS,all_experiments):
    t = concat({e: all_experiments[e] for e in [x for b in EXPS.values() for x in b]})
    g=  t.groupby("Exp")
    diff = g.apply(max)[["X","Y"]]-g.apply(min)[["X","Y"]]
    return np.mean(diff["X"]*diff["Y"])
def cellnumber(area,k,density):
    return area*density/(k**2)

def split_and_sample(grouped):
    samp_group = grouped.apply(lambda x: x.sample(n = NUM_CELLS_FINAL))
    exps = list(np.unique(samp_group["Exp"]))
    exps.sort()
    indices = np.concatenate([samp_group.loc[e].index for e in exps])
    return samp_group,indices

def alloc_cells(dists,n_dict,cluster_func,k,**kwargs):
    Os = dists/np.expand_dims(np.sum(dists,1),1)
    Es = n_dict[k]
    alloc ,_,_ = cluster_func(Es,Os,**kwargs)
    return alloc

def filter_nodes(alloc,dists,cluster_func,n_dict,K, **kwargs):
    un, counts = np.unique(alloc,return_counts = True)
    #min_cells = .005 * NUM_CELLS_FINAL
    min_cells = 5
    to_keep = counts>min_cells
    if sum(to_keep) < len(to_keep):
        keep = un[counts> min_cells]
        Es = n_dict[K][keep] 
        n_dict[K] = Es
        alloc = alloc_cells(dists,n_dict,cluster_func,K,**kwargs)
        alloc = filter_nodes(alloc,dists,cluster_func, n_dict,K)
    return alloc





        
  

 ### optional Rtree implementation
        #        print ('Inserting points...',flush = True)
        #         idx = index.Index()
        #idx = 'empty_var'
        #         for i,data in df.iterrows():
        #             idx.insert(int(i), (int(data.X),int(data.Y),int(data.X),int(data.Y)))
        #       print ('Done inserting points...',flush = True)


def calculate_all_dists (params,all_experiments,random_select_cells_seed = 0):

    if random_select_cells_seed:
        select_run_cells(params,all_experiments,random_select_cells_seed)
    
    K_VALUES = params["K_VALUES"]
    sum_cols = params['sum_cols']
    BUILD_NUM_CELLS = params['BUILD_NUM_CELLS']
    idx = 'empty_var'
    print ("Training model...",flush = True)
    WINDOWS = pd.DataFrame() #initialize
    
    exps = list(all_experiments.keys())
    for completed,exp in enumerate(exps):
        print (str(completed+1) +"/"+str(len(exps))+" -  Experiment:", exp,flush = True)
        df = all_experiments[exp]
        
        #calculate windows for building graph (different cells for different k)

        print ('Calculating windows for building graph', flush = True)
        for k,n in zip(K_VALUES,BUILD_NUM_CELLS):
            print ("\t-K:", k,flush = True)
            
            sample = df.sample(n=n,random_state = random_select_cells_seed)
            cell_counts = combine_dists(sample,df,k,sum_cols,idx,isBuild = 1,isRun = 0, normalize = False)
            WINDOWS = pd.concat([WINDOWS,cell_counts])
        
        #calculate windows for running graph (same cell for all k)
        print ('Calculating windows for running graph', flush = True)
        
        sample = df[df['isRun']==1] 
      
        for k in K_VALUES:
            print ("\t-K:", k,flush = True)
            cell_counts = combine_dists(sample,df,k,sum_cols,idx,isBuild = 0,isRun = 1, normalize = False)
    
            
            WINDOWS = pd.concat([WINDOWS,cell_counts])
            
        
        
            
    return WINDOWS

def select_run_cells(params,all_experiments,random_seed):
    np.random.seed(random_seed)

    for exp,cells in all_experiments.items():
        y = np.ones(params['FINAL_NUM_CELLS'])
        n = np.zeros(len(cells)-len(y))
        vals = np.append(y,n)
        np.random.shuffle(vals)
        cells['isRun'] = vals

def combine_dists(sample,df,k,sum_cols,idx,isBuild,isRun, normalize = False):
    dists,_ = get_dists(sample[["X","Y"]].values,df,k,sum_cols,idx, normalize=normalize)
    cell_counts = pd.DataFrame(dists,columns = sum_cols)
    cell_counts['k'] = k
    cell_counts['isBuild']= isBuild
    cell_counts['isRun'] = isRun
    cell_counts['orig_index'] = sample['orig_index'].values
    
    return cell_counts
             
    

def get_dists(points,df,k, sum_cols,idx,subset_indices = None, normalize=False):
    
    try:
        exps = np.unique(df["Exp"])
        if len(exps)>1:
            warnings.warn("Multiple Experiments in one dataframe. Will mix distributions!")
    except:
        pass
    
    dists=np.zeros((len(points),len(sum_cols)))
    #returned_points = []
    
        

    for i,point in enumerate(points):
        min_x=point[0]-k/2.0
        max_x=point[0]+k/2.0
        min_y =point[1]-k/2.0
        max_y=point[1]+k/2.0
        if subset_indices==None:
            subset = df
        else:
            subset = subset_indices[i]
            
        
        q=subset.query('@min_x<X<@max_x and @min_y<Y<@max_y' )
        
        
#         bounded_ind = list(idx.intersection((min_x, min_y, max_x, max_y)))
#         q = df.loc[bounded_ind]
        #counts = q['Clusterid'].value_counts(normalize=normalize,dropna=True,sort=False)
        counts = q[sum_cols].sum(axis = 0)
        #dists.append(counts.values)
        dists[i] = counts.values
        #returned_points+=[q]
    
    return np.array(dists),0#returned_points

class PathError(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)



def save_data(main,params):
    full_path = params["PATH"] + "/" + params["PROJECT_NAME"]
    if os.path.isdir(full_path):
        raise PathError("Project folder already exists!", full_path)
    else:
        os.mkdir(full_path)
        main.to_csv(full_path+"/main_distributions.csv")
        save_params(full_path, params)
#     print ("Data to be saved at:", full_path)
#     main.to_csv(params["N"])
    

    
def save_params(path, params):

    full_path = path + "/params"

    os.mkdir(full_path)
    f = open(full_path+"/summary.txt","w")
    for k,v in params.items():
        f.write( str(k)+"\t"+str(v)+"\t"+"\n" )
    f.close()

    #numerical output that will be read in later.  Easier if saved as separate files
    K_VALUES = params["K_VALUES"]
    cats = params ["sum_cols"]
    pd.Series(cats).to_csv(full_path+"/sum_cols.csv",index = False)
    pd.Series(K_VALUES).to_csv(full_path+"/kvalues.csv",index = False)
#     np.savetxt(full_path + "/sum_cols.txt",list(cats),fmt = '%s')
#     np.savetxt(full_path + "/kvalues.txt",K_VALUES,fmt = '%s')    
