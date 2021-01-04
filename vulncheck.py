# Check the devices configuration
  # What passive security is there?
  # Configurations
  # Secure passwords
# Check for and list the security services protecting the device
  # What scanners and checkers are going on?
  # IDS
  # Tracking logs/SIEM
  # Firewall

# One-time scan
# Recurring scan/protection (just check certain things?)

# We wabt to ID the device and see what's already there
  # List IoT devices

# We want to ID the device and see what's already there
# Test for default creds
# List current CVEs
# List the findings from Mozilla IoT Privacy Site
# List most current updates

import os
import re

def locate_devices():
    # find the IP address and subnet mask
    # scan the subnet for devices
    # check if the devices are IoT devices
    pass

def configs():
    # look in /etc for config files
    config_files = [os.path.join(root, name)
            for root, dirs, files in os.walk("/etc")
            for name in files
            if name.endswith((".conf", ".yml", ".cnf", ".ini", ".json", ".toml"))]
    # find clear-text passwords (regex for password, = or :, " or ')
    for file_name in config_files:
        try:
            f = open(file_name, 'r')
            for line in f.readlines():
                passwd = re.findall([Pp]assword\s*[:|=]*\s*['|\"]*.*['|\"]*",line)
                print('[+] ' + filename + ': ' + passwd)
            f.close()
        except:
            print("[-] An error occurred while opening " + filename)
            pass
    # look for other configuration issues/best practices (this may depend on type of file and program, need to compile a list)

def patch_level():
    # check patch level
    pass

def cve():
    # check CVEs
    pass

def comms():
    # check communication protocols (http/s, bluetooth, 4/5g, mqtt, zigbee, etc.)
    # look for end-to-end encryption
    pass

def passwords():
    # check for device users
    # check for device hashes
    # look for login methods (ssh, http/s, telnet, etc.)
    # find/check default creds
    # check common/weak passwords
    pass

def ids():
    # look for an IDS on the device
    pass

def siem():
    # look for evidence of a SIEM on the device
    # splunk universal forwarder
    # beats (filebeats, etc.)
    pass

def firewall():
    # check for active firewall on the device
    # check if traffic passes through a firewall
    pass

def choice1():
    # call the individual functions
    locate_devices()
    configs()
    cvs()
    comms()
    passwords()
    ids()
    siem()
    firewall()

def choice2():
    pass

def choice3():
    pass

def choice4():
    pass

def choice5():
    pass

def choice6():
    pass

def choice7():
    pass

def choice8():
    pass

def main():
    try:
        while(True):
            print('''
[1] Full Scan (including current device) 
[2] Scan Visible IoT Devices (network-based features)
[3] Check Configuration Files and Patch Level
[4] Check Passwords
[5] Find IDS
[6] Find SIEM
[7] Find Firewall
[8] Generate Report with Existing Data
[0] Exit
            '''
            )
            choice = input("[*] Choose an option: ")
            if(choice == "0"):
                print("[*] Quitting\n")
                break
            elif(choice == "1"):
                #ip_range = input("[*] IP address or range to scan: ")
                print("[*] Attempting full scan, this may take some time...")
            elif(choice == "2"):
                print("[*] Attempting to locate IoT devices...")
            elif(choice == "3"):
                print("[*] Finding configuration files...")
            elif(choice == "4"):
                print("[*] Checking for users...")
            elif(choice == "5"):
                print("[*] Looking for an IDS...")
            elif(choice == "6"):
                print("[*] Looking for a SIEM client...")
            elif(choice == "7"):
                print("[*] Looking for an active firewall...")
            elif(choice == "8"):
                print("[*] Checking existing data...")
    except KeyboardInterrupt:
        print("[*] Quitting\n")
    except:
        print("[-] An error has occurred\n")

if __name__ == "__main__":
    main()
