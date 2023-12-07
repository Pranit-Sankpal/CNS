#include <iostream>
#include <string>

std::string encrypt(std::string plaintext, int key)
{
    std::string ciphertext = "";
    for (char &ch : plaintext)
    {
        if (isalpha(ch))
        {
            char base = isupper(ch) ? 'A' : 'a';
            ch = ((ch - base + key) % 26) + base;
        }
        ciphertext += ch;
    }
    return ciphertext;
}

std::string decrypt(std::string ciphertext, int key)
{
    return encrypt(ciphertext, 26 - key); // Decryption is essentially encryption with the inverse key
}

int main()
{
    int choice;
    std::string text;
    int key;

    std::cout << "Choose an option:" << std::endl;
    std::cout << "1. Encryption" << std::endl;
    std::cout << "2. Decryption" << std::endl;
    std::cout << "Enter your choice (1 or 2): ";
    std::cin >> choice;
    std::cin.ignore(); // Clear the input buffer

    if (choice == 1 || choice == 2)
    {
        std::cout << "Enter text: ";
        std::getline(std::cin, text);

        std::cout << "Enter key (an integer): ";
        std::cin >> key;

        if (choice == 1)
        {
            std::string encrypted = encrypt(text, key);
            std::cout << "Encrypted text: " << encrypted << std::endl;
        }
        else
        {
            std::string decrypted = decrypt(text, key);
            std::cout << "Decrypted text: " << decrypted << std::endl;
        }
    }
    else
    {
        std::cout << "Invalid choice. Please enter 1 or 2." << std::endl;
    }

    return 0;
}
