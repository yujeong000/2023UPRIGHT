import os
import shutil
def get_subdirectories(path):
    subdirectories = [os.path.join(path, d) for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return subdirectories

def make_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
def remove_dir(path):   
    if os.path.exists(path):
            shutil.rmtree(path)
        
def get_last_directory_name(path):
    # 경로를 나누고 마지막 요소를 반환
    return os.path.basename(os.path.normpath(path))

def get_files(path, extension):
    list_files = []
    
    for root, subdirs, files in os.walk(path):
        if len(files) > 0:
            for f in files:
                fullpath = os.path.join(root, f)
                if f.lower().endswith(extension):
                    list_files.append(fullpath)

    return list_files

def get_filename(self, file_path):
        filename = os.path.basename(file_path)
        return filename
    
    