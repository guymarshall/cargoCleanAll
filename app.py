import os

current_dir = os.getcwd()

for subdir in os.listdir(current_dir):
    if os.path.isdir(subdir):
        os.chdir(subdir)
        os.system("cargo clean")
        os.chdir(current_dir)
