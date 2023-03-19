import os
import time
import sys

#crunch [usr] [usr2] 0123456789 [-o file]


def crunch(c):
     c = int(input('''\033[1;32m
     
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
          
  
     elif c == 1:
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
          
                   
     elif c == 1:
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
          
 
     elif c == 1:
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
          
                 
     else:
          print('error')       
          
      
 
          
          
          
     
          
          
crunch('c')
