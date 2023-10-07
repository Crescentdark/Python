import subprocess

interface = input("interface >")
new_mac = input("new MAC >")

print(f"[+] Changing Mac address for {interface} to {new_mac} ")

subprocess.call(f"ifconfig {interface} down")
subprocess.call(f"ifconfig {interface} hw ether" + new_mac,)
subprocess.call(f"ifconfig {interface} up")