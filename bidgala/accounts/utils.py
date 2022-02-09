# Standard library imports
import base64
import string
import json
import random

# Related third party imports
from Crypto.Cipher import AES

# Local application/library specific imports



def random_string(stringLength=10):
	""" This method is used to generate random string.

	Args:
		key: The secret key.
		plaintext: message to be encrypted
	
	Returns:
		It returns a encrypted string

	"""
	letters = string.ascii_lowercase + '0123456789'
	return ''.join(random.choice(letters) for i in range(stringLength))



def encrypt(key, plaintext):
	""" This method is used to ecrypt a message.

	Args:
		key: The secret key.
		plaintext: message to be encrypted
	
	Returns:
		It returns a encrypted string

	"""
	cipher = AES.new(key, AES.MODE_CTR)
	ct_bytes = cipher.encrypt(plaintext.encode())
	nonce = base64.b64encode(cipher.nonce).decode('utf-8')
	ct = base64.b64encode(ct_bytes).decode('utf-8')
	result = json.dumps({'nonce':nonce, 'ciphertext':ct})
	return base64.urlsafe_b64encode(result.encode())
 


def decrypt(key, ciphertext):
	""" This method is used to decrypt a message.

	Args:
		key: The secret key.
		ciphertext: message to be decrypted
	
	Returns:
		It returns a decrypted string

	"""
	json_input = base64.urlsafe_b64decode(ciphertext).decode()
	b64 = json.loads(json_input)
	ct = base64.b64decode(b64['ciphertext'])
	nonce = base64.b64decode(b64['nonce'])
	cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
	return cipher.decrypt(ct)




def clear_messages(messages, request):
	storage = messages.get_messages(request)
	for _ in storage:
		pass
	storage.used = True
	return messages