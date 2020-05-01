import os
import pathlib

###_________________________________________________
#Delete a directory
def deleteDir(path1):
        if(path1.is_file()):
            os.remove(path1)
        else:
            try:
                path1.rmdir()
            except WindowsError:
                for i in os.listdir(path1):
                    deleteDir(path1/i)
                path1.rmdir()

# or u can use shutil.rmtree(dirstr)