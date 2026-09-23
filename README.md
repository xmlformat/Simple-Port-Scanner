# Python TCP Port Scanner

A simple TCP port scanner written in Python using the built-in `socket` module.

This project was created as a learning exercise to explore Python networking, TCP connections, input validation, exception handling, and the `socket` library.

## Features

- Scan TCP ports on a specified hostname or IPv4 address
- Allow users to specify multiple ports
- Validate port numbers between 1 and 65535
- Handle invalid user input
- Use connection timeouts
- Handle `Ctrl+C` to begin the scan
- No external Python packages required

## Requirements

- Python 3-higher
- Git (only required if cloning the repository)
- No external Python packages are required

## Installation

### Windows

#### 1. Install Python

Download and install Python 3 from:

https://www.python.org/downloads/

During installation, make sure to enable:

```text
Add Python to PATH
```

You can verify that Python was installed correctly by opening Command Prompt or PowerShell and running:

```powershell
python --version
```

You should see a version similar to:

```text
Python 3.13.13
```

#### 2. Clone the repository

Open Command Prompt or PowerShell and run:

```powershell
git clone https://github.com/xcvmsdvksndvskjv/Simple-Port-Scanner
cd Simple-Port-Scanner
```

#### 3. Run the program

```powershell
python port_scanner.py
```

---

### Linux

#### 1. Check for Python 3

Open a terminal and run:

```bash
python3 --version
```

If Python 3 is not installed, Debian/Ubuntu-based distributions can install it with:

```bash
sudo apt update
sudo apt install python3 git
```

#### 2. Clone the repository

```bash
git clone https://github.com/xcvmsdvksndvskjv/Simple-Port-Scanner
cd python-port-scanner
```

#### 3. Run the program

```bash
python3 port_scanner.py
```

## Usage

After starting the program, enter the hostname or IPv4 address you want to scan:

```text
Enter a hostname or ipv4 address: example.com
```

The program will then ask you to enter ports individually:

```text
Press Ctrl+C at any time to exit and begin scan.
Enter a port: 80
Added port 80 to list
Enter a port: 443
Added port 443 to list
Enter a port: 22
Added port 22 to list
```

When you have finished entering ports, press:

```text
Ctrl+C
```

The program will then begin scanning the ports that were entered.

## Example

An example scan may look like:

```text
Enter a hostname or ipv4 address: example.com
Press Ctrl+C at any time to exit and begin scan.
Enter a port: 80
Added port 80 to list
Enter a port: 443
Added port 443 to list
Enter a port: 22
Added port 22 to list
^C

Beginning scan:

Port 80 is open.
Port 443 is open.
Port 22 is closed or unreachable.
```

The exact results will depend on the host and network being scanned.

## How It Works

The program uses Python's built-in `socket` module to attempt TCP connections to the ports provided by the user.

### 1. Creating a Socket

The scanner creates an IPv4 TCP socket:

```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

`AF_INET` specifies IPv4, while `SOCK_STREAM` specifies a TCP connection.

### 2. Setting a Timeout

The scanner uses:

```python
s.settimeout(1)
```

This prevents the program from waiting indefinitely for a connection attempt.

### 3. Attempting a Connection

The program uses:

```python
s.connect_ex((host, port))
```

`connect_ex()` attempts to establish a connection to the specified host and port.

A return value of `0` indicates that the connection was successful:

```python
if result == 0:
    print(f"Port {port} is open.")
```

A non-zero result indicates that the connection was unsuccessful.

The current version reports these ports as:

```text
closed or unreachable
```

The program does not attempt to distinguish between every possible reason for a failed connection.

## Input Validation

The program checks that port numbers are within the valid port range:

```text
1 - 65535
```

For example:

```text
Enter a port: 70000
Port must be between 1-65535.
```

It also handles non-numeric input using ValueError:

```text
Enter a port: hello
Please enter a valid port.
```



## Disclaimer

This project is intended for educational purposes and authorized security testing.

Only scan systems that you own or have explicit permission to test.

I am  not responsible for any misuse of this software, don't be a naughty boy or girl
