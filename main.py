from symetric import Symetric
from rsa import RSADemo
from getpass import getpass
from cracker import Cracker

plain_text = getpass("Password: ")

cracker = Cracker()

print("-------------------- Symetric --------------------")

encrypted_text = cracker.encryptor.encrypt_text(plain_text)
print("Encrypted password = %s" %(encrypted_text))

decrypted_text = cracker.encryptor.decrypt_text(encrypted_text)
print("Decrypted password = %s" %(decrypted_text))


print("-------------------- Asymetric --------------------")

cracker.encryptor2.encrypt(plain_text)
print("Encrypted password = %s" %(cracker.encryptor2.encrypted))
cracker.encryptor2.decrypt(cracker.encryptor2.encrypted)
print("Decrypted password = %s" %(cracker.encryptor2.decrypted))

 
wordlist = cracker.readwordlist().decode('UTF-8')
guesspasswordlist = wordlist.split('\n')

cracker.bruteforce(guesspasswordlist, plain_text)
 
print("Your password is strong")
 