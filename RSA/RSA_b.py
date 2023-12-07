from generate_prime import generate_prime_no, is_prime

# Function to find mod: a^m mod n


def findExpoMod(a, m, n):
    return pow(a, m, n)


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def gcd(a, h):
    temp = 0
    while (1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp


def gen_keys(p, q):
    n = p*q
    phi = (p-1)*(q-1)

    e = 2
    while (e < phi):
        if (gcd(e, phi) == 1):
            break
        else:
            e += 1

    d = mod_inverse(e, phi)

    print(f"Your Public Key is:\ne = {str(e)}\nn = {str(n)}")
    print(f"Your Private Key is:\nd = {str(d)}\nn = {str(n)}")


def encrypt(message, e, n):
    # Convert alphabetic input to numerical values
    numerical_message = [ord(char) - ord('A') for char in message.upper()]

    # Encryption: C = (M ^ e) % n
    encrypted_message = [findExpoMod(char, e, n) for char in numerical_message]
    return encrypted_message


def decrypt(encrypted_message, d, n):
    # Decryption: M = (C ^ d) % n
    decrypted_numerical_message = [findExpoMod(
        char, d, n) for char in encrypted_message]

    # Convert back to alphabetic characters
    decrypted_message = ''.join(chr(char + ord('A'))
                                for char in decrypted_numerical_message)
    return decrypted_message


# Main Code
ch = int(input("What do you want to perform?\n1. Generate Public & Private Keys\n2. Encryption\n3. Decryption\n"))

if (ch == 1):
    gen_r = input(
        "Do you want to generate the prime numbers automatically ? [y/n]\n")
    if gen_r == 'y':
        dig_p = int(
            input("Enter the number of digits in first prime number(p): "))
        p = generate_prime_no(dig_p)
        dig_q = int(
            input("Enter the number of digits in second prime number(q): "))
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

elif (ch == 2):
    message = input("Enter the message to be encrypted:\n")
    print("Enter the Public Key (e, n):")
    e = int(input("Enter the value of 'e':\n"))
    n = int(input("Enter the value of 'n':\n"))

    encrypted_message = encrypt(message, e, n)
    print(f"Encrypted message is:\n{' '.join(map(str, encrypted_message))}")

elif (ch == 3):
    encrypted_message = list(map(int, input(
        "Enter the list of encrypted values separated by space:\n").split()))
    print("Enter the Private Key (d, n):")
    d = int(input("Enter the value of 'd':\n"))
    n = int(input("Enter the value of 'n':\n"))

    decrypted_message = decrypt(encrypted_message, d, n)

    ans = ""
    for a in decrypted_message:
        if (a < 'A' or a > 'Z'):
            ans += " "
        else:
            ans += a

    print(f"Decrypted message is:\n{ans}")

else:
    print("Invalid input!")
