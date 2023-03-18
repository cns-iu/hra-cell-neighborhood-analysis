'''
Graham Barlow September, 18 , 2018
'''

import pandas as pd
import numpy as np
import os


def build_lattice(windows, cluster_func,THRESHOLDS, K_VALUES,cats,MAX_ITERS = 30,prints=True,**kwargs):
    '''
    Sample windows to cluster to form nodes:
    
    group: groupby object of windows
    cluster_func:  clustering function (as python function object)
    THRESHOLDS:  iterable of divisive thresholds for each k
    K_VALUES: k for each level
    cats:  columns to index from windows used for clustering
    MAX_ITERS:  maximum number of clusters for each k.
    **kwargs: kwargs passed to cluster_func
    '''
    isBuild = 1
    isRun = 0

    n_dict = {}
    if prints:
        print ("Building lattice...")
    for K,dist_threshold in zip(K_VALUES,THRESHOLDS):
        if prints:
            print ("\tK:", K,flush = True)
        dists = windows[(windows['isBuild']==isBuild)& (windows['k']==K)][cats].values
        
        #dists = group.get_group((isBuild,isRun,K))[cats].values 
        Es = add_nodes(dists,dist_threshold,cluster_func,MAX_ITERS,**kwargs)
        n_dict[K] = Es
    return n_dict

def run_lattice(windows,n_dict,cluster_func,K_VALUES,cats,prints = True,affinity = True,**kwargs):
    '''
    Run same cell subset through each level k and allocate distance to node
    
    group:  groupby object of windows
    n_dict:  (key,value)  = (k,cluster center)
    cluster_func:  clustering function (as python function object)
    K_VALUES: k for each level
    cats:  columns to index from windows used for clustering
    **kwargs: kwargs passed to cluster_func
    '''
    
    isBuild = 0
    isRun = 1
    
    #samples = group.get_group((isBuild,isRun,K_VALUES[0]))
    samples = windows[(windows['isRun']==isRun)& (windows['k']==K_VALUES[0])]
    PATHS = pd.DataFrame(samples.index.values,columns = ['orig_index'])
    if prints:
        print ("Running lattice...")
    for K in K_VALUES:
        if prints:
            print ("\tK:", K,flush = True)
        #dists = group.get_group((isBuild,isRun,K))[cats].values
        dists = windows[(windows['isRun']==isRun)& (windows['k']==K)][cats].values
        Os = dists + np.mean(dists,axis = 0)
        Os = Os/Os.sum(axis = 1,keepdims = True)
        Es = n_dict[K]
        _,_,phi2_dists = cluster_func(Es,Os,**kwargs)
        
        if affinity == 'aff':
        #convert distance to node to affinity
            to_concat = pd.DataFrame(np.exp(-30*phi2_dists)/np.exp(-30*phi2_dists).sum(axis = 1,keepdims=True),columns = [str(K)+".aff."+str(i) for i in range(phi2_dists.shape[1])])
            PATHS = pd.concat([PATHS,to_concat],axis = 1)
            
        elif affinity == 'dist':
            to_concat = pd.DataFrame(phi2_dists,columns = [str(K)+".dist."+str(i) for i in range(phi2_dists.shape[1])])
            PATHS = pd.concat([PATHS,to_concat],axis = 1)
        
        elif affinity == 'none':
            continue
        
        closest = np.argmin(phi2_dists,axis = 1)
        PATHS[K] = closest
        

        
        
#         alloc = alloc_cells(dists,n_dict,cluster_func,K,**kwargs)
#         alloc = filter_nodes(alloc,dists,cluster_func,n_dict,K,**kwargs)
        #allocs.append(alloc)
#     A = np.vstack(allocs)
#     paths = pd.DataFrame(A.T,columns = K_VALUES)
#     paths = pd.concat([samples[["X","Y","Clusterid","Exp","index"]].reset_index(drop=True),paths.reset_index(drop=True)],axis = 1)
    
    PATHS = PATHS.set_index('orig_index')
    return PATHS



    
