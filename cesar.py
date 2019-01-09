#coding: utf-8

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_list = list(alphabet.lower())

def encrypt():
	message = raw_input("digite sua mensagem: ")
	message = message.lower()
	message = list(message)

	for i in xrange(len(message)):
		caracter = message[i]
		if(caracter in alphabet_list):
			position = alphabet_list.index(caracter)
			position_codified = (position+3)%26
			message[i] = alphabet_list[position_codified]

	message_encrypted = ""

	for caracter in message:
		message_encrypted+=caracter

	print message_encrypted

def decrypt():
	message = raw_input("digite sua mensagem: ")
	message = message.lower()
	message = list(message)

	for i in xrange(len(message)):
		caracter = message[i]
		if(caracter in alphabet_list):
			position = alphabet_list.index(caracter)
			position_codified = (position-3)%26
			message[i] = alphabet_list[position_codified]

	message_encrypted = ""

	for caracter in message:
		message_encrypted+=caracter

	print message_encrypted

def main():
	final = False
	while not final:
		option = raw_input("Digite o número da opção: \n1 - Encriptar\n2 - Decriptar\n0 ou Outro - Sair\n")
		try:
			if int(option) == 1:
				encrypt()
			elif int(option) == 2:
				decrypt()
			else:
				final = True
		except Exception as e:
			final = True

main()