import os

# specify the directory where the files are located
directory = '/path/to/folder'

# use os.listdir() to get a list of all files in the directory
for filename in os.listdir(directory):
    # check if the file ends with ".template"
    if filename.endswith(".template"):
        # construct the full path to the old file name
        old_path = os.path.join(directory, filename)
        # construct the new file name by removing ".template"
        new_path = os.path.join(directory, filename[:-9])
        # use os.rename() to rename the file
        os.rename(old_path, new_path)