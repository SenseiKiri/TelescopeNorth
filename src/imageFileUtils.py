from boltons import fileutils


def getAllImagesFromFolder():
    """
    This method will return all PNG/JPG/JPEG Images in Folder
        ./resources/exampleImages/
    :return: List of filepath-strings
    """
    filePath = './resources/exampleImages/'
    fileGenerator = fileutils.iter_find_files(filePath, patterns=['*.png', '*jpg', '*jpeg'])
    fileList = []
    for file in fileGenerator:
        fileList.append(file)
    return fileList
