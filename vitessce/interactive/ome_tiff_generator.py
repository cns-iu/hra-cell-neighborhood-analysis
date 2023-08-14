import os
import sys
import pandas as pd
import numpy as np
import ast
from tqdm import tqdm
from skimage.draw import polygon, line
from vitessce.data_utils import multiplex_img_to_ome_tiff
from skimage.morphology import disk, dilation


def generate_cell_mask(mask, value, vertices, is_line=False):
    if is_line:
        # Loop over pairs of vertices
        for i in range(len(vertices) - 1):
            rr, cc = line(int(vertices[i][1]), int(vertices[i][0]),
                          int(vertices[i + 1][1]), int(vertices[i + 1][0]))
            mask[rr, cc] = value
    else:
        rr, cc = polygon([v[1] for v in vertices], [v[0] for v in vertices])
        mask[rr, cc] = value


def convert_str_to_list(row):
    return [list(i) for i in ast.literal_eval(row)]


def generate_mask_arr(type_list, table, mask_shape, is_line=False):
    # initialize an empty mask for each cell type
    masks = {cell_type: np.zeros(mask_shape, dtype=np.uint8)
             for cell_type in type_list}
    for index, row in tqdm(table.iterrows(), total=len(table), desc='Processing rows'):
        generate_cell_mask(
            masks[row['Neighborhood']], color_dict[row['Neighborhood']], row['vertices'], is_line=is_line)

    # Create an ordered list of masks
    mask_list = [masks[cell_type] for cell_type in type_list]

    # make the line thicker by dilation
    if is_line:
        for i in range(len(mask_list)):
            selem = disk(1)
            mask_list[i] = dilation(mask_list[i], selem)

    # Stack masks into a 3D array. The new array has shape (n, m, len(cell_types)),
    # where n and m are the dimensions of the original masks.
    bitmask_stack = np.dstack(mask_list)
    return bitmask_stack


def vertices_str2list(table, zoom_scale):
    table['vertices'] = table['vertices'].apply(convert_str_to_list)
    table['vertices'] = table['vertices'].apply(
        lambda x: [[int(i[0] * zoom_scale), int(i[1] * zoom_scale)] for i in x])


# Default region_index
region_index = 1

scale = 1

# Check if at least one command-line argument is given
if len(sys.argv) >= 2:
    # Use the given argument as region_index
    region_index = int(sys.argv[1])
if len(sys.argv) >= 3:
    # Use the given argument as scale
    scale = float(sys.argv[2])

# Construct the path to the nuclei file
nuclei_root_path = r'G:\HuBMAP\Hickey\Intestine_64_data\vitessce_neighbour'
nuclei_file_name = f'Region_{region_index}_nuclei_table.csv'
nuclei_file_path = os.path.join(nuclei_root_path, nuclei_file_name)

cell_table = pd.read_csv(nuclei_file_path)

# convert the vertices column from string to list
vertices_str2list(cell_table, scale)

all_cell_types = ['Adatpive Immune Enriched', 'CD66+ Mature Epithelial', 'CD8+ T Enriched IEL', 'Glandular Epithelial',
                  'Innate Immune Enriched', 'Inner Follicle', 'Innervated Smooth Muscle', 'Innervated Stroma',
                  'Macrovasculature', 'Mature Epithelial', 'Microvasculature', 'Outer Follicle', 'Paneth Enriched',
                  'Plasma Cell Enriched', 'Secretory Epithelial', 'Smooth Muscle', 'Smooth Muscle & Innate Immune',
                  'Stroma', 'Stroma & Innate Immune', 'Transit Amplifying Zone']
color_dict = {'Adatpive Immune Enriched': 1, 'CD66+ Mature Epithelial': 2, 'CD8+ T Enriched IEL': 3, 'Glandular Epithelial': 4, 'Innate Immune Enriched':
              5, 'Inner Follicle': 6, 'Innervated Smooth Muscle': 7, 'Innervated Stroma': 8, 'Macrovasculature':
              9, 'Mature Epithelial': 10, 'Microvasculature': 11, 'Outer Follicle': 12, 'Paneth Enriched':
              13, 'Plasma Cell Enriched': 14, 'Secretory Epithelial': 15, 'Smooth Muscle': 16, 'Smooth Muscle & Innate Immune':
              17, 'Stroma': 18, 'Stroma & Innate Immune': 19, 'Transit Amplifying Zone': 20}

# Assert that both color_dict and cell_types share same elements
assert set(all_cell_types) == set(color_dict.keys()
                                  ), "Keys in the color_dict do not match the cell_types list"

# determine the shape of your canvas
height = (cell_table['y'].max() + 30) * scale
width = (cell_table['x'].max() + 30) * scale
shape = (height, width)
shape = tuple(map(int, shape))
print(shape)

print("Generating cell masks...")
groups = sorted(cell_table['Neigh_sub'].unique().tolist())
cell_mask_stack_list = []
for group in groups:
    print(f"\tGenerating {group} masks...")
    cell_types = sorted(
        cell_table[cell_table["Neigh_sub"] == group]["Neighborhood"].unique().tolist())
    filtered_cell_table = cell_table[cell_table["Neigh_sub"] == group]
    cell_mask_stack = generate_mask_arr(cell_types, filtered_cell_table, shape)
    cell_mask = np.amax(cell_mask_stack, axis=2)[:, :, np.newaxis]
    cell_mask_stack_list.append(cell_mask)

layer_combine = True

mask_stack = np.dstack(cell_mask_stack_list)
final_types = groups
assert len(
    final_types) == mask_stack.shape[2], "layer number does not match layer names"

# Ensure the axes are in the CYX order by transposing the array
bitmask_arr = np.transpose(mask_stack, (2, 0, 1))

# Save the masks
print("Saving masks...")

tif_name = f'Region_{region_index}_mask.ome.tif'
multiplex_img_to_ome_tiff(bitmask_arr, final_types, os.path.join(
    nuclei_root_path, tif_name), axes="CYX")

# PS code
# for ($i=1; $i -le 64; $i++) {
#     Write-Host "Running python .\ome_tiff_generator.py $i"
#     python .\ome_tiff_generator.py $i
# }

# Linux pyramid commands
# for i in {1..64}
# do
#   ./bftools/bfconvert -tilex 512 -tiley 512 -pyramid-resolutions 6 -pyramid-scale 2 -compression LZW /mnt/g/HuBMAP/Hickey/Intestine_64_data/vitessce_neighbour/Region_${i}_mask.ome.tif /mnt/g/HuBMAP/Hickey/Intestine_64_data/vitessce_neighbour/hickey_neigh_data/Region_${i}_mask.pyramid.ome.tif
# done
