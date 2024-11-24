import socket
import sys
from Crypto.Cipher import AES
import base64

def decrypt_message(key, encrypted_message):
    """
    Decrypts a base64-encoded AES-encrypted message.
    Args:
        key (bytes): The decryption key (must match the client's encryption key).
        encrypted_message (str): The base64-encoded ciphertext to decrypt.
    Returns:
        str: The plaintext message.
    """
    padding = len(encrypted_message) % 4
    if padding != 0:
        encrypted_message += '=' * (4 - padding)
    
    # Decode the message from base64
    encrypted_bytes = base64.b64decode(encrypted_message)
   
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    decrypted_message = decrypted_bytes.decode('utf-8').rstrip()  # Remove padding
    return decrypted_message

# Example usage on the server
AES_KEY = b'16_byte_aes_key!!'[:16]  # 16 bytes


# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = '127.0.0.1'
server_port = 2000

# Bind the server socket to the address and port
try:
    server_socket.bind((server_address, server_port))
    print("Bind Done")
except Exception as e:
    print(f"Bind Failed. Error: {e}")
    sys.exit()

# Listen for incoming connections
try:
    server_socket.listen(1)
    print("Listening for Incoming Connections.....")
except Exception as e:
    print(f"Listening Failed. Error: {e}")
    server_socket.close()
    sys.exit()

while True:
    # Accept a connection from a client
    try:
        client_socket, client_address = server_socket.accept()
        print(f"Client Connected with IP: {client_address[0]} and Port No: {client_address[1]}")
    except Exception as e:
        print(f"Accept Failed. Error: {e}")
        server_socket.close()
        sys.exit()

    # Receive a message from the client
    try:
        encrypted_message = client_socket.recv(1024).decode()
        print(f"Encrypted message received: {encrypted_message}")
        decrypted_message = decrypt_message(AES_KEY, encrypted_message)
        print(f"Decyrpted Client Message: {decrypted_message}")
    except Exception as e:
        print(f"Receive Failed. Error: {e}")
        client_socket.close()
        server_socket.close()
        sys.exit()

    # Process the client message and prepare a response
    #client_id = decrypted_message  # Assuming the last character of the message is the client ID
    server_message = f"Hello I am Server. Your decrypted message is: {decrypted_message}"
    print(server_message)

    # Send the response to the client
    try:
        client_socket.sendall(server_message.encode())
    except Exception as e:
        print(f"Send Failed. Error: {e}")
        client_socket.close()
        server_socket.close()
        exit()

    # Close the client socket after handling the connection
    client_socket.close()

# Close the server socket (optional since it's inside an infinite loop)
server_socket.close()
