import os
import shutil

def move_files(old_dir, new_dir, postfix, del_or_not=True):
    if not os.path.exists(old_dir):
        print(f'Error: The source folder {old_dir} does not exist.')
        return
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    for root, dirs, files in os.walk(old_dir):
        for file in files:
            if file.endswith(postfix):
                source_file = os.path.join(root, file)
                destination_file = os.path.join(new_dir, file)
                try:
                    shutil.move(source_file, destination_file)
                    print(f'Moved from {old_dir} to {new_dir}: {file}')
                    if del_or_not and os.path.exists(source_file):
                        os.remove(source_file)
                        print(f'Deleted original file: {source_file}')
                except Exception as e:
                    print(f'Error moving file {source_file}: {e}')
    print('Move completed! ')

old_dir = 'E:/Research/Data/SDO/HMI/SHARP/AR3664/'
new_dir = 'E:/Research/Data/SDO/HMI/SHARP/magnetogram/'
postfix = '.magnetogram.fits'
del_or_not = True

move_files(old_dir, new_dir, postfix, del_or_not)
    