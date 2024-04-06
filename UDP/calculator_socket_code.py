import socket
import sys

def create_socket() -> socket.socket:
    """
    Create a UDP socket
    
    Returns:
    socket.socket: The created socket
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print("Failed to create socket")
        sys.exit()
    return s
