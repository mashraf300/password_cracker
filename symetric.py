from cryptography.fernet import Fernet


class Symetric:

	def __init__(self):
		self.key = Fernet.generate_key()


	def encrypt_text(self, plain_text):
	    f = Fernet(self.key)
	    encrypted_text = f.encrypt(bytes(plain_text, "UTF-8"))
	    return encrypted_text.decode()


	def decrypt_text(self, encrypted_text):
	    f = Fernet(self.key)
	    return f.decrypt(bytes(encrypted_text,"UTF-8")).decode()


