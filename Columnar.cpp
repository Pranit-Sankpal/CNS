#include<iostream>
#include <string>
#include <vector>
#include <algorithm>

    std::string encrypt(std::string plaintext, std::string key)
{
    std::vector<int> order(key.size());
    for (int i = 0; i < order.size(); ++i)
    {
        order[i] = i;
    }
    std::sort(order.begin(), order.end(), [&key](int i, int j)
              { return key[i] < key[j]; });

    int rows = (plaintext.size() + key.size() - 1) / key.size();
    std::vector<std::string> grid(rows, std::string(key.size(), ' '));

    for (int i = 0, k = 0; i < rows; ++i)
    {
        for (int j : order)
        {
            if (k < plaintext.size())
            {
                grid[i][j] = plaintext[k++];
            }
            else
            {
                grid[i][j] = '_'; // Pad with underscores if plaintext ends early
            }
        }
    }

    std::string ciphertext;
    for (int j = 0; j < key.size(); ++j)
    {
        for (int i = 0; i < rows; ++i)
        {
            if (grid[i][j] != '_')
            {
                ciphertext += grid[i][j];
            }
        }
    }

    return ciphertext;
}

std::string decrypt(std::string ciphertext, std::string key)
{
    int rows = (ciphertext.size() + key.size() - 1) / key.size();
    int cols = key.size();

    int full_cols = ciphertext.size() / rows;
    int extra_chars = ciphertext.size() % rows;

    std::vector<int> col_order(cols);
    for (int i = 0; i < col_order.size(); ++i)
    {
        col_order[i] = i;
    }
    std::sort(col_order.begin(), col_order.end(), [&key](int i, int j)
              { return key[i] < key[j]; });

    std::vector<int> col_lengths(cols, full_cols);
    for (int i = 0; i < extra_chars; ++i)
    {
        col_lengths[col_order[i]]++;
    }

    std::vector<std::string> grid(rows, std::string(cols, ' '));
    int idx = 0;
    for (int j = 0; j < cols; ++j)
    {
        for (int i = 0; i < col_lengths[j]; ++i)
        {
            grid[i][col_order[j]] = ciphertext[idx++];
        }
    }

    std::string plaintext;
    for (int i = 0; i < rows; ++i)
    {
        for (int j = 0; j < cols; ++j)
        {
            if (grid[i][j] != '_')
            {
                plaintext += grid[i][j];
            }
        }
    }

    return plaintext;
}

int main()
{
    int choice;
    std::string text;
    std::string key;

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

        std::cout << "Enter key: ";
        std::getline(std::cin, key);

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
