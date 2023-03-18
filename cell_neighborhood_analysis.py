'''
Code part of "High Resolution Single Cell Maps Reveals Distinct Cell Organization and Function Across Different Regions of the Human Intestine"
by Hickey et al.

doi: https://doi.org/10.1101/2021.11.25.469203
'''

import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import time
import sys
import matplotlib.pyplot as plt
import math
import os

from sklearn.cluster import MiniBatchKMeans
import seaborn as sns
import scanpy as sc

from cellhier.general import *


def get_windows(job, n_neighbors, tissue_group, exps, X, Y):
    start_time, idx, tissue_name, indices = job
    job_start = time.time()

    print("Starting:", str(idx + 1) + '/' + str(len(exps)), ': ' + exps[idx])

    tissue = tissue_group.get_group(tissue_name)
    to_fit = tissue.loc[indices][[X, Y]].values

    fit = NearestNeighbors(n_neighbors=n_neighbors).fit(tissue[[X, Y]].values)
    m = fit.kneighbors(to_fit)

    # sort_neighbors
    args = m[0].argsort(axis=1)
    add = np.arange(m[1].shape[0]) * m[1].shape[1]
    sorted_indices = m[1].flatten()[args + add[:, None]]

    neighbors = tissue.index.values[sorted_indices]

    end_time = time.time()

    print("Finishing:", str(idx + 1) + "/" + str(len(exps)), ": " + exps[idx], end_time - job_start,
          end_time - start_time)
    return neighbors.astype(np.int32)


