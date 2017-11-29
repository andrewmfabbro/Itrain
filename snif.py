from scapy.all import *
from scapy.layers.l2 import ARP


def arp_display(pkt):
    if pkt[ARP].op == 1:  # who-has (request)
        if pkt[ARP].psrc == '0.0.0.0':  # ARP Probe
            print
            "ARP Probe from: " + pkt[ARP].hwsrc


print sniff(prn=arp_display, filter="arp", store=0, count=10)
