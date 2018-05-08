import shutil
import os

extension_to_folder = {}
print(os.getcwd())
os.chdir('FilesToSort')
for filename in os.listdir('.'):
    file_extension = filename.split('.')[-1]
    if file_extension in extension_to_folder.keys():
        shutil.move(filename, extension_to_folder[file_extension])
    else:
        folder = input('What category would you like to sort .{} files into? '.format(file_extension))
        extension_to_folder[file_extension] = folder
        try:
            os.mkdir('{}'.format(folder))
        except OSError:
            pass
        finally:
            shutil.move(filename, extension_to_folder[file_extension])
