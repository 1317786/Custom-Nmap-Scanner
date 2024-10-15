import nmap

scanner = nmap.PortScanner()

print("Welcome! This is a simple nmap automation tool")
print("<----------------------------------------------------->")

ip_addr = input("Please enter the IP address you would like to scan: ")
print("The IP you have entered is: ", ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan \n""")
print("You have selected option: ", resp)

resp_dict = {'1': ['-v -sS', 'tcp'], '2': ['-v -sU', 'udp'], '3': ['-v -sS -sV -sC -A -O', 'tcp']}

if resp not in resp_dict.keys():
    print("Please enter a valid option")
else:
    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, "1-1024", resp_dict[resp][0])
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())

    protocol = resp_dict[resp][1]
    if protocol in scanner[ip_addr].all_protocols():
        print("Open Ports: ", list(scanner[ip_addr][protocol].keys()))
    else:
        print("No open ports found or the protocol is not used.")
