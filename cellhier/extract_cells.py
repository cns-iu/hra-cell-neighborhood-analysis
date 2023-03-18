import pims
import numpy as np
import pandas as pd
import os
import matplotlib as mpl
import matplotlib.pyplot as plt


def display_cells(I,xys,panel,indices = None,window_size = 60,dpi = 500,to_save = False,vmax_percentile = 95,vmin_percentile = 10,figsize = None,fontsize = 3,plot_title = True):
        mpl.rcParams['figure.dpi']= dpi
        if indices is None:
            indices = np.arange(len(xys))
        xys_copy = (xys).astype(int).copy()
        
        for r,(x,y) in enumerate(xys_copy):
            if figsize:
                f,ax = plt.subplots(1,len(panel),figsize = figsize)
            else:
                f,ax = plt.subplots(1,len(panel))
           
            I_win = I[:,max(0,y-window_size):min(I.shape[1]-1,y+window_size),max(0,x-window_size):min(I.shape[2]-1,x+window_size)]
            if type(to_save)==dict:
                to_save[indices[r]] = I_win
           
            for c,chan_name in enumerate(panel):
                img = I_win[c]
                #img=img/np.median(img)
                if vmax_percentile:
                    ax[c].imshow(img,vmax = np.percentile(img,vmax_percentile),vmin = np.percentile(img,vmin_percentile))
                else:
                    ax[c].imshow(img)
                ax[c].scatter(window_size,window_size,c = 'red',marker = '+',s = 1,alpha = .3)
                if plot_title:
                    ax[c].set_title(chan_name[:6],fontsize = fontsize,rotation = 45,pad = 10)
                #ax[c].axis('off')
                ax[c].set_yticklabels([])
                ax[c].set_xticklabels([])
                if c==0:
                    ax[c].set_ylabel(str(indices[r]))

            plt.show()
            
        mpl.rcParams['figure.dpi']= 150   
        #return save

class SingleExperiment (object):
    
    
    def __init__(self,runName,bestFocus_path,channelNames_path = '',only_montages = True,half_resolution = True):
        '''
        only_montages:  only extract montages from BestFocus folder
        half_resolution:  if working with images, the images are at half resolution so the entered XY coordinates need to be divided by 2
        '''
        self.exp_images = {}
        self.regions = []
        self.channelNames = []
        self.name = runName
        self.half_resolution = half_resolution
        
        if channelNames_path == '':
            channelNames_path = '/'.join(bestFocus_path.split('/')[:-2])+'/channelNames.txt'
            self.channelNames = list(pd.read_csv(channelNames_path,header = None).values[:,0]) 
    
        montages = [k for k in os.listdir(bestFocus_path) if '.tif' in k] 
        if len(montages)==0:
            print ("could not find any regions with montage. If you don't want montages change argument 'only_montages' to 'False'")
            return
        print ('found the following regions...')
        print (montages)
        for montage in montages:
            region = montage.split('_')[0]
            try:
                i = pims.TiffStack(os.path.join(bestFocus_path,montage))
                self.exp_images[(runName,region)] = i
                self.regions+=[region]
            except:
                print ('Couldnt load following images...')
                print (runName,region)
                print (bestFocus_path)
                print ()
            

        
class SetExperiment(object):

    
    def __init__(self,runs,df,run_col = 'run',reg_col='region',X = 'X',Y='Y'):
        self.runs = runs
        self.run_col = run_col
        self.reg_col = reg_col
        self.X = X
        self.Y = Y
        
        for run in df[run_col].unique():
            if run not in self.runs:
                print ('could not find ',run, 'in input runs')
  
    
    def plot_single_cells(self,df,reveal_channels,window_size = 60,dpi = 500,to_save = False,
                          figsize = None,fontsize = 3,vmax_percentile = 90,vmin_percentile = 10,
                         plot_title = True):
        save = {}
        for run in df[self.run_col].unique():
            if run not in self.runs:
                print ('could not find this run in SetExperiment.runs')
            else:
                print ('plotting run: {}'.format(run))
                channels = [self.runs[run].channelNames.index(p) for p in reveal_channels]
                print ('channels:',channels)
                run_df = df[df[self.run_col]==run]
                for reg in run_df[self.reg_col].unique():
                    if reg not in self.runs[run].regions:
                        print ('couldnt find region in SingleExperiment ({}) regions'.format(run))
                    else:
                        img_pims = self.runs[run].exp_images[(run,reg)]
                        reg_df = run_df[run_df[self.reg_col]==reg]
                        xys = reg_df[[self.X,self.Y]].values
                        if self.runs[run].half_resolution:
                            xys = xys/2

                        I = np.array(img_pims[channels])

                        display_cells(I,xys,reveal_channels,window_size = window_size,indices = reg_df.index.values,dpi = dpi,to_save = save,figsize = figsize,fontsize = fontsize,vmax_percentile = vmax_percentile,vmin_percentile = vmin_percentile,
                                     plot_title = plot_title)
                        
        return save
    
    def get_crop_stack(self,Exp,X,Y,channel_names,window_size,cells = [[]],**kwargs):
        '''
        may cause issues if using experiment with run, region,X,Y columns not labeled as they are here
        '''
        run,region = Exp.split('_')
        single_experiment_object = self.runs[run]
        if single_experiment_object.half_resolution:
            X= X//2
            Y = Y//2
    #     I = S.runs[run].exp_images[region]
        channels = [single_experiment_object.channelNames.index(channel_name) for channel_name in channel_names]
        tiff_page = single_experiment_object.exp_images[(run,region)]
        I = np.array(tiff_page[channels])
        crop_stack = I[:,max(0,Y-window_size):min(I.shape[1]-1,Y+window_size),max(0,X-window_size):min(I.shape[2]-1,X+window_size)]

        return crop_stack
    def get_rescaled_coordinates(self,Exp,X,Y,subset,window_size,**kwargs):
        '''
        subset:  df with columns labeled as singleExperiment
        X:  center x coordinate
        Y:  center y coordinate
        '''
        run,region = Exp.split('_')
        subset = subset[subset['Exp']==Exp]
        single_experiment_object = self.runs[run]
        if single_experiment_object.half_resolution:
            X= X//2
            Y = Y//2
            subset['rescaled_x'] = subset[self.X]//2
            subset['rescaled_y'] = subset[self.Y]//2
        else:
            subset['rescaled_x'] = subset[self.X]
            subset['rescaled_y'] = subset[self.Y]



        crop = subset.query('@X-@window_size<rescaled_x<@X+@window_size and @Y-@window_size<rescaled_y<@Y+@window_size')
        crop['rescaled_x'] = crop['rescaled_x'].values-X+window_size
        crop['rescaled_y'] = crop['rescaled_y'].values-Y+window_size
        
        
        return crop
    
                        