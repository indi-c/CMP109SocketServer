import TCP.word_count_socket_code as wcsc
import shared.input_handling as ih
import socket
import typing

# open file
## chose file to open
def open_file() -> typing.TextIO:
    """
    Open the file
    
    Returns:
    file: The file
    """
    # verify the file name
    while True:
        # get the file name
        file_name = input("Enter the file name: ")
        # verify the file exists
        if ih.verify_file(file_name):
            # open the file
            f = open(file_name, "r")
            break
    return f

# read text from file
def read_file(f: typing.TextIO) -> str:
    """
    Read the text from the file
    
    Parameters:
    f (file): The file
    
    Returns:
    str: The text
    """
    # read the text from the file
    text = f.read()
    return text

def split_text(text: str) -> list[str]:
    """
    Split the text into segments 512 bytes long
    
    Parameters:
    text (str): The text
    
    Returns:
    list[str]: The segments
    """
    # split the text into words
    words = text.split()
    # create a list of segments 512 bytes long
    # initialize the segment list
    segments = []
    # initialize the segment
    segment = ""
    # loop through the words
    for word in words:
        # check if adding the word to the segment will make it longer than 512 bytes
        if (len(segment) + len(word) + 1) > 512:
            # add the segment to the list
            segments.append(segment.rstrip())
            # start a new segment with the word
            segment = word + " "
        else:
            # add the word to the segment
            segment += word + " "
    
    # add the last segment to the list if it is not empty
    if segment != "":
        segments.append(segment)
    
    return segments

def loop(host: str, port: int, s: socket.socket):
    """
    The main loop of the program
    
    Parameters:
    host (str): The host
    port (int): The port
    s (socket.socket): The socket
    """
    # open file
    f = open_file()
    # read text from file
    text = read_file(f)
    # split text into segments 512 bytes long
    segments = split_text(text)
    # send segments to server
    word_count = wcsc.send_segments(s, segments, host, port)
    # display result to user
    print("Word Count: " + str(word_count) + '\n')

def setup():
    """
    Setup the program
    """
    # get the host and port
    host, port = ih.get_host_port()
    # create the socket
    s = wcsc.create_socket()
    loop(host, port, s)

def main():
    setup()

if __name__ == "__main__":
    main()