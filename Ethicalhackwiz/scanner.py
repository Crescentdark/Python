import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target", dest="target",help="target ip")
    options = parser.parse_args()