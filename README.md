# shift_value

This is a command line tool written with Python for encryption and decryption of simple algorithms such as rot13 or base64. 

usage: shift_cipher.py [-h] [-e] [-b] [-d] [-s SHIFT] [-t TEXT] [-i]

Shift value encryptor.

optional arguments:
  -h, --help            show this help message and exit
  -e, --encrypt         Encrypt option
  -b, --base64          Switch to Base64
  -d, --decrypt         Decrypt option
  -s SHIFT, --shift     Specify the shift value(default=13)
  -t TEXT, --text TEXT  Specify the text you wanna encrypt or decrypt
  -i, --interactive     Enter the interactive prompt

python shift_cipher.py -i
python shift_cipher.py -e -b -t "Hello World"
python shift_cipher.py -d -s 13 -t "Hello World"


!! WARNING !! very shitty code ahead
