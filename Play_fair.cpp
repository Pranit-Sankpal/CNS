#include <iostream>
#include <string>
#include <vector>
#include <cctype>

// Function to prepare the key for Playfair cipher
std::string prepareKey(std::string key)
{
    std::string preparedKey = "";
    std::vector<bool> visited(26, false);

    // Append the key
    for (char ch : key)
    {
        if (isalpha(ch) && !visited[tolower(ch) - 'a'])
        {
            visited[tolower(ch) - 'a'] = true;
            preparedKey += tolower(ch);
        }
    }

    // Append the remaining alphabet characters
    for (char ch = 'a'; ch <= 'z'; ++ch)
    {
        if (ch != 'j' && !visited[ch - 'a'])
        {
            preparedKey += ch;
        }
    }

    return preparedKey;
}

// Function to generate the Playfair cipher matrix
std::vector<std::vector<char>> generateMatrix(std::string key)
{
    std::vector<std::vector<char>> matrix(5, std::vector<char>(5));

    key = prepareKey(key);

    int idx = 0;
    for (int i = 0; i < 5; ++i)
    {
        for (int j = 0; j < 5; ++j)
        {
            matrix[i][j] = key[idx++];
        }
    }

    return matrix;
}

// Function to find the position of a character in the matrix
void findPosition(std::vector<std::vector<char>> &matrix, char ch, int &row, int &col)
{
    if (ch == 'j')
        ch = 'i';
    for (int i = 0; i < 5; ++i)
    {
        for (int j = 0; j < 5; ++j)
        {
            if (matrix[i][j] == ch)
            {
                row = i;
                col = j;
                return;
            }
        }
    }
}

// Function to encrypt using the Playfair cipher
std::string encryptPlayfair(std::string plaintext, std::string key)
{
    std::vector<std::vector<char>> matrix = generateMatrix(key);

    std::string encryptedText = "";
    for (int i = 0; i < plaintext.length(); i += 2)
    {
        int row1, col1, row2, col2;
        findPosition(matrix, tolower(plaintext[i]), row1, col1);
        findPosition(matrix, tolower(plaintext[i + 1]), row2, col2);

        if (row1 == row2)
        {
            encryptedText += matrix[row1][(col1 + 1) % 5];
            encryptedText += matrix[row2][(col2 + 1) % 5];
        }
        else if (col1 == col2)
        {
            encryptedText += matrix[(row1 + 1) % 5][col1];
            encryptedText += matrix[(row2 + 1) % 5][col2];
        }
        else
        {
            encryptedText += matrix[row1][col2];
            encryptedText += matrix[row2][col1];
        }
    }

    return encryptedText;
}

// Function to decrypt using the Playfair cipher
std::string decryptPlayfair(std::string ciphertext, std::string key)
{
    std::vector<std::vector<char>> matrix = generateMatrix(key);

    std::string decryptedText = "";
    for (int i = 0; i < ciphertext.length(); i += 2)
    {
        int row1, col1, row2, col2;
        findPosition(matrix, tolower(ciphertext[i]), row1, col1);
        findPosition(matrix, tolower(ciphertext[i + 1]), row2, col2);

        if (row1 == row2)
        {
            decryptedText += matrix[row1][(col1 + 4) % 5];
            decryptedText += matrix[row2][(col2 + 4) % 5];
        }
        else if (col1 == col2)
        {
            decryptedText += matrix[(row1 + 4) % 5][col1];
            decryptedText += matrix[(row2 + 4) % 5][col2];
        }
        else
        {
            decryptedText += matrix[row1][col2];
            decryptedText += matrix[row2][col1];
        }
    }

    return decryptedText;
}

int main()
{
    int choice;
    std::string text, key;

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
            std::string encrypted = encryptPlayfair(text, key);
            std::cout << "Encrypted text: " << encrypted << std::endl;
        }
        else
        {
            std::string decrypted = decryptPlayfair(text, key);
            std::cout << "Decrypted text: " << decrypted << std::endl;
        }
    }
    else
    {
        std::cout << "Invalid choice. Please enter 1 or 2." << std::endl;
    }

    return 0;
}
