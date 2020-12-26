import base64
import logging

alph = "abcdefghijklmnopqrstuvwxyz"


def base64enc(string: str):
	byte = string.encode("UTF-8")
	enc = base64.b64encode(byte)
	encoded_string = enc.decode("ascii")

	return encoded_string


def base64dec(string: str):
	try:
		byte = string.encode("UTF-8")
		dec = base64.b64decode(byte)
		decoded_string = dec.decode("ascii")
	except Exception:
		print("\nAn error occured... Make sure you are using a valid base64 encoded string")
	else:
		return decoded_string


def _locate(ch):
	for i in range(len(alph)):
		if alph[i] == ch:
			return i


def _file_contents(path):
	text = ""
	with open(path, 'r') as file:
		for line in file.readlines():	
			text += line
		return text


def encrypt(text: str, shift_val: int):
	ciph = ""
	for ch in text:
		if ch != " ":
			index = _locate(ch)
			if (index + shift_val) >= len(alph):
				chr_len = len(alph) - index
				ch = alph[shift_val - chr_len]
				ciph += ch
			else:
				ch = alph[index + shift_val]
				ciph += ch
		else:
			ciph += " "

	return ciph


def decrypt(text: str, shift_val: int):
	ciph = ""
	for ch in text: 
		if ch != " ":
			index = _locate(ch)
			if shift_val >= index:
				chr_len = shift_val - index
				if chr_len == 0:
					ciph += 'a'
				else:
					ch = alph[len(alph) - chr_len]
					ciph += ch

			else:
				ch = alph[index - shift_val]
				ciph += ch

		else:
			ciph += " "

	return ciph