def train_a_model (group,cluster_func,THRESHOLDS,K_VALUES,cats,MAX_ITERS = 30,prints = True,affinity = True,**kwargs):
    '''
    Build and allocate cells to graph
    
    cluster_func:  function used for clustering windows:
    function must accept arguments as (Es,Os,kwargs) and return alloc,max,dists
    
    where:
    
    alloc: allocations of each object in Os
    max:  index of next cluster
    dists:  distance matrix between Os and Es
    
    THRESHOLDS:  iterable of divisive thresholds for each k
    K_VALUES: k for each level
    cats:  columns to index from windows used for clustering
    MAX_ITERS:  maximum number of clusters for each k.
    **kwargs: kwargs passed to cluster_func
    
    '''
    if affinity!='aff' and affinity!='dist' and aff !='none':

        raise ValueError('Argument \'affinity\' must be \'aff\', \'dist\' or \'None\'')
    
    n_dict = build_lattice(group,cluster_func,THRESHOLDS,K_VALUES,cats,MAX_ITERS,prints = prints,**kwargs)
    paths = run_lattice(group,n_dict,cluster_func,K_VALUES,cats,prints = prints,affinity = affinity,**kwargs)
    return n_dict,paths


def save(project_name, path, main,n_dict,final,THRESHOLDS,K_VALUES, cats ):
    exp_path = path+"/"+project_name
    if project_name in os.listdir(path):
        raise PathError("Project Name already in path!  Aborting to not overwrite saved data")
    else:
        os.mkdir(exp_path)
        main.to_csv(exp_path+"/main_distributions.csv")
        
    

    
    
def save_model(paths,n_dict,model_name,cats, PROJECT_FOLDER,reset_index=  True):
    model_path = PROJECT_FOLDER+"/"+model_name
    
    if os.path.isdir(model_path):
        raise PathError("Model folder already exists!", model_path)
    else:
        os.mkdir(model_path)
        if reset_index:
            paths = paths.reset_index()
        paths.to_csv(model_path+"/paths.csv")
        node_df = save_n_dict(n_dict,cats)
        node_df.to_csv(model_path+"/nodes.csv")
    
def save_n_dict(n_dict,cats):
    to_concat = []
    for k,v in n_dict.items():
        d = pd.DataFrame(v,columns = cats)
        d['k'] = k
        to_concat.append(d)

    df = pd.concat(to_concat).reset_index()
    return df       
    
def load_model(PROJECT_FOLDER, model_name,cats):
    paths = pd.read_csv(os.path.join(PROJECT_FOLDER,model_name,"paths.csv"))
    n_dict = load_n_dict(PROJECT_FOLDER,model_name,cats)
    return paths,n_dict

def load_n_dict(PROJECT_FOLDER,model_name,cats):
    n = pd.read_csv(os.path.join(PROJECT_FOLDER ,model_name,"nodes.csv"))
    n_dict1 = {}
    n_group = n.groupby("k")
    for k, level in  n_group:
        n_dict1[k] = level.sort_values("index")[cats].values
        
    return n_dict1
    
# def apply_merge(df,mapping, change_col_name = "Clusterid",new_col_name = "old_Clusterid", rename = True,start_clusterid = None):
    
#     ''' 
#     df:  paths to change clusterid of
#     mapping:  Cell annotation with list of clusterids to merge
#     change_col_name:  column to draw values from to change
#     new_col_name:  what to name added columns.  see rename
#     rename:  if True:
#         will set current change_col_name columns to new_col_name and set
#         the modified column to "Clusterid"
        
#         if False:
#             will append modified column as new column and name it new_col_name.
        
#         if one wants to use the merged columns from here on out set rename = True
    
