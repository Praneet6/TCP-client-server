import socket
import threading

def handle_client(conn, addr):
    print(f"[+] Connected by {addr}")
    with open("received_file.txt", "wb") as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
    print("[+] File received successfully.")
    conn.close()

def start_server():
    host = '127.0.0.1'  # localhost
    port = 5001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print(f"[*] Server listening on {host}:{port}")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
