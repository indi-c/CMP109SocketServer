import socket

def create_socket() -> socket.socket:
    """
    Create the socket
    
    Returns:
    socket: The socket
    """
    # create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return s

def send_segment(s: socket.socket, segment: str):
    """
    Send the text to the server
    
    Parameters:
    s (socket.socket): The socket
    text (str): The text
    """
    # send the text to the server
    s.sendall(segment.encode("ascii", "ignore"))

def receive_result(s: socket.socket) -> str:
    """
    Receive the result from the server
    
    Parameters:
    s (socket.socket): The socket
    
    Returns:
    str: The result
    """
    # receive the result from the server
    result = s.recv(1024)
    return result.decode("ascii", "ignore")

def send_segments(s: socket.socket, segments: list[str], host: str, port: int) -> int:
    """
    Send the text to the server
    
    Parameters:
    s (socket.socket): The socket
    segments (list[str]): The segments

    Returns:
    int: The word count
    """
    s.connect((host, port))
    # send text to server
    # initialise word count
    word_count = 0
    for segment in segments:
        # send the segment to the server
        send_segment(s, segment)
        # receive result from server
        try:
            result = receive_result(s)
            word_count += int(result)
        except ValueError:
            print("Error receiving result")
            print("result: " + result + '\n')
            s.close()
    s.close()
    return word_count