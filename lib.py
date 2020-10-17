import os


def folderToTab(folder):
    path = folder
    tab = []
    obj = os.scandir(path) 

    for entry in obj : 
        if entry.is_dir() or entry.is_file() and entry.name != '.DS_Store': 
            tab.append(f'{os.path.abspath(folder)}/{entry.name}')

    obj.close()
    return tab


def folderToTabFront(folder):
    path = folder
    tab = []
    obj = os.scandir(path) 

    for entry in obj : 
        if entry.is_dir() or entry.is_file() and entry.name != '.DS_Store': 
            tab.append(f'{entry.name}')

    obj.close()
    return tab
