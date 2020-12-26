import sys
from tools import *


def menu():
	try:
		user_input = input("\nEncrypt or Decrypt[e/d] (q to quit): ")		
		while user_input.lower() != 'q':
			base64_opt = input("\nDo you want to switch to Base64?[y/n]: ")
			if base64_opt.lower() == 'y':
				if user_input == 'e':
					text = input("\nEnter the text you want to encrypt: ")
					print(f"Base64 Encrypted: {base64enc(text)}")
				elif user_input == 'd':
					text = input("\nEnter the text you want to decrypt: ")
					print(f"Decrypted: {base64dec(text)}")				
			else:
				if user_input.lower() == 'e':
					value = input("\nEnter the shift value(default=13): ")
					if not value:
						value = 13

					text = input("\nEnter the text you want to encrypt: ")
					
					try:
						print(f"Encrypted: {encrypt(text, int(value))}")
					except ValueError:
						print("\nPlease enter a valid shift value. ")

				if user_input.lower() == 'd':
					value = input("\nEnter the shift value(default=13): ")
					if not value:
						value = 13

					text = input("\nEnter the text you want to decrypt: ")
					print(f"Decrypted: {decrypt(text, int(value))}")	

			user_input = input("\nEncrypt or Decrypt[e/d] (q to quit)")
	except KeyboardInterrupt:
		print("\n\nYou have caused a keyboard interrupt. Exiting...")
		sys.exit(0)


# menu()