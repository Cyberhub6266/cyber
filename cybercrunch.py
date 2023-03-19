import time
import sys
import datetime
import subprocess
import os
#import crunch

#logo
os.system('clear')
def logo(l):
     l = '''\033[1;31m
     
     

 .---.     .---. .----. .-. .-..-. .-. .---. .-. .-.
/  ___}   /  ___}| {}  }| { } ||  `| |/  ___}| {_} |
\     }   \     }| .-. \| {_} || |\  |\     }| { } |
 `---'     `---' `-' `-'`-----'`-' `-' `---' `-' `-'Create_By_©®
   
     '''
     for i in l:
          time.sleep(0.001)
          sys.stdout.write(i)
          sys.stdout.flush()
     
logo('l')
'''


'''
d = datetime.datetime.now()
print(d)

def t():
     time.sleep(2)
          
t()


def any(ins):
     ins =input( '''\033[1;35m
     
[+]Please Type Any Key[+] ''')



     for i in ins:
          time.sleep(0.01)
          sys.stdout.write(i)
          sys.stdout.flush()
          
      
     if ins != "" or ins =="":
          print('''\033[1;32m

[+]Please wait Installing[+]   
''')

          time.sleep(1)
          os.system('apt update -y')
          os.system('apt upgrade -y')
          os.system('apt install crunch')
          os.system('apt install figlet')
     
     
     else:
          print('''\033[1;36m
 
[+]Something Wrong[+] 
     
     ''')
         
          
          
          
     
     
     
any('ins')

def install():
     print('''\033[1;31m
          
[+]All Tool Installed[+] 
              
     ''')
     
     time.sleep(2)

def clear():
     
     os.system('clear')
     
     
clear()

logo('l')


def help(h,show):
     h = input('''
[+] Please Type -h/-H [+]    
''')


     show = '''\033[1;32m
     


      [+] crunch [min] [max] [cn] [output] [+]
      ----------------------------------------
      [1]      Number    [+]
      [2]      Character [+]
      [3]  Cap Character [+]
      [4]  N+C Character [+]
      [5]      Output    [+]
      ----------------------------------------
         
     
     
'''

     for g in show:
           time.sleep(0.001)
           sys.stdout.write(g)
           sys.stdout.flush()
          






help('h','show')


#crunch [usr] [usr2] 0123456789 [-o file]


def crunch(c):
     c = int(input('''\033[1;34m
     
[+]Enter Your Target[+]
     '''))
     
     
     if c == 1:
          usr = int(input('''
[+]Enter Min Num[+]      
          '''))
          
          usr2 = int(input('''
[+]Enter Max Num[+]
          '''))
          
          file = input('''
[+]Enter File Name
          ''')
          
          use = 'crunch {} {} 0123456789 -o {}.txt'.format(usr,usr2,file)
          
          
          os.system(use)
          
  
     elif c == 2:
          usr = int(input('''
[+]Enter Min Num[+]      
          '''))
          
          usr2 = int(input('''
[+]Enter Max Num[+]
          '''))
          
          file = input('''
[+]Enter File Name
          ''')
          
          use = 'crunch {} {} abcdefghijklmnopqrstuvwxyz -o {}.txt'.format(usr,usr2,file)
          os.system(use)
                   
     elif c == 3:
          usr = int(input('''
[+]Enter Min Num[+]      
          '''))
          
          usr2 = int(input('''
[+]Enter Max Num[+]
          '''))
          
          file = input('''
[+]Enter File Name
          ''')
          
          use = 'crunch {} {} ABCDEFGHIJKLMNOPQRSTUVWXYZ -o {}.txt'.format(usr,usr2,file)  
          os.system(use)
 
     elif c == 4:
          usr = int(input('''
[+]Enter Min Num[+]      
          '''))
          
          usr2 = int(input('''
[+]Enter Max Num[+]
          '''))
          
          file = input('''
[+]Enter File Name
          ''')
          
          use = 'crunch {} {} 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#£_&-+/*:;!?€¥$¢°=\%©®™[]<> -o {}.txt'.format(usr,usr2,file)
          os.system(use)
                 
     else:
          print('error')       
          
      
 
          
          
          
     
          
          
crunch('c')
