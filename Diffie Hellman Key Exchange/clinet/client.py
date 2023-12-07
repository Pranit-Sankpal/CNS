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

HOST = 'localhost'
PORT = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)  # Server address and port
client_socket.connect(server_address)
print(f"Connected to server at: {HOST}:{PORT}")

# Receive the server's public key, q, alpha
received_Ya = client_socket.recv(1024)
Ya = int(received_Ya.decode())
print(f"Received server's public key as: {Ya}")

received_q = client_socket.recv(1024)
q = int(received_q.decode())
print(f"Received large prime as: {q}")

received_alpha = client_socket.recv(1024)
alpha = int(received_alpha.decode())
print(f"Received alpha as: {alpha}")

# Client's Private Key
Xb = int(input(f"Enter the private key for B (Xb) [less than {q}]:\n"))
if Xb >= q:
    print("Private key must be less than choosen prime!")
    exit()

# Client's Public Key
Yb = findExpoMod(alpha, Xb, q)
print(f"Client's Public key is: {Yb}")

# Send this to Server
print("Sending Client's Public Key to Server...")
send_Yb = str(Yb).encode()
client_socket.sendall(send_Yb)

# Receive Server's Shared key
received_Ks = client_socket.recv(1024)
Ks = int(received_Ks.decode())
print(f"Received Server's Shared key as: {Ks}")

# Compute shared key and send to server
Kc = findExpoMod(Ya, Xb, q)
print(f"Client's Shared key is: {Kc}")

print("Sending it to server...")
send_Kc = str(Kc).encode()
client_socket.sendall(send_Kc)

if Kc == Ks:
    print("Both shared keys are equal\nKeys exchanged successfully!")
else:
    print("Both shared keys aren't equal.\nKey exchange failed!")

client_socket.close()