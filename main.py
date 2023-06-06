from tkinter import filedialog
from Assets.secretKey import *


file = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
if not file:
    print("No file selected")
    input("Press ENTER to exit ")
    exit()
print(file)
encrypt_or_decrypt = input(
    "Would you like to encrypt or decrypt? (E/D) ").lower()
while True:
    if encrypt_or_decrypt == "e" or encrypt_or_decrypt == "d":
        break
    else:
        encrypt_or_decrypt = input("Please enter either E or D ")
password = input("What's the password? ")
password = hashPass(password)

with open(file, 'r') as f:

    content = f.read()


with open(file, 'w') as f:
    if encrypt_or_decrypt == "e":
        new_content = encrypt(content, password)
        f.write(new_content)
        print("Done, your file has been encrypted")
    elif encrypt_or_decrypt == "d":
        new_content = decrypt(content, password)
        f.write(new_content)
        print("Done, your file has been decrypted")
    input("Press ENTER to close ")
