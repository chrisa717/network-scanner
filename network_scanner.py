import socket

def scan(target_ip, port_range):
    print(f"Scanning target: {target_ip}")
    for port in range(*port_range):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            sock.close()
        except KeyboardInterrupt:
            print("\nScan interrupted.")
            break
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    target = input("Enter IP to scan: ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))
    scan(target, (start_port, end_port + 1))
