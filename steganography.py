import cv2
import os

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

img = cv2.imread('img.png')

mess = input("enter the message")
password = input("enter the password")

k = 0
m = 0
n = 0
z = 0

length = len(mess)

shift = int(input("enter shift for the message"))
message = ""
for char in mess:
    if char.isalpha():
       ascii_offset = ord('a') if char.islower() else ord('A')
       encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
       message += encrypted_char
    else:
       message += char


for i in range(length):
    img[n, m, z] = (d[message[i]] ^ d[password[k]])%256
    m = m+1
    n = n+1
    z = (z + 1) % 3
    k = (k+1) % len(password)


img1 = cv2.imwrite("encryption.png", img)
os.system("start encryption.png")
print("Encryption is successfully completed")

k = 0
m = 0
n = 0
z = 0

while True:
    decpassword = input("Enter the password for Decryption")
    dec_shift = int(input("enter shift back to get original message"))
    decryption = ""
    decreptmessg = ""
    if decpassword == password:
        for i in range(length):
            decryption += c[(img[n, m, z] ^ d[password[k]]) % 256]
            m = m + 1

            n = n + 1
            z = (z + 1) % 3
            k = (k + 1) % len(password)


        for char in decryption:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                decrypted_char = chr((ord(char) - ascii_offset - dec_shift + 26) % 26 + ascii_offset)
                decreptmessg += decrypted_char
            else:
                decreptmessg += char

        print("decrypted message", decreptmessg)
        break
    else:
        print("Enter the correct password")
