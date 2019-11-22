import os


def getFiles(path, suffix):
     return [os.path.join(root, file) for root, dirs, files in os.walk(path) for file in files if file.endswith(suffix)]