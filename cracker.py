from symetric import Symetric
from rsa import RSADemo
import hashlib
from urllib.request import urlopen

class Cracker:
    def __init__(self):
        self.url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
        self.encryptor = Symetric()
        self.encryptor2 = RSADemo()
 
    def readwordlist(self):
        try:
            wordlistfile = urlopen(self.url).read()
        except Exception as e:
            print("error:", e)
            exit()
        return wordlistfile
 
 
    def hash(self, wordlistpassword):
        result = self.encryptor.encrypt_text(wordlistpassword)
        return result
 
 
    def bruteforce(self, guesspasswordlist, actual_password):
        actual_password_hash = hash(actual_password)
        for guess_password in guesspasswordlist:
        
            if hash(guess_password) == actual_password_hash:
                print("Your password is:", guess_password,
                      "\nThis password is weak")
                exit()
 
