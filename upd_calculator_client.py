import udp_input_handling as uih
import calculator_socket_code as csc
import sys
import socket

def cleanup(s: socket.socket):
    print("Closing the connection")
    # close socket
    s.close()
    print("Exiting the program")

def loop(host: str, port: int, s: socket.socket):
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
            print("Result: " + result.decode("ascii", "ignore"))
    # catch the keyboard interrupt exception
    except KeyboardInterrupt:
        print("\nKeyboard interrupt Received\n")
    # cleanup
    finally:
        cleanup(s)

# setup
def setup():
    host, port = uih.get_host_port()
    s = csc.create_socket()
    loop(host, port, s)

def main():
    setup()

if __name__ == "__main__":
    main()