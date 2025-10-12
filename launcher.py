import subprocess
import sys
import time

server_scripts = [
    "server1.py",
    "server2.py",
    "server3.py",
    "server4.py",
    "server5.py",
    "server6.py",
]

processes = []

def start_server(script):
    return subprocess.Popen([sys.executable, script])

if __name__ == "__main__":
    print("Starting backend servers...")
    for script in server_scripts:
        p = start_server(script)
        processes.append(p)
        print(f"Started {script}")
        time.sleep(0.5)

    print("All servers started. Press Ctrl+C to terminate.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down servers...")
        for p in processes:
            p.terminate()
        print("All servers terminated.")
