import socket
import threading
import time

SERVER_IP = "0.0.0.0"
PORT = 5000

# vote options
options = {
    1: "Linux",
    2: "Windows",
    3: "Mac"
}

vote_count = {1: 0, 2: 0, 3: 0}
voted_students = set()

total_packets_received = 0
expected_packets = 0  # based on sequence numbers


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, PORT))

print("Server started...")
print(f"Listening on port {PORT}\n")


def display_results():
    while True:
        time.sleep(5)

        print("\n------ LIVE RESULTS ------")

        for k in vote_count:
            print(f"{options[k]} : {vote_count[k]}")

        print("--------------------------")
        print(f"Packets Received : {total_packets_received}")
        print(f"Expected Packets : {expected_packets}")

        loss = expected_packets - total_packets_received
        loss = max(loss, 0)

        if expected_packets > 0:
            loss_percent = (loss / expected_packets) * 100
        else:
            loss_percent = 0

        print(f"Packet Loss      : {loss}")
        print(f"Loss Percentage  : {loss_percent:.2f}%")
        print(f"Unique Voters    : {len(voted_students)}")
        print()


def receive_votes():
    global total_packets_received, expected_packets

    while True:
        data, addr = sock.recvfrom(1024)
        message = data.decode()

        try:
            tag, srn, vote, seq = message.split("|")
            vote = int(vote)
            seq = int(seq)

            total_packets_received += 1
            expected_packets = max(expected_packets, seq)

            if srn in voted_students:
                print(f"Duplicate vote ignored from {srn}")
                continue

            voted_students.add(srn)

            if vote in vote_count:
                vote_count[vote] += 1
                print(f"Vote received from {srn} → {options[vote]}")

        except:
            print("Invalid packet received")


threading.Thread(target=display_results, daemon=True).start()
receive_votes()
