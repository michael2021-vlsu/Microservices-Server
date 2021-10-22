import os
import pathlib
import __main__

#Редактируй здесь
launcher_paths = ["Сервис 1", "Сервис 2", "Сервис 3", "Сервис 4"]
#Дальше не редактируй

currdir = None
if __name__ == '__main__':
    currdir = str(pathlib.Path(__file__).parent.resolve())
else:
    currdir = str(pathlib.Path(__main__.__file__).parent.resolve())

os.chdir(currdir)
for item in launcher_paths:
    launchstr = currdir + os.path.sep + item + os.path.sep + 'launch.py"'
    os.system('start python "' + launchstr)