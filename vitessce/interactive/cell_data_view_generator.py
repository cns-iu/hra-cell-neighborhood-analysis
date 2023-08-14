import pandas as pd


cell_dict = {'Adatpive Immune Enriched': 1, 'CD66+ Mature Epithelial': 2, 'CD8+ T Enriched IEL': 3, 'Glandular Epithelial': 4, 'Innate Immune Enriched':
             5, 'Inner Follicle': 6, 'Innervated Smooth Muscle': 7, 'Innervated Stroma': 8, 'Macrovasculature':
             9, 'Mature Epithelial': 10, 'Microvasculature': 11, 'Outer Follicle': 12, 'Paneth Enriched':
             13, 'Plasma Cell Enriched': 14, 'Secretory Epithelial': 15, 'Smooth Muscle': 16, 'Smooth Muscle & Innate Immune':
             17, 'Stroma': 18, 'Stroma & Innate Immune': 19, 'Transit Amplifying Zone': 20}

cell_data = {
    'cell_id': list(cell_dict.values()),
    'cell_type': list(cell_dict.keys())
}

print(cell_data)

cell_sets_data = pd.DataFrame(cell_data)

cell_sets_data.to_csv('cell_sets.csv', index=False)
