
import random


#fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
def get_d(e, z):
    ###################################your code goes here#####################################

	#followed the slides as closely as I could to use the euclidean algorithm to get d
	d = [0,0]
	rs1 = [1,0]
	rs2 = [0,1]
	tempz = z
	while((e%z)!= 0):
		m = e%z
		quot = e//z
		d[0]=rs1[0] - quot*rs2[0]
		d[1]=rs1[1]-quot*rs2[1]
		rs1=rs2[:]
		rs2=d[:]
		e=z
		z=m
	if d[0] <= 0:
		while d[0] < 0:
			d[0]=d[0]+tempz
	return d[0]

    
def is_prime (num):
    if num > 1: 
      
        # Iterate from 2 to n / 2  
       for i in range(2, num//2): 
         
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0: 
               return False 
               break
           else: 
               return True 
  
    else: 
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    ###################################your code goes here#####################################
    #e is encryption, d is decrytion, n is p*q, z is phi of n
    #followed similar steps we took from hw except here we can get random e values
    #
    n = p*q
    z = (q-1)*(p-1)
    e = random.randrange(1,n)
    while (gcd(e, z)!=1): 
    #check e and z are relatively prime
        e = random.randrange(1,n)
    d= get_d(e,z)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    ###################################your code goes here#####################################
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!
    m = (ord(plaintext)) #m (message) is the plaintext
    # we need the public key and the value of n here. pk is two values
    e, n = pk
    ciphertext = pow(m, e, n) 
    #like in our hw, cipher text is (m^e) mod n = ciphertext
    return ciphertext

def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext
    d, n = pk
    #same as homework, (chipertext^d)modn = plaintext
    plaintext= chr((pow(ciphertext, d, n)))
    return ''.join(plaintext)

