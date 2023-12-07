from generate_prime import is_prime, generate_prime_no
import socket

# Function to find mod: a^m mod n
def findExpoMod(a, m, n):
    # Decimal to binary conversion
    m_bin = bin(m).replace("0b", "")

    # Convert it into list (individual characters)
    m_bin_lst = [int(i) for i in m_bin]

    # Initialize the list
    a_lst = [a]
    
    # Functions to perform operations
    # If next value = 0
    def oneOperation(num):
        return (num*num) % n

    # If next value = 1
    def twoOperation(num):
        return (a * oneOperation(num)) % n
        
    for j in range(len(m_bin_lst)):
        if j+1 == len(m_bin_lst):
            break

        if(m_bin_lst[j+1] == 0):
            a_lst.append(oneOperation(a_lst[j]))
        else:
            a_lst.append(twoOperation(a_lst[j]))

    return a_lst[-1]

def is_primitive_root(alpha, q):
    L = []

    for i in range(1, q):
        L.append(findExpoMod(alpha, i, q))

    for i in range(1, q):
        if L.count(i) > 1:
            L.clear()
            return False
            
        return True

# Initialize Socket
HOST = 'localhost'
PORT = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)  # Server address and port
server_socket.bind(server_address)
server_socket.listen(1)
print(f"Server started at: {HOST}:{PORT}")

print("Waiting for a client to connect...")
client_socket, client_address = server_socket.accept()
print("Client connected: ", client_address)

# DH Key-exchange
# Choose prime no. 'q'
print("Choose a large integer prime number(q):")
gen_r = input("Do you want to generate the prime number automatically ? [y/n]\n")
if gen_r == 'y':
    dig_p = int(input("Enter the number of digits in prime number: "))
    q = generate_prime_no(dig_p)
    print(f"q = {q}")
elif gen_r == 'n':
    q = int(input("Enter a large prime number:\n"))
    if not is_prime(q):
        print(f"Entered number is not prime!")
        exit()
else:
    print("Invaild choice!")   
    exit()

# Choose primitive root 'alpha'
print("Choose primitive root (alpha):")
gen_pr = input("Do you want to find the primitive root automatically ? [y/n]\n")
if gen_pr == 'y':
    for a in range(2, q):
        if is_primitive_root(a, q):
            alpha = a
            break
    print(f"Alpha = {alpha}")
elif gen_pr == 'n':
    alpha = int(input(f"Enter the primiitive root of {q}:\n"))
    if not is_primitive_root(alpha, q):
        print(f"This is not the primitive root!")
        exit()
else:
    print("Invaild choice!")   
    exit()

# Server's Private key
Xa = int(input(f"Enter the private key for A (Xa) [less than {q}]:\n"))
if Xa >= q:
    print("Private key must be less than choosen prime!")
    exit()

# Server's Public Key
Ya = findExpoMod(alpha, Xa, q)

# Send this data to client
print(f"Server's Public Key is: {Ya}")
print("Sending Public Key to client...")
send_Ya = str(Ya).encode()
client_socket.sendall(send_Ya)

print("Sending choosen large prime to client...")
send_q = str(q).encode()
client_socket.sendall(send_q)

print("Sending primitive root to client...")
send_alpha = str(alpha).encode()
client_socket.sendall(send_alpha)

print("Waiting for Client's Public Key...")

# Receive Client's Public Key
received_Yb = client_socket.recv(1024)
Yb = int(received_Yb.decode())
print(f"Received Public Key of Client: {Yb}")

# Compute shared key and send to client
Ks = findExpoMod(Yb, Xa, q)
print(f"Server's Shared Key is: {Ks}")

print("Sending it to client...")
send_Ks = str(Ks).encode()
client_socket.sendall(send_Ks)

# Receive Client's Shared Key
print("Waiting for Client's Shared Key...")
received_Kc = client_socket.recv(1024)
Kc = int(received_Kc.decode())
print(f"Received Client's Shared Key as: {Kc}")

if Ks == Kc:
    print("Both shared keys are equal\nKeys exchanged successfully!")
else:
    print("Both shared keys aren't equal.\nKey exchange failed!")

client_socket.close()
server_socket.close()