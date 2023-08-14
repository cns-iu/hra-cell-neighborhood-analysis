import os
import sys
import pandas as pd
import numpy as np


def generate_cross_vertices(x, y, radius):
    # Vertices at the ends of the cross
    vertices = [
        (x, y),  # Center
        (x - radius, y),  # Left
        (x + radius, y),  # Right
        (x, y),  # Center
        (x, y + radius),  # Up
        (x, y - radius),  # Down
        (x, y),  # Center
    ]
    return vertices


def generate_cell_vertices(x, y, radius, num_vertices=12):
    angles = np.linspace(0, 2 * np.pi, num_vertices+1)
    vertices = [
        (x + np.cos(angle) * radius, y + np.sin(angle) * radius) for angle in angles
    ]
    return vertices


def generate_random_cell_vertices(x, y, radius, num_vertices=12):
    angles = np.linspace(0, 2 * np.pi, num_vertices+1)
    vertices = []
    # Add randomness to radius and angle
    random_radius = np.random.uniform(0.9 * radius, 1.1 * radius)
    for angle in angles:
        random_angle = np.random.uniform(-0.2, 0.2)  # adjust as needed
        vertices.append(
            (
                x + np.cos(angle + random_angle) * random_radius,
                y + np.sin(angle + random_angle) * random_radius,
            )
        )
    vertices.append(vertices[0])
    return vertices


def generate_link_vertices(x, y, vx, vy):
    return [(x, y), (vx, vy)]


def main():
    # Default region_index
    region_index = 3
    scale = 1
    universal_size = 8

    # Check if at least one command-line argument is given
    if len(sys.argv) >= 2:
        # Use the given argument as region_index
        region_index = int(sys.argv[1])
    if len(sys.argv) >= 3:
        # Use the given argument as scale
        scale = float(sys.argv[2])

    # Construct the path to the nuclei file
    output_root_path = r"G:\HuBMAP\Hickey\Intestine_64_data\vitessce_neighbour"
    nuclei_root_path = r"G:\HuBMAP\Hickey\Intestine_64_data"
    nuclei_file_name = f"Region_{region_index}.csv"
    nuclei_file_path = os.path.join(nuclei_root_path, nuclei_file_name)

    # read the csv file
    nuclei_df = pd.read_csv(nuclei_file_path)

    # construct the 'cell' table and generate vertices
    cell_table = nuclei_df[["Neighborhood", "Neigh_sub", "x", "y"]].copy()
    cell_table["vertices"] = cell_table.apply(
        lambda row: generate_cell_vertices(row["x"], row["y"], universal_size), axis=1)

    # Save the tables to .csv files
    cell_table.to_csv(os.path.join(output_root_path,
                                   f"Region_{region_index}_nuclei_table.csv"), index=False)


if __name__ == "__main__":
    main()


# PS code
# for ($i=1; $i -le 64; $i++) {
#     Write-Host "Running python .\data_conversion.py $i"
#     python .\data_conversion.py $i
# }
