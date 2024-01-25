#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is nmap automation tool")
print("<----------------------------------->")

ip_addr = input("Please enter the IP adress you want to scan: ")
print("The IP you enetered is: ", ip_addr)
type(ip_addr)

resp = input(""" \nPlease enter the type of scan you wan to run
             1) SYN ACK Scan
             2)UDP Scan
             3)Comprehensive Scan""")

print("You have selected option: ", resp)