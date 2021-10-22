import os
import pathlib
import __main__

#Редактируй здесь
progname = "SimpleIO.dll"
#Дальше не редактируй

currdir = None
if __name__ == '__main__':
    currdir = str(pathlib.Path(__file__).parent.resolve())
else:
    currdir = str(pathlib.Path(__main__.__file__).parent.resolve())

os.chdir(currdir)
dotnetcmd = 'dotnet "' + currdir + os.path.sep + progname + '"'
os.system("start " + dotnetcmd)
