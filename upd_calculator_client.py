import shared.input_handling as ih
import UDP.calculator_socket_code as csc
import socket

def cleanup(s: socket.socket):
    """
    Cleanup the program
    
    Parameters:
    s (socket.socket): The socket to close
    """
    print("Closing the connection")
    # close socket
    s.close()
    print("Exiting the program")

def loop(host: str, port: int, s: socket.socket):
    """
    The main loop of the program
    
    Parameters:
    host (str): The host
    port (int): The port
    s (socket.socket): The socket
    """

    try:
        while True:
            # get the input from the user
            data = input("Enter the expression: ")
            if data == "exit":
                break
            try:
                # send the input to the server
                s.sendto(data.encode("ascii", "ignore"), (host, port))
                # receive the result from the server
                result, _ = s.recvfrom(1024)
            except OSError:
                print("Socket error")
                continue
            # display the result to the user
            print("Result: " + result.decode("ascii", "ignore") + '\n')
    # catch the keyboard interrupt exception
    except KeyboardInterrupt:
        print("\nKeyboard interrupt Received\n")
    # cleanup
    finally:
        cleanup(s)

# setup
def setup():
    """
    Setup the program
    """
    host, port = ih.get_host_port()
    s = csc.create_socket()
    loop(host, port, s)

def main():
    setup()

if __name__ == "__main__":
    main()