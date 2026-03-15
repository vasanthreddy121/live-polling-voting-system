import socket
import re

SERVER_IP = "192.168.1.8"   # change to server IP if different machine
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# SRN validation pattern
pattern = r"^PES2UG\d{2}[A-Z]{2}\d{3}$"

print("------ LIVE POLL ------\n")

print("Which OS do you prefer?\n")
print("1. Linux")
print("2. Windows")
print("3. Mac\n")

# get SRN
while True:
    srn = input("Enter your SRN: ").upper()

    if re.match(pattern, srn):
        break
    else:
        print("Invalid SRN format. Example: PES2UG25CS829\n")

# vote input
while True:
    try:
        vote = int(input("Enter your vote (1-3): "))
        if vote in [1,2,3]:
            break
    except:
        pass

    print("Invalid vote. Try again.")

# create packet
message = f"VOTE|{srn}|{vote}"

# send vote
sock.sendto(message.encode(), (SERVER_IP, PORT))

print("\nVote sent successfully!")
