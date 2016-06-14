import random
import string
import os.path


number = random.randrange(100,999)
string.characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'

characters_section = ''.join(random.choice(string.characters) for _ in range(8))  
password = str(number) + characters_section

account = input('This password is for: ')
your_pass =  'Your password for {} is: {}\n'.format(account, password)
print(your_pass)

save = '/home/andrew/python'
file_name = input("What is the name of the file: ")
completeName = os.path.join(save, file_name +".dat")         
with open(completeName, "a") as file1:
    file1.write(your_pass)