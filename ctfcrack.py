

def caesar(text, mode):
	result = ""
	if mode == "encode":
		for j in range(1, 26):
			for i in range(len(text)):
				char = text[i]
				if(char.isupper()):
					result += chr((ord(char) + j - 65) % 26 + 65)
				else:
					result += chr((ord(char) + j - 97) % 26 + 97)
			print("* Shift: ", j, " ", result)
			result = ""
	elif mode == "decode":
		for j in range(1, 26):
			for i in range(len(text)):
				char = text[i]
				if(char.isupper()):
					result += chr((ord(char) - j - 65) % 26 + 65)
				else:
					result += chr((ord(char) - j - 97) % 26 + 97)
			print("* Shift: ", j, " ", result)
			result = ""

text = "aLper"
caesar(text, "encode")
print()
text= "yJncp"
caesar(text, "decode")