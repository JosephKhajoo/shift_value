import argparse
from tools import *
from menu import menu

parser = argparse.ArgumentParser(description='Shift value encryptor.')

parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt option\n')
parser.add_argument('-b', '--base64', action='store_true', help='Switch to Base64\n')
parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt option\n')
parser.add_argument('-s', '--shift', type=int, default=13, help='Specify the shift value(default=13)\n')
parser.add_argument('-t', '--text', type=str, help='Specify the text you wanna encrypt or decrypt\n')
parser.add_argument('-i', '--interactive', action='store_true', help='Enter the interactive prompt\n')

args = parser.parse_args()


def main():
	if args.interactive:
		menu()

	if args.base64:
		if args.decrypt:
			print(f"\nBase64 Decrypted: {base64dec(args.text)}")
		elif args.encrypt:
			print(f"\nBase64 Encrypted: {base64enc(args.text)}")
	else:
		try:
			if args.decrypt:
				print(f"\nDecrypted: {decrypt(args.text, args.shift)}")
			elif args.encrypt:
				print(f"\nEncrypted: {encrypt(args.text, args.shift)}")

		except TypeError:
			if not isinstance(args.text, int):
				print("\nPlease only enter strings... ")
			
			else:
				print("\nPlease specify the following arguments: -s/--shift, -t/--text")


if __name__ == '__main__':
	main()