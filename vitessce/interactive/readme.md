# Vitessce Visualization Repository

This repository hosts scripts and notebooks that are dedicated to generating Vitessce visualizations using data in the OME-TIFF format. Below is the description of the files included in this repository.

## Files Description

### `cell_data_view_generator.py`

This Python script is responsible for generating CSV files that define the color scheme for the visualization to show more colors. These CSV files can be used to define the color scheme and other properties for visualizing different types of data in Vitessce.

### `data_conversion.py`

This Python script is used to convert raw data into a format suitable for generating an OME-TIFF file for visualization in Vitessce. The main function reads CSV files containing the raw data, filters the data based on specified values, and constructs tables for data point vertices. These tables are then saved as separate CSV files. The generated CSV files serve as input for the next step in the data processing pipeline.

### `ome_tiff_generator.py`

This Python script converts the processed data from the previous step into an OME-TIFF file format, which is compatible with Vitessce for visualization. It includes functions for generating cell masks and converting strings to lists. The script reads the CSV files generated in the data_conversion.py step, converts the vertices column from a string to a list format, and generates cell masks for different cell types. These masks are then combined into a stack and saved as an OME-TIFF file, which can be directly loaded into Vitessce for visualization.

### `Vitessce_bitmask_hickey_Neigh_local.ipynb`

This notebook generates a Vitessce visualization using data in the OME-TIFF format. There are two ways to view the visualization: locally as a data export for the HuBMAP publication page or online using vitessce.io for online preview. The `OUTPUT_LEVEL` parameter is used to determine which way to use. The script downloads the necessary image and CSV files, sets up the Vitessce configuration, and creates the visualization. The resulting visualization can be viewed on vitessce.io or exported as a JSON file for further use.

## How to Run

1. For `data_conversion.py`, run the following command in Powershell to run all 64 regions:

```
for ($i=1; $i -le 64; $i++) {
    Write-Host "Running python .\data_conversion.py $i"
    python .\data_conversion.py $i
}
```

2. For `ome_tiff_generator.py`, run the following command in Powershell to run all 64 regions:

```
for ($i=1; $i -le 64; $i++) {
    Write-Host "Running python .\ome_tiff_generator.py $i"
    python .\ome_tiff_generator.py $i
}
```

2. For `Vitessce_bitmask_hickey_Neigh_local.ipynb`, open the notebook using Jupyter Notebook, Jupyter Lab, or Google Colab and execute the cells as required.

## Dependencies

- Python
- vitessce
- skimage
- tqdm
- Jupyter Notebook (for the `.ipynb` file)

