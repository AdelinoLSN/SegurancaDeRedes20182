class RSA(object):
	def __init__(self):
		self.publicKey = None
		self.privateKey = None
		self.n = None

	#Função auxiliar de modinv (inverso modular)
	def egcd(self,a, b):
	    if a == 0:
	        return (b, 0, 1)
	    else:
	        g, y, x = self.egcd(b % a, a)
	        return (g, x - (b // a) * y, y)

	#Função modular
	def modinv(self,a, m):
	    g, x, y = self.egcd(a, m)
	    if g != 1:
	        raise Exception('modular inverse does not exist')
	    else:
	        return x % m

	def primeInCommum(self,phi_n):
		for i in range(phi_n):
			if i!=1:
				count = 0
				for j in range(1,i):
					if(i%j == 0):
						count+=1
				if(count == 1):
					if(phi_n%i != 0):
						return i

	def generateKeys(self,p,q):
		n = p*q
		phi_n = (p-1)*(q-1)

		e = self.primeInCommum(phi_n)
		d = self.modinv(e,phi_n)

		self.publicKey = e
		self.privateKey = d
		self.n = n

	def encrypt(self,plain_text,e,n):
		ascii_text = [0(c) for c in plain_text]

		encrypted_ascii = []
		for char in ascii_text:
			encrypted_ascii.append((int(char)**e)%n)

		ascii_text = ""
		for asc in encrypted_ascii:
			ascii_text+=str(asc)
			ascii_text+=" "
		ascii_text=ascii_text[:-1]

		return ascii_text

	def decrypt(self,encrypted_ascii,d,n):
		ascii_encrypted = encrypted_ascii.split(' ')

		decrypted_ascii = []
		for char in ascii_encrypted:
			decrypted_ascii.append(((int(char))**d)%n)

		decrypted_text = ''.join(chr(i) for i in decrypted_ascii)

		return decrypted_text

def main(p,q):
	rcarsa = RSA()
	rsa.generateKeys(p,q)