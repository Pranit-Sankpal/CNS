# Using the numbers as plaintext

from generate_prime import generate_prime_no, is_prime

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

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def gcd(a, h):
	temp = 0
	while(1):
		temp = a % h
		if (temp == 0):
			return h
		a = h
		h = temp

def gen_keys(p, q):
    n = p*q
    phi = (p-1)*(q-1)

    e = 2
    # e must be co-prime to phi and smaller than phi.
    while (e < phi):
        if(gcd(e, phi) == 1):
            break
        else:
            e += 1

    # Private key choosing 'd' such that it satisfies
    # d*e = 1 mod (phi)
    d = mod_inverse(e, phi)

    print(f"Your Public Key is:\ne = {str(e)}\nn = {str(n)}")
    print(f"Your Private Key is:\nd = {str(d)}\nn = {str(n)}")


def encrypt(M, e, n):
    if(len(str(M))) < n:
        # Encryption: C = (M ^ e) % n
        C = findExpoMod(M, e, n)
        return C
    else:
        print("Message size should be less than 'n' !!")

def decrypt(C, d, n): 
    # Decryption: M = (C ^ d) % n
    M = findExpoMod(C, d, n)

    return M

# Main Code
ch = int(input("What do you want to perform?\n1. Generate Public & Private Keys\n2. Encryption\n3. Decryption\n"))

if (ch == 1):
    gen_r = input("Do you want to generate the prime numbers automatically ? [y/n]\n")
    if gen_r == 'y':
        dig_p = int(input("Enter the number of digits in first prime number(p): "))
        p = generate_prime_no(dig_p)
        dig_q = int(input("Enter the number of digits in second prime number(q): "))
        q = generate_prime_no(dig_q)

        print(f"p = {p}")
        print(f"q = {q}")

        gen_keys(p, q)

    elif gen_r == 'n':
        p = int(input("Enter first large prime number(p):\n"))
        if not is_prime(p):
            print(f"Entered number is not prime!")
            exit()
    
        q = int(input("Enter second large prime number(q):\n"))
        if not is_prime(q):
            print(f"Entered number is not prime!")
            exit()

        gen_keys(p, q)

    else:
        print("Invaild choice!")   
        exit()

elif(ch == 2):
    M = int(input("Enter the message to be encrypted:\n"))
    print("Enter the Public Key (e, n):")
    e = int(input("Enter the value of 'e':\n"))
    n = int(input("Enter the value of 'n':\n"))

    C = encrypt(M, e, n)

    print(f"Ciphertext is:\n{str(C)}")

elif(ch == 3):
    C = int(input("Enter the ciphertext to be decrypted:\n"))
    print("Enter the Private Key (d, n):")
    d = int(input("Enter the value of 'd':\n"))
    n = int(input("Enter the value of 'n':\n"))
    M = decrypt(C, d, n)

    print(f"Decrypted message is:\n{str(M)}")

else:
    print("Invalid input!")