import pandas as pd
import os

folder_path = r'G:\HuBMAP\Hickey\Intestine_64_data\vitessce_neighbour'

union_of_types = set()

# Iterate through the files and read the unique values in the "type" column
for i in range(1, 65):
    file_path = os.path.join(folder_path, f'Region_{i}_nuclei_table.csv')
    df = pd.read_csv(file_path)
    unique_types = sorted(df['Neighborhood'].unique())
    length = len(unique_types)
    print(f'Region_{i} / {length}: {unique_types}')
    
    # Update the union set with the unique types of the current region
    union_of_types.update(unique_types)
   
# Convert the union set to a list and sort it
sorted_union_of_types = sorted(list(union_of_types))
 
# Print the union set of all types across regions
print(f'Union of all types across regions: {sorted_union_of_types}')

color_dict = {key: value for value, key in enumerate(sorted_union_of_types, 1)}

# Result
print(color_dict)