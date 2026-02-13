import socket
import threading

def send_file():
    host = '127.0.0.1'  # same machine
    port = 5001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    filename = "text.txt"  # Ensure this file exists in same folder
    with open(filename, "rb") as f:
        print("[*] Sending file...")
        data = f.read(1024)
        while data:
            s.send(data)
            data = f.read(1024)
    s.close()
    print("[+] File sent successfully!")

if __name__ == "__main__":
    t = threading.Thread(target=send_file)
    t.start()
    t.join()
