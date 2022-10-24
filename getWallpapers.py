import os
import ctypes
import shutil

user32 = ctypes.windll.user32
f_width = user32.GetSystemMetrics(0)
f_height = user32.GetSystemMetrics(1)

def copy_files(base_folder):
  source_folder = os.path.expanduser('~') + '/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/'
  destination_folder = base_folder

  shutil.copytree(source_folder, destination_folder)
  return destination_folder

def convert_to_images(base_folder):
  for file in os.listdir(base_folder):

   head, tail = os.path.splitext(file)
   if not tail:
       src = os.path.join(base_folder, file)
       dst = os.path.join(base_folder, file + '.jpg')

       if not os.path.exists(dst): # check if the file doesn't exist
           os.rename(src, dst)

# TODO: Segmentar en carpetas segun dimensiones de imagen
def group_by_screensize(base_folder):
  from PIL import Image
  for file in os.listdir(base_folder):
    im = Image.open(os.path.join(base_folder, file))
    i_width, i_height = im.size
    if i_width == f_width and i_height == f_height:
      print(file)
    elif i_width == f_height and i_height == f_width:
      print(file)
    else:
      im.close()
      os.remove(os.path.join(base_folder, file))


# TODO: * Destination_folder debera ser input
def main():
  folder_name = r"C:/Users/bakur/OneDrive/Escritorio/Wallpapers/"

  copy_files(folder_name)
  convert_to_images(folder_name)
  group_by_screensize(folder_name)


main()