def main():

    #Choose this information and input based on above
    ks = [5,10,20] # k=5 means it collects 5 nearest neighbors for each center cell
    path_to_data = "/Users/abhiroop/Developer/cns/CODEX_HuBMAP_alldata_Dryad.csv"

    X = 'x'
    Y = 'y'
    reg = 'unique_region'
    file_type = 'csv'

    cluster_col = 'Cell Type'
    keep_cols = [X,Y,reg,cluster_col]
    save_path = '/Users/abhiroop/Developer/cns/hra-cell-neighborhood-analysis/viz/'

    # Import Data
    n_neighbors = max(ks)

    cells = pd.read_csv(path_to_data)
    cells = pd.concat([cells, pd.get_dummies(cells[cluster_col])], 1)
    sum_cols = cells[cluster_col].unique()
    values = cells[sum_cols].values

    # Get each region
    tissue_group = cells[[X, Y, reg]].groupby(reg)
    exps = list(cells[reg].unique())
    tissue_chunks = [(time.time(), exps.index(t), t, a) for t, indices in tissue_group.groups.items() for a in
                     np.array_split(indices, 1)]
    tissues = [get_windows(job, n_neighbors, tissue_group, exps, X, Y) for job in tissue_chunks]

    # Loop over k to compute neighborhoods
    out_dict = {}
    for k in ks:
        for neighbors, job in zip(tissues, tissue_chunks):
            chunk = np.arange(len(neighbors))  # indices
            tissue_name = job[2]
            indices = job[3]
            window = values[neighbors[chunk, :k].flatten()].reshape(len(chunk), k, len(sum_cols)).sum(axis=1)
            out_dict[(tissue_name, k)] = (window.astype(np.float16), indices)

    windows = {}
    for k in ks:
        window = pd.concat(
            [pd.DataFrame(out_dict[(exp, k)][0], index=out_dict[(exp, k)][1].astype(int), columns=sum_cols) for exp in
             exps], 0)
        window = window.loc[cells.index.values]
        window = pd.concat([cells[keep_cols], window], 1)
        windows[k] = window

    k = 10
    n_neighborhoods = 30
    neighborhood_name = "neighborhood" + str(k)
    k_centroids = {}

    # producing what to plot
    windows2 = windows[k]
    windows2[cluster_col] = cells[cluster_col]

    km = MiniBatchKMeans(n_clusters=n_neighborhoods, random_state=0)

    labels = km.fit_predict(windows2[sum_cols].values)
    k_centroids[k] = km.cluster_centers_
    cells[neighborhood_name] = labels

    neigh_list = [1, 22, 12, 18, 20]

    # this plot shows the types of cells (ClusterIDs) in the different niches (0-9)
    k_to_plot = k
    niche_clusters = (k_centroids[k_to_plot])
    tissue_avgs = values.mean(axis=0)
    fc = np.log2(
        ((niche_clusters + tissue_avgs) / (niche_clusters + tissue_avgs).sum(axis=1, keepdims=True)) / tissue_avgs)
    fc = pd.DataFrame(fc, columns=sum_cols)
    s = sns.clustermap(fc.iloc[neigh_list, :], vmin=-3, vmax=3, cmap='bwr', figsize=(15, 8))
    s.savefig(save_path+"celltypes_perniche_"+"_"+str(k)+".png", dpi=600)

    col_list = list(sum_cols)
    hm = cells.groupby(['neighborhood10'])[col_list].mean()
    sns.clustermap(hm, cmap='viridis', standard_scale=0)

    n_conversion_30 = {
        0: 'Secretory Epithelial',
        1: 'Mature Epithelial',
        2: 'Smooth Muscle',
        3: 'Plasma Cell Enriched',
        4: 'Adatpive Immune Enriched',
        5: 'Microvasculature',
        6: 'Stroma',
        7: 'Inner Follicle',
        8: 'Secretory Epithelial',
        9: 'Paneth Enriched',

        10: 'CD66+ Mature Epithelial',
        11: 'Innervated Smooth Muscle',
        12: 'Transit Amplifying Zone',
        13: 'Stroma & Innate Immune',
        14: 'CD8+ T Enriched IEL',
        15: 'CD66+ Mature Epithelial',
        16: 'Secretory Epithelial',
        17: 'Stroma',
        18: 'Transit Amplifying Zone',
        19: 'Plasma Cell Enriched',

        20: 'Transit Amplifying Zone',
        21: 'Innervated Stroma',
        22: 'Mature Epithelial',
        23: 'Smooth Muscle & Innate Immune',
        24: 'Plasma Cell Enriched',
        25: 'Innate Immune Enriched',
        26: 'Glandular Epithelial',
        27: 'CD8+ T Enriched IEL',
        28: 'Outer Follicle',
        29: 'Macrovasculature',

    }
    cells['Neighborhood'] = cells['neighborhood10'].map(n_conversion_30)
    cells['Neighborhood'].unique()

    pal_color = {
        'CD44hi Tumor': 'tan',
        'Tumor': 'gray',
        'Ki67+ Tumor': 'beige',
        'Ki67+ TYRP1hi Tumor': 'brown',
        'Ki67+ CD71hi Tumor': 'orange',
        'APC Enriched Tumor': 'green',
        'Inflamed Tumor': 'magenta',
        'Vascularized Immune Infiltrate': 'black',
        'Unproductive T cell Tumor Interface': 'red',
        'Immune Infiltrate': 'skyblue',
        'TYRP1hi Tumor': 'olive',
        'Productive T cell Tumor Interface': 'blue',
        'Neutrophil Enriched Immune Infiltrate': 'yellow',
        'Neutrophil Enriched': 'gold'
    }

    pal_color_cells = {
        'EGFR+ Epithelial cell': 'blue',
        'Smooth muscle cell': 'red',
        'Epithelial cell': 'yellow',
        'Nerve cell': 'magenta',
        'Macrophage': 'orange',
        'CD4+ Treg': 'green',
        'Endothelial cell': 'brown',
        'CD8+ T cell': 'black',
        'Intestinal Epithelial cell': 'gray',
        'Neutrophil': 'skyblue',
        'Parietal cell': 'fuchsia',
        'Plasma cell': 'gold',
        'NK cell': 'plum',
        'CD4+ T cell': 'yellowgreen',
        'CK7+ Epithelial cell': 'tan',
        'Neck cell': 'navy',
        'Neuroendocrine cell': 'bisque',
        'Chief cell': 'goldenrod',
        'Goblet cell': 'blueviolet',
        'Foveolar cell': 'darkorange',
        'Stromal cell': 'teal',
        'PDPN+ Stromal cell': 'olive',
        'p63+ EGFR+ Epithelial cell': 'dimgray',
        'Gastric mucouse secreting cell': 'indigo',
        'Biglycan+ Stromal cell': 'lightcoral',
        'Dendritic cell': 'cyan',
        'Paneth cell': 'ivory',
        'B cell': 'beige',
        'Squamous Epithelial cell': 'darkblue',
        'Immune unknown cell': 'lightcyan',
        'p63+ Epithelial cell': 'royalblue',
    }

    cell_list = list(cells['Cell Type'].unique())
    neigh_list = list(cells.Neighborhood.unique())
    color_list = list(pal_color_cells.values())
    dict_cell = dict(zip(cell_list, color_list))
    dict_neigh = dict(zip(neigh_list, color_list))
    dict_neigh

    dict_neigh2 = {
        'Transit Amplifying Zone': 'darkblue',
        'Microvasculature': 'black',
        'Adatpive Immune Enriched': 'orange',
        'Glandular Epithelial': 'darkorange',
        'CD66+ Mature Epithelial': 'firebrick',
        'Stroma & Innate Immune': 'brown',
        'CD8+ T Enriched IEL': 'green',
        'Mature Epithelial': 'magenta',
        'Innate Immune Enriched': 'skyblue',
        'Outer Follicle': 'navy',
        'Plasma Cell Enriched': 'yellow',
        'Innervated Stroma': 'blueviolet',
        'Stroma': 'gray',
        'Macrovasculature': 'gold',
        'Secretory Epithelial': 'yellowgreen',
        'Smooth Muscle': 'red',
        'Innervated Smooth Muscle': 'lightgreen',
        'Inner Follicle': 'blue',
        'Smooth Muscle & Innate Immune': 'tan',
        'Paneth Enriched': 'lightblue'}

    # modify figure size aesthetics for each neighborhood
    plt.rcParams["legend.markerscale"] = 24
    figs_n, names = catplot(cells, X='Xcorr', Y='Ycorr', exp='array',
                            hue='Neighborhood', invert_y=True, size=1, figsize=8, palette=dict_neigh2)

    for fig, name in zip(figs_n, names):
        fig.savefig(save_path + f'/{name}.png', dpi=200)




if __name__ == "__main__":
    main()
