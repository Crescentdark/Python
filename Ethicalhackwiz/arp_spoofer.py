import scapy.all as scapy 
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    