#     returns modified dataframe, ledger of changes
#     '''
#     if start_clusterid == None:
#         max_cluster = max(df[change_col_name])+1
#     else:
#         max_cluster = start_clusterid
#     df['temporary_name'] = df[change_col_name].astype('float')
#     new_vals = {}
#     for cell in mapping.keys():
#         to_change = mapping[cell]
#         if len(to_change)>1:
#             df.at[df[change_col_name].isin(to_change),'temporary_name'] = max_cluster
#             new_vals[cell] = max_cluster
#             max_cluster+=1
#         else:
#             new_vals[cell] = to_change[0]
#     if rename:
#         print ("Changing ", change_col_name , "to ", new_col_name)
#         df = df.rename(index = str , columns = {change_col_name: new_col_name})
#         print ("Changing modified column to Clusterid")
#         df = df.rename(index = str, columns = {"temporary_name": "Clusterid"})
#     else:
#         print ("Changing modified column to ", new_col_name)
#         df = df.rename(index = str , columns = {"temporary_name": new_col_name})
        
#     ledger = pd.DataFrame(mapping)
#     ledger = ledger.rename(index = str, columns = {0: "Merged Clusterids"})
#     ledger['new_clusterid'] = None
#     ledger.at[new_vals.keys(),'new_clusterid'] = list(new_vals.values())
    
#     return df,ledger   
# def get_mapping(df):
#     #old =pd.read_csv(Cluster_annotation_path,sep  = "\t",header = None)
#     old = df
#     old = old.rename(index = str, columns = {1: "Cell Type", 0: "Clusterid"})
#     s = old.groupby("Cell Type").apply(lambda x: x["Clusterid"].values)
#     clusters = np.array(np.concatenate([s[i] for i in range(len(s)) ]))
#     return s,clusters

def phi_2(Es,Os): 
    '''
    Calculate phi_2 distance between windows.
    
    Es:  matrix of shape (number of clusters, number of features)
    Os:  matrix of shape (number of observations, number of features)
    
    returns:
    alloc:  vector of length (number of observations ).  Allocations of Os to Es clusters
    max_arg:  index of most distant observed value to become next cluster
    phi2:  distance matrix between Es and Os of shape (number of clusters, number of observations)
    
    '''
   
    dists = ((np.expand_dims(Es,axis =0)-np.expand_dims(Os, axis = 1))**2)/(Es[None,:,:])
    phi2=np.sum(dists,2)
    dists=np.amin(phi2,1)
    alloc=np.argmin(phi2,1)

    max_arg = np.argmax(dists)
    
    
    return alloc,max_arg,phi2


class DivisiveClustering(object):
    def __init__(self,cluster_func = phi_2,num_iters=25):
        self.cluster_func = cluster_func
        self.num_iters = num_iters
        self.log = {}
        self.norm_Os = 0
        self.centroids = {}
        
    def add_nodes(self,counts,num_iters,**kwargs):
        '''
        Implementation of divisive clustering algorithm.

        counts:  matrix of shape (number of windows, number of features).  Sum of each cell type or softly-clustered
        cell type in each window.
        dist_threshold:  minimum distance at which to end clustering.
        cluster_func:  function used for clustering windows:
        MAX_ITERS:  maximum number of clusters for each k.
        **kwargs: kwargs passed to cluster_func: 
        '''
       
        counts = counts + counts.mean(axis = 0)
        
        Os = counts/np.sum(counts,axis = 1, keepdims = True)
        self.norm_Os = Os
        initial_Es = np.mean(counts,axis = 0)[None,:] #starting is average of vectors to cluster

        #get window that's most distant from parent to initiate process
        
        alloc,max_distr,phi2_dists=self.cluster_func(initial_Es,self.norm_Os,**kwargs)

        new_distr=Os[max_distr]
        Es = np.expand_dims(new_distr,0)
   

        for n in range(1,num_iters+1):
            alloc,max_distr,_= self.cluster_func(Es,self.norm_Os,**kwargs)
            new_distr=Os[max_distr]
            Es=np.vstack([Es,new_distr])
            self.log[n] = (Es,alloc) 
    
    def get_centroids(self,n):
        alloc = self.log[n][1]
        included = np.unique(alloc)
        centroids = np.zeros((len(included),self.norm_Os.shape[1]))
        for i in range(len(included)):
            center = self.norm_Os[alloc==included[i]].mean(axis = 0)
            center = center/center.sum()
            centroids[i] = center
        self.centroids[n] = centroids
        return centroids
    
    def fit(self,y,n,centroids = True):
        if centroids:
            Es = self.centroids[n]
        else:
            Es = self.log[n][0]
        y+y.mean(axis = 0)
        y = y/np.sum(y,axis = 1,keepdims = True)
        alloc = self.cluster_func(Es,y)[0]
        
        return alloc
        
    
    
    
