import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get.payload())
    if scapy_packet.haslayer(scapy.DNSRR)