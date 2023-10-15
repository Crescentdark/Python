import netfilterqueue
import scapy.all as scapy

ack_list = []

def set_load(packet, load):
    