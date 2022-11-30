import sys,os,platform
from time import *
import datetime
from datetime import date
import time
	#--- Color  ---#
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray

from datetime import datetime

now = datetime.now()

dt_string = now.strftime("%H:%M:%S")	# dd/mm/YY H:M:S

today = date.today()

print(G+'''
 /$$        /$$$$$$  /$$    /$$ /$$$$$$$$       /$$   /$$
| $$       /$$__  $$| $$   | $$| $$_____/      | $$  | $$
| $$      | $$  \ $$| $$   | $$| $$            | $$  | $$
| $$      | $$  | $$|  $$ / $$/| $$$$$         | $$  | $$
| $$      | $$  | $$ \  $$ $$/ | $$__/         | $$  | $$
| $$      | $$  | $$  \  $$$/  | $$            | $$  | $$
| $$$$$$$$|  $$$$$$/   \  $/   | $$$$$$$$      |  $$$$$$/
|________/ \______/     \_/    |________/       \______/ 
                                                                                                                                                                                                                        ''')
print(W+''' 
    /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$
   |__  $$ /$$__  $$ /$$__  $$| $$$ | $$
      | $$| $$  \ $$| $$  \ $$| $$$$| $$
      | $$| $$$$$$$$| $$$$$$$$| $$ $$ $$
 /$$  | $$| $$__  $$| $$__  $$| $$  $$$$
| $$  | $$| $$  | $$| $$  | $$| $$\  $$$
|  $$$$$$/| $$  | $$| $$  | $$| $$ \  $$
 \______/ |__/  |__/|__/  |__/|__/  \__/                                                                                                                      
                                         '''+B+'\tv1.1')

print("\t"+B+"<<<<<<| "+R+"Love u jaan "+B+"|>>>>>>\n")
print("\t"+G+"Welcome "+B+"to"+R+" Termux"+G+"\t\t")
print("\tDATE : ",today,"\t\t\t")
print("\tTIME : ",dt_string,"\t\t\t")
print("\tGitHub : "+R+" SilentCoder2")
print("\t"+P+"Welcome SILENT-CODER"+G+'\n')
print(C + '-' *20 +R+ 'Repository'+C+'-' *20)
os.system('ls $HOME')
print('-' *50)
os.system('cd')
