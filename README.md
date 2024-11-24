# AES Encryption with Socket Programming

This project demonstrates how to implement AES encryption and decryption in Python using the PyCryptodome library. The communication between a client and a server is handled using 
TCP sockets. The server always listens for incoming connections, and encrypted messages are exchanged between the client and server.

# Features
- AES(EBC) encryption and decryption.
- Secure data transmission over TCP sockets.
- Simple and easy-to-understand structure.

## Prerequisites
- Python 3.11 or later installed on your system.
- PyCryptodome library for AES encryption.
   
## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/Mamoona-Mahmood/AES-EBC.git

### 2. Install Required Libraries

Install the required Python libraries:

pip install pycryptodome

### 3. Configure Server and Client

Running the Project
# Step 1: Start the Server

Run the server script first to start listening for connections:

python server.py

The server will continuously listen for incoming connections and decrypt received messages.
# Step 2: Start the Client

Run the client script to send encrypted messages to the server:

python client.py

Follow the on-screen prompts to enter a message. The message will be encrypted, sent to the server, and decrypted for display.

### Example Output
# On the Server:
Bind Done
Listening for Incoming Connections.....

Client Connected with IP: 127.0.0.1 and Port No: 54321

Encrypted message received: 1B2M2Y8AsgTpgAmY7PhCfg==9fKeEtCYT3Z4eQsMpUEDSY34u4N2WtA=
Decrypted Client Message: Hello Server! This is Client.
Hello Client! Your decrypted message is: Hello Server! This is Client.


# On the Client:

Connected to the server
Enter Message: Hello Server! This is Client.
Encrypted Message: 1B2M2Y8AsgTpgAmY7PhCfg==9fKeEtCYT3Z4eQsMpUEDSY34u4N2WtA=
Message sent to the server
Server Message: Hello Client! Your decrypted message is: Hello Server! This is Client.