def get_centroids(Es,Os,alloc):
    '''
    After allocating cells to nodes, compute cluster centers.
    
    Es:  matrix of shape (number of clusters, number of features)
    Os:  matrix of shape (number of observations, number of features)
    
    alloc:  vector of length (number of observations ).  Allocations of Os to Es clusters
    '''
    included = np.unique(alloc)
    centroids = np.zeros((len(included),Es.shape[1]))
    for i in range(len(included)):
        center = Os[alloc==included[i]].mean(axis = 0)
        center = center/center.sum()
        centroids[i] = center

    return centroids
    
    

def add_nodes(counts,dist_threshold,cluster_func,MAX_ITERS = 30,**kwargs):
    '''
    Implementation of divisive clustering algorithm.
    
    counts:  matrix of shape (number of windows, number of features).  Sum of each cell type or softly-clustered
    cell type in each window.
    dist_threshold:  minimum distance at which to end clustering.
    cluster_func:  function used for clustering windows:
    MAX_ITERS:  maximum number of clusters for each k.
    **kwargs: kwargs passed to cluster_func: 
    '''
    cells_per_window = counts.sum(axis = 1)
    
    counts = counts[cells_per_window>np.mean(cells_per_window)/2]
    counts = counts + counts.mean(axis = 0)
    Os = counts/np.sum(counts,axis = 1, keepdims = True)
    initial_Es = np.mean(counts,axis = 0)[:,None] #starting is average of vectors to cluster
    
    #get window that's most distant from parent to initiate process
    alloc,max_distr,phi2_dists=cluster_func(initial_Es,Os,**kwargs)
    
    new_distr=Os[max_distr]
    Es = np.expand_dims(new_distr,0)
    
    
    for x in range(MAX_ITERS-1):
        alloc,max_distr,phi2_dists=cluster_func(Es,Os,**kwargs)
        dists = np.amin(phi2_dists,1)
        if dists[max_distr]<dist_threshold: break
        new_distr=Os[max_distr]
        Es=np.vstack([Es,new_distr])
        
    if x ==MAX_ITERS-1:
        print ("Stopped at maximum iterations")
    centroids = get_centroids(Es,Os,alloc)
    
    
    return centroids
    



# def build_paths(main,cluster_func,cats,trained_models, K_VALUES,num_paths = 2,**kwargs):
    
#     df = main[main["Set"]=="validation"]
#     exps = np.unique(df["Exp"])
#     df["Exp"] = df["Exp"].cat.set_categories(exps)
#     norm_distributions,bulk_indices = build_validation_data(df,cats)
#     columns = ['Distance'] + list(K_VALUES)
    
#     keys = list(bulk_indices.keys())
#     keys.sort()
#     pos = pd.concat([df[df["Exp"] == k].set_index('index').loc[bulk_indices[k]] for k in keys],axis =0)
#     pos = pos[pos['k'] == K_VALUES[0]]
    
    
#     result = {}
#     for name,model in trained_models.items():
#         print ("Validating model:", name,flush = True)
#         paths = model['allocations']
#         A = paths[K_VALUES].values.astype(int)
#         n_dict = model['node_dict']
#         unique_paths,counts = np.unique(A, axis =0,return_counts = True)
#         include = counts>num_paths
#         unique_paths = unique_paths[include]
        
#         #build array (num_cells x num_levels + 1)
#         #where first column is return phi_2 distance summed over k levels
#         #last columns are allocation for each k
#         allocs_and_dists = np.array([alloc_cell(distr,n_dict,cluster_func,K_VALUES,unique_paths, **kwargs) for distr in norm_distributions])
#         allocs = allocs_and_dists[:,1:]
#         dists = allocs_and_dists[:,0]
#         result[name] = {"dists": dists, "allocs": allocs}
#     return result,pos

    
# def build_validation_data(df,cats):
#     exp_group = df.groupby("Exp")
#     cols = ['index'] + cats

