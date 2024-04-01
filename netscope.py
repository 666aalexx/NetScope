#!/usr/bin/python3

import sys; import os; import argparse; import socket; import signal; import time

#Colours
redColour = "\033[31m"
greenColour = "\033[32m"
yellowColour = "\033[33m"
blueColour = "\033[34m"
resetColour = "\033[0m"

def sig_handler(sig, frame):
    sys.exit(1)

signal.signal(signal.SIGINT, sig_handler)

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", required=True)
args = parser.parse_args()

def main():
    ip = args.target
    ports = [21, 22, 25, 53, 80, 110, 143, 443, 3389]
    with open("openPorts.txt", "w") as output:
        output.write("PORT\tSERVICE/VERSION\n")
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            try:
                s.connect((ip, port))
                result = s.recv(1024).decode("utf-8").strip()
                print(f"{greenColour}[+]{resetColour} {port}")
                output.write(f"{port}\t\t{result}\n")
            except socket.timeout:
                print(f"{greenColour}[+]{resetColour} {port}")
                output.write(f"{port}\t\tN/A\n")
            except:
                pass

if __name__ == "__main__":
    main()

