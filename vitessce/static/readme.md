# Vitessce Visualization Repository

This repository hosts scripts and notebooks that are dedicated to generating Vitessce visualizations using data in the OME-TIFF format. Below is the description of the files included in this repository.

## Files Description

### `png2ometif.py`
- **Description:** A Python script that converts PNG images to OME-TIFF format. It iteratively reads PNG images from the specified directory, performs necessary transformations, and then converts them to the corresponding OME-TIFF files. The script accepts an optional command-line argument for the root path, and it processes 64 regions by default.
- **Dependencies:** vitessce, skimage, tqdm
- **Usage:** `python png2ometif.py [root_path]`

### `Vitessce_bitmask_VCCF_local.ipynb`
- **Description:** A Jupyter Notebook that generates a Vitessce visualization using data in the OME-TIFF format. It allows two viewing options: locally as a data export for the HuBMAP publication page or online preview through vitessce.io. The `OUTPUT_LEVEL` parameter helps in determining the visualization type. It includes downloading the required image and CSV files, setting up the Vitessce configuration, and creating the visualization. The result can be viewed online or exported as a JSON file.
- **Dependencies:** Refer to the notebook for specific package requirements.
- **Usage:** Open and run the notebook using Jupyter Notebook or Jupyter Lab.

## How to Run

1. For `png2ometif.py`, run the script using the command `python png2ometif.py [root_path]` (replace `[root_path]` with the desired path if needed).
2. For `Vitessce_bitmask_VCCF_local.ipynb`, open the notebook using Jupyter Notebook, Jupyter Lab, or Google Colab and execute the cells as required.

## Dependencies

- Python
- vitessce
- skimage
- tqdm
- Jupyter Notebook (for the `.ipynb` file)

