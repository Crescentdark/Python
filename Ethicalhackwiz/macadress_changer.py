import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="Interface that changes Mac adress")
    parser.add_option("-m","--mac", dest="new_mac", help="New Mac adress")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, or use --help")
    elif not options.new_mac:
        parser.error("[-] Please specify an interface, or use --help")
    return options


def change_mac(interface, new_mac):
    print(f"[+] Changing Mac address for {interface} to {new_mac} ")

    subprocess.call(f"ifconfig {interface} down")
    subprocess.call(f"ifconfig {interface} hw ether" + new_mac,)
    subprocess.call(f"ifconfig {interface} up")


options = get_arguments()
#change_mac(options.interface, options.new_mac)

def get_c_mac(interface):
    ifcresult = subprocess.check_output(["ifconfig", interface])
    macsearchresult = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifcresult)

    if macsearchresult:
        print(macsearchresult.group(0))
    else:
        print("[-] Couldnt read MAc address")