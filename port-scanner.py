import socket

host = input("Enter a hostname or ipv4 address: ")
ports = []

print("Press Ctrl+C at any time to exit and begin scan.")
try:
    while True:
        try:
            user_input = int(input("Enter a port: "))
            if 1 <= user_input <= 65535:
                ports.append(user_input)
                print(f"Added port {user_input} to list")
            else:
                print("ports must be between 1-65535")
        except ValueError:
            print("Please enter a valid port")
except KeyboardInterrupt:
    print("\nBeginning scan: ")


def port_scanner(host, ports):
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)

            result =  s.connect_ex((host, port))

            if result == 0:
                print(f"port {port} is open.")
            else:
                print(f"port {port} is filtered or closed")

port_scanner(host, ports)