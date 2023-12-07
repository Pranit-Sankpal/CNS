#include <iostream>
#include <string>
#include<vector>

std::string encryptRailFence(std::string plaintext, int rails)
{
    std::string ciphertext;
    std::vector<std::string> fence(rails);

    int row = 0;
    bool down = false;

    for (char ch : plaintext)
    {
        fence[row] += ch;

        if (row == 0 || row == rails - 1)
        {
            down = !down;
        }

        row += down ? 1 : -1;
    }

    for (const std::string &str : fence)
    {
        ciphertext += str;
    }

    return ciphertext;
}

std::string decryptRailFence(std::string ciphertext, int rails)
{
    std::string plaintext(ciphertext.length(), ' ');
    std::vector<int> pos(ciphertext.length());
    int idx = 0;
    int row = 0;
    bool down = false;

    for (int i = 0; i < ciphertext.length(); ++i)
    {
        pos[i] = row;

        if (row == 0 || row == rails - 1)
        {
            down = !down;
        }

        row += down ? 1 : -1;
    }

    for (int i = 0; i < rails; ++i)
    {
        for (int j = 0; j < ciphertext.length(); ++j)
        {
            if (pos[j] == i)
            {
                plaintext[j] = ciphertext[idx++];
            }
        }
    }

    return plaintext;
}

int main()
{
    int choice;
    std::string text;
    int rails;

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

        std::cout << "Enter number of rails: ";
        std::cin >> rails;

        if (choice == 1)
        {
            std::string encrypted = encryptRailFence(text, rails);
            std::cout << "Encrypted text: " << encrypted << std::endl;
        }
        else
        {
            std::string decrypted = decryptRailFence(text, rails);
            std::cout << "Decrypted text: " << decrypted << std::endl;
        }
    }
    else
    {
        std::cout << "Invalid choice. Please enter 1 or 2." << std::endl;
    }

    return 0;
}
