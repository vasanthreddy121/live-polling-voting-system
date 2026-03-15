import socket
import threading
import time

SERVER_IP = "0.0.0.0"
PORT = 5000

# vote options
vote_count = {
    1: 0,
    2: 0,
    3: 0
}

options = {
    1: "Linux",
    2: "Windows",
    3: "Mac"
}

# store SRNs to prevent duplicate votes
voted_students = set()

# statistics
total_packets_received = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, PORT))

print("Server started...")
print(f"Listening on port {PORT}\n")


def display_results():
    while True:
        time.sleep(10)

        print("\n------ LIVE RESULTS ------")

        for k in vote_count:
            print(f"{options[k]} : {vote_count[k]}")

        print("--------------------------")
        print(f"Votes Received: {total_packets_received}")
        print(f"Unique Voters : {len(voted_students)}")
        print()


def receive_votes():
    global total_packets_received

    while True:
        data, addr = sock.recvfrom(1024)

        message = data.decode()
        total_packets_received += 1

        try:
            tag, srn, vote = message.split("|")
            vote = int(vote)

            if srn in voted_students:
                print(f"Duplicate vote ignored from {srn}")
                continue

            voted_students.add(srn)

            if vote in vote_count:
                vote_count[vote] += 1
                print(f"Vote received from {srn} → {options[vote]}")

        except:
            print("Invalid packet received")


# thread for displaying results
threading.Thread(target=display_results, daemon=True).start()

receive_votes()
