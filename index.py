import string
import random


# Characters to generate password from
characters = list(string.ascii_letters + string.digits + "~!@#$%^&*()`,.;[]{}")

def generate_random_password():
	# Password length
	length = int(input("[?] Password Length : "))

	# Shuffling the characters
	random.shuffle(characters)
	
	# Generate random characters
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	# Shuffle
	random.shuffle(password)

	# Print the output
	print("[!] Output :", "".join(password))
    


# Execute function
generate_random_password()