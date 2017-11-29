import time
import sys
import requests
import xlwt
from scapy.all import *
from scapy.layers.l2 import ARP

MAGIC_FORM_URL = 'https://api.cloudstitch.com/afab/itrain-spreadsheet/datasources/sheet'
timeStarted = False




def record_time_start():
    connected = False
    data = {
    #"Timestamp": time.strftime("%Y-%m-%d %H:%M"),
    "Timestamp": time.strftime(("%Y-%m-%d %H:%M:%S.%f")[:-3]),
    "Measurement": 'Start'
    }

    timeStarted = True
    while(connected == False):

        try:
            requests.post(MAGIC_FORM_URL, data)
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("zzzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue

    #requests.post(MAGIC_FORM_URL, data)

def record_time_end():
    data = {
    "Timestamp": time.strftime(("%Y-%m-%d %H:%M:%S.%f")[:-3]),
    "Measurement": 'End'
    }
    timeStarted = False
    requests.post(MAGIC_FORM_URL, data)

def arp_display(pkt):
  timestamp = time.strftime(("%Y-%m-%d %H:%M:%S.%f")[:-3])
  print "passed line 28"
  if pkt[ARP].op == 1:
    print "line 30"
      #if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
    print "line 33"
    if (pkt[ARP].hwsrc == 'c4:85:08:a0:c4:09' and timeStarted == False): # pets dash button / put your own MAC here
        print "Pushed pets button. Timer has started. Timestamp: "+timestamp
        record_time_start()
    elif (pkt[ARP].hwsrc == 'c4:85:08:a0:c4:09' and timeStarted == True): # pets
        print "Pushed pets button. Timer has ended."+timestamp
        record_time_end()
    else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc



print sniff(prn=arp_display, filter="arp", store=0, count=10)
print "Done."