# live-polling-voting-system
# Live Polling and Voting System (UDP)

## Project Overview

This project implements a **real-time live polling system using UDP socket programming**.
Multiple clients (students) send their votes to a central server. The server collects the votes, prevents duplicate voting, aggregates results, and periodically displays the live poll results.

This system demonstrates concepts of:

* UDP socket communication
* Client–server architecture
* Packet monitoring using Wireshark
* Duplicate vote detection
* Real-time result aggregation
* 
Features

* UDP based communication
* Real-time voting from multiple clients
* SRN-based voter identification
* Duplicate vote detection
* Live result display
* Packet monitoring using Wireshark
* Lightweight terminal-based interface
  
 Voting System Details

Each student votes using their SRN (Student Registration Number).

Example SRN:
PES2UG25CS829

Structure of SRN:

| Segment | Meaning               |
| ------- | --------------------- |
| PES2UG  | University Prefix     |
| 25      | Year of joining       |
| CS      | Branch code           |
| 829     | Unique student number |

The SRN is used as a **unique voter ID** to prevent duplicate voting.

 Project Architecture

Client Laptop(s)
      |
      | UDP Vote Packet
      |
      v
Server (UDP Socket)
      |
      | Vote Processing
      |
      v
Live Poll Results

Technologies Used

* Python
* UDP Socket Programming
* Wireshark (for packet capture)
* Terminal Interface

How the System Works

Step 1 – Start the Server

Run the server program:
python server.py
The server starts listening for UDP packets on port **5000**.

Step 2 – Run Client Programs

Students run the client program:
python client.py
The client asks for:

* Student SRN
* Vote option

Example voting screen:


------ LIVE POLL ------

Which OS do you prefer?

1. Linux
2. Windows
3. Mac

Enter your SRN:
Enter your vote (1-3):


Step 3 – Vote Packet Transmission

The client sends a UDP packet to the server.

Example packet format:

VOTE|PES2UG25CS829|2

Where:

* `PES2UG25CS829` → Student SRN
* `2` → Selected option

Step 4 – Vote Processing

The server performs the following steps:

1. Receives UDP packet
2. Extracts SRN and vote option
3. Checks for duplicate voters
4. Updates vote count
5. Stores SRN in a voted list

Step 5 – Live Result Display

The server periodically prints live results:


------ LIVE RESULTS ------

Linux : 3
Windows : 5
Mac : 2



Preventing Duplicate Votes

The server maintains a set of voter SRNs.

If the same SRN sends another vote:

```
Duplicate vote ignored from PES2UG25CS829
```

Packet Capture using Wireshark

To observe vote packets:

1. Open Wireshark
2. Select the network interface
3. Apply filter:

```
udp.port == 5000
```

Captured packet example:


VOTE|PES2UG25CS829|2


This confirms that UDP vote packets are transmitted correctly.



License

This project is created for educational purposes.
