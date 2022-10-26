import os
import ctypes
import shutil

user32 = ctypes.windll.user32
f_width = user32.GetSystemMetrics(0)
f_height = user32.GetSystemMetrics(1)

images_path = '/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/'
extension_convert = '.jpg'


def copy_files():
    source_folder = os.path.expanduser('~') + images_path
    destination_folder = destination

    if not os.path.isdir(destination):
        shutil.copytree(source_folder, destination_folder)
        return destination_folder
    else:
        print("Folder already exists")


def convert_to_images():
    for file in os.listdir(destination):

        head, tail = os.path.splitext(file)
        if not tail:
            src = os.path.join(destination, file)
            dst = os.path.join(destination, file + extension_convert)

            if not os.path.isdir(dst):
                os.rename(src, dst)


def make_folders_by_size():
    names = ['landscape', 'portrait']
    mode = 0o777

    for name in names:
        path = os.path.join(destination, name)
        os.mkdir(path, mode)


def group_by_screensize():
    from PIL import Image
    for file in os.listdir(destination):
        im = Image.open(os.path.join(destination, file))
        i_width, i_height = im.size
        im.close()
        if i_width == f_width and i_height == f_height:
            shutil.move(os.path.join(destination, file),
                        os.path.join(destination, 'landscape'))
        elif i_width == f_height and i_height == f_width:
            shutil.move(os.path.join(destination, file),
                        os.path.join(destination, 'portrait'))
        else:
            os.remove(os.path.join(destination, file))


def main():
    copy_files()
    convert_to_images()
    make_folders_by_size()
    group_by_screensize()


destination = raw_input("Enter the folder name to save images: ")
destination = os.path.join(os.getcwd(), destination)
main()