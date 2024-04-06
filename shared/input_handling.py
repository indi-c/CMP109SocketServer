import re

# verify the port number
def verify_port(port: str) -> bool:
    """
    Verify the port number

    Parameters:
    port (str): The port number to verify

    Returns:
    bool: True if the port number is valid, False otherwise
    """
    # check if the port number is a number
    try:
        port = int(port)
    # if not a number, print error message and return False
    except ValueError:
        print("Invalid port number\n")
        return False
    
    # check if the port number is within the valid range 0-65535
    # if not, print error message and return False
    if port < 0 or port > 65535:
        print("Invalid port number\n")
        return False
    # return True if the port number is valid
    return True

# verify the selected host
def verify_host(host: str) -> bool:
    """
    Verify the host
    
    Parameters:
    host (str): The host to verify
    
    Returns:
    bool: True if the host is valid, False otherwise
    """
    # check if the host matches the IP address pattern
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", host):
        print("Invalid host\n")
        return False
    
    # split the host into octets
    octets = host.split(".")
    for octet in octets:
        # check if the octet is a number
        try:
            octet = int(octet)
        # if not a number, print error message and return False
        except ValueError:
            print("Invalid host\n")
            return False
        # check if the octet is within the valid range 0-255
        # if not, print error message and return False
        if octet < 0 or octet > 255:
            print("Invalid host\n")
            return False
        
    # return True if the host is valid
    return True

def get_host_port() -> tuple[str, int]:
    """
    Get the host and port from the user

    Returns:
    tuple[str, int]: The host and port
    """
    while True:
        host = input("Enter the host: ")
        if verify_host(host):
            break
    while True:
        port = input("Enter the port: ")
        if verify_port(port):
            break
    return host, int(port)

# verify the selected file
def verify_file(file_name: str) -> bool:
    """
    Verify the file
    
    Parameters:
    file_name (str): The file to verify
    
    Returns:
    bool: True if the file is valid, False otherwise
    """
    try:
        # open the file
        f = open(file_name, "r")
        f.close()
    except FileNotFoundError:
        print("File not found")
        return False
    return True