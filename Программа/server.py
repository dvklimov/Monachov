import socket
import hashlib
import sys
import random
import json
import binascii
from Crypto.Cipher import AES
from Crypto import Random
import time



#start server
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.listen(1)
print('Server started')
conn, addr = sock.accept()




conn.close()
sock.close()