import shutil
import os

print(os.getcwd())
os.chdir('FilesToSort')
for filename in os.listdir('.'):
    file_extension = filename.split('.')[-1]
    try:
        os.mkdir(file_extension)
    except OSError:
        pass
    finally:
        shutil.move(filename, file_extension)
