from ast import Assign
from function import *
from kerangajaib import kerangajaib
from F04 import *
from F06 import *
from F07 import *
from F12 import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('folder')
args = parser.parse_args()

dfuser = csv_to_array("C:\TubesDaspro\tubesdaspro\user.csv")
dfgame = csv_to_array("C:\TubesDaspro\tubesdaspro\game.csv")
dfriwayat = csv_to_array("C:\TubesDaspro\tubesdaspro\riwayat.csv")
dfkepemilikan = csv_to_array("C:\TubesDaspro\tubesdaspro\kepemilikan.csv")

end = False

while end == False:
    command = input(">>>").lower()
    log = False
    admin = False
    if command == "login":
        


