#KIR18686921 Christopher Kirby
import pyshark
import time
import struct

def detection():
    #initiate pyshark
    capture = pyshark.LiveCapture()
    capture.sniff(timeout= 20)
    last_IP = ""
    last_count = 0
    #run until 5000 packets have been captured (this can be removed to run indefinately)
    for packet in capture.sniff_continuously(packet_count=5000):
        try:
            localtime = time.asctime(time.localtime(time.time()))
            src_addr = packet.ip.src #the ip of the incoming connection
           
            print("Checking Packet")
            #check if the IP addresses if it does then increase the count
            if str(src_addr) == str(last_IP):
                last_count = last_count + 1
                #if the count exceeds 30 consecutive connections notify the user of a possible attack
                if last_count > 30:
                    print("%s Possible Attack Detected From Ip: %s"%(localtime,src_addr))     
            else:
                last_count = 0
            #set the last ip address
            last_IP = src_addr
                  
        except AttributeError as e:

            pass
        

