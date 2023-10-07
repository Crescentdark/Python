import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i","--interface", dest="interface", help="Interface that changes Mac adress")
parser.add_option("-m","--mac", dest="new_mac", help="New Mac adress")


parser.parse_args()

interface = input("interface >")
new_mac = input("new MAC >")

print(f"[+] Changing Mac address for {interface} to {new_mac} ")

subprocess.call(f"ifconfig {interface} down")
subprocess.call(f"ifconfig {interface} hw ether" + new_mac,)
subprocess.call(f"ifconfig {interface} up")