import sys
import random
import base64
from Crypto.Util import number
 
 

f = open('g.txt','r')
g = int(f.readline())
f.close()

f = open('p.txt','r')
p = int(f.readline())
f.close()

# Begin
print("INPUT:")
print("p= ",p)
print("g= ",g)

# Alice Sends Bob A = g^a mod p
#get random a
a = int(random.uniform(1,g))
print("a= ",a)
A = pow(g,a,p)#(g**a)%p	
# Bob Sends Alice B = g^b mod p
b = int(random.uniform(1,g))
print("b= ",b)
B = pow(g,b,p)#(g**b)%p
# Alice Computes Shared Secret: s = B^a mod p
KAlice = pow(B,a,p)#(B**a)%p
print("key ALice:",KAlice)
# Bob Computes Shared Secret: s = A^b mod p
KBob = pow(A,b,p)#(A**b)%p
print("Key Bob",KBob)