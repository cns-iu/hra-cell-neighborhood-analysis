from vitessce.data_utils import rgb_img_to_ome_tiff
from skimage import io
import sys
from os.path import join
from tqdm import tqdm

root_path = r'\\wsl.localhost\Ubuntu\home\vitessce\static_images'

if len(sys.argv) >= 2:
    root_path = sys.argv[1]

for i in tqdm(range(1, 65)):  # Loop from 1 to 64
    img_file = f'Region_{i}.png'
    output_file = f'Region_{i}.ome.tif'

    img_arr = io.imread(join(root_path, img_file))
    img_arr = img_arr.transpose((2, 0, 1))
    img_arr = img_arr[0:3, :, :]

    rgb_img_to_ome_tiff(
        img_arr,
        output_path=join(root_path, output_file),
        img_name='EUI',
        axes="CYX",
    )

# Linux command
# for i in {1..64}; do
#   ./bftools/bfconvert -tilex 512 -tiley 512 -pyramid-resolutions 6 -pyramid-scale 2 -compression LZW ./static_images/Region_${i}.ome.tif ./static_images/Region_${i}.pyramid.ome.tif
# done

# img_file = rf'C:\Users\bunny\Desktop\GFTU\00a67c839.png'
# # Check if at least one command-line argument is given
# # arg for img_file
# if len(sys.argv) >= 2:
#     img_file = sys.argv[1]

# output_file = img_file.replace('.png', '.ome.tif')

# img_arr = io.imread(img_file)
# img_arr = img_arr.transpose((2, 0, 1))
# img_arr = img_arr[0:3, :, :]

# rgb_img_to_ome_tiff(
#     img_arr,
#     output_path=output_file,
#     img_name='EUI',
#     axes="CYX", )
