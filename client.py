import socket
import sys
from Crypto.Cipher import AES
import base64

# AES encryption function
def encrypt_message(key, message):
    """
    Encrypts a message using AES encryption with ECB mode.
    Args:
        key (bytes): The encryption key (must be 16, 24, or 32 bytes long).
        message (str): The plaintext message to encrypt.
    Returns:
        str: The base64-encoded ciphertext.
    """
    cipher = AES.new(key, AES.MODE_ECB)
    # Pad the message to a multiple of 16 bytes
    padded_message = message + (16 - len(message) % 16) * ' '
    encrypted_bytes = cipher.encrypt(padded_message.encode())
    return base64.b64encode(encrypted_bytes).decode()

# AES key (must be shared between client and server)
AES_KEY = b'16_byte_aes_key!!'[:16]  # 16 bytes'  # Ensure this key is securely shared

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 2000)

# Attempt to connect to the server
try:
    client_socket.connect(server_address)
    print("Connected to the server")
except socket.error as e:
    print(f"Connection Failed. Error: {e}")
    print("Closing Client Connection")
    client_socket.close()
    sys.exit()

# Get a message from the user
client_message = input("Enter Message: ")

encrypted_message = encrypt_message(AES_KEY, client_message)
print(f"Encrypted Message: {encrypted_message}")

# Send the message to the server
try:
    client_socket.sendall(encrypted_message.encode())
    print("Message sent to the server")
except socket.error as e:
    print(f"Send Failed. Error: {e}")
    client_socket.close()
    exit()

# Receive a response from the server
try:
    server_message = client_socket.recv(2000).decode()
    print(f"Server Message: {server_message}")
except socket.error as e:
    print(f"Receive Failed. Error: {e}")
finally:
    # Close the client socket
    client_socket.close()