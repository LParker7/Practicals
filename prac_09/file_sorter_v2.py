import shutil
import os

extension_to_folder = {}
print(os.getcwd())
os.chdir('FilesToSort')
for filename in os.listdir('.'):
    file_extension = filename.split('.')[-1]
    if file_extension not in extension_to_folder.keys():
        folder = input('What category would you like to sort .{} files into? '.format(file_extension))
        extension_to_folder[file_extension] = folder
        try:
            os.mkdir('{}'.format(folder))
        except OSError:
            pass
    shutil.move(filename, extension_to_folder[file_extension])
