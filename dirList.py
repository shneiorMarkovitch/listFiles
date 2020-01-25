from os import listdir
from os.path import isfile, join
import utility
mypath='D:\shneior\E2Etest'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)
utility.writeOnCsv(onlyfiles)