#     bulk_indices = {}
#     bulk_distrs ={}
#     for exp,data in exp_group:
#         group = data.groupby("index")
#         ind_distrs = np.array([g.sort_values('k',axis=0,ascending = False)[cols].values for _,g in group ])
#         index  = ind_distrs[:,0,0]
#         distrs = ind_distrs[:,:,1:]
#         bulk_indices[exp] = index
#         bulk_distrs[exp] = distrs
        
#     keys = np.unique(df["Exp"])
#     keys.sort()
    
    
#     distributions = np.concatenate([bulk_distrs[k] for k in keys])
    
#     norm_distributions = distributions/(np.sum(distributions,2)[:,:,None])
#     #indices =  np.concatenate([bulk_indices[k] for k in keys])
#     return norm_distributions,bulk_indices

# def alloc_cell(cell_dists,n_dict,cluster_func,K_VALUES,M,**kwargs):

#     nodes = []
#     total_distance = 0
#     for i, k_dist in enumerate(cell_dists):
#         k = K_VALUES[i]
#         try:
#             next_node_options = np.unique(M[:,0]).astype(int)
            
#             Es = n_dict[k]
#             #to_include = np.isin(np.arange(len(Es)),next_node_options)
#             to_include = np.array([False]*len(Es))
            
#             to_include[next_node_options] = True
#             alloc,_, distance = cluster_func(Es[to_include],k_dist[None,:],**kwargs)
#             total_distance+= distance[0]
#             alloc = alloc[0]
#             alloc = next_node_options[alloc]
#             nodes.append(alloc)
#             t = M[:,0] == alloc
#             M = M[t,1:]
#         except IndexError:
#             print ('error:',k, M.shape)
#             total_distance+= np.nan
#             alloc = np.nan
#             nodes.append(alloc)
        
#     out = [total_distance] + nodes
#     return np.array(out)
# def reallocate_pathless(paths,K_VALUES,main,cats,num=5):
#     # get cells that need to be reallocated

#     inverse,counts = alloc_paths(paths,K_VALUES)
#     path_count = counts[inverse]
#     include = path_count>num
#     print ("Cells preserved:", sum(include)/len(include),flush = True)
#     print ("Neighborhoods preserved:", sum(counts>num)/len(counts),flush = True)
    
#     #split dataframe into those that will and will not be reallocated
#     print ("reconfiguring dataframes...")
#     p = paths[include]
#     reallocate = paths[~include].copy()
#     build = main[main["isBuild"]==0]
#     merge = pd.merge(reallocate.drop(K_VALUES,1),build, on = ["X","Y","Clusterid","Exp","index"])
#     merge["Set"] ='validation'
    
#     #force remaining cells down paths
#     print ("reallocating cells...")
#     tm = {"final": {'node_dict': n_dict,"allocations": p}}
#     costs, a_dict = validate_all(merge,cats,tm,K_VALUES)
    
#     new_allocs = a_dict["final"]
#     match = ["X","Y","Clusterid","Exp","index"]
#     cols = match + K_VALUES
#     final = pd.concat([new_allocs[cols],p[cols]])
#     print ("finishing...")
#     inverse,counts = alloc_paths(final,K_VALUES)
#     final["unique_paths"] = inverse
#     return final

# def validate_all (new_main,cats,trained_models,K_VALUES,num_paths = 2):
#     result,pos = build_paths(new_main,cats,trained_models,K_VALUES,num_paths)
#     costs = []
#     allocs ={}
#     path_ks = K_VALUES
#     for model_name,r in result.items():
#         a = pd.DataFrame(r['allocs'],columns = K_VALUES)
#         df = pd.concat([pos.reset_index(),a.reset_index(drop=True)],axis = 1)
#         cost = np.mean(r['dists'])
#         costs.append([model_name,cost])
#         allocs[model_name] = df
#     return np.array(costs),allocs
    