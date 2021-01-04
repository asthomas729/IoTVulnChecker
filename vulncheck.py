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

def main():
    try:
        while(True):
            print('''
            [1] Scan Current Device (All Features)
            [2] List Visible IoT Devices
            [3] Check Configuration Files
            [4] Check Passwords
            [5] Find IDS
            [6] Find SIEM
            [7] Find Firewall
            [8] Generate Report with Existing Data
            [0] Exit
            '''
            )
            choice = input("Choose an option: ")
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
