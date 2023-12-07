#include <iostream>
#include <bits/stdc++.h>

using namespace std;
long long find_multiplicative_inverse(long long a, long long b)
{
    long long q, r, t1 = 0, t2 = 1, t, main_a = a;

    while (b > 0)
    {
        q = a / b;
        r = a % b;
        t = t1 - (t2 * q);

        a = b;
        b = r;
        t1 = t2;
        t2 = t;
    }

    if (t1 < 0)
    {
        t1 += main_a;
    }
    return t1;
}
int main()
{

    cout << "________________________________________________________\n";
    cout << "Chinese Remainder Theorem Problem  \n";
    cout << "________________________________________________________\n";

    cout << "Suppose that equation needs to be in form of X = a (mod m)\n";

    cout << "How many equations you want to perfrom : \t";
    int count;
    cin >> count;
    cout << "\n________________________________________________________\n";
    int M = 1;
    vector<int> a, m;
    for (int i = 0; i < count; i++)
    {
        cout << "Equation No : \t" << i + 1 << endl;
        cout << "Enter a :\t";
        int a_data;
        cin >> a_data;
        cout << "Enter m :\t";
        int m_data;
        cin >> m_data;
        a.push_back(a_data);
        m.push_back(m_data);
        cout << "\n____________________________________________________________________________________\n";
        M = M * m_data;
    }
    cout << "\nValue of M  :\t" << M << endl;
    vector<long long> M_vector, M_inverse_vector;

    for (int i = 0; i < count; i++)
    {
        M_vector.push_back(M / m[i]);
    }

    for (int i = 0; i < count; i++)
    {
        M_inverse_vector.push_back(find_multiplicative_inverse(m[i], M_vector[i]));
    }

    long long sum = 0;
    for (int i = 0; i < count; i++)
    {
        sum += (a[i] * M_vector[i] * M_inverse_vector[i]);
    }
    long long ans = sum % M;
    cout << "\nAfter calculations :\n";
    cout << "______________________________________________________________________________________________\n";
    cout << "|\tEq. No\t|\ta[i]\t|\tm[i]\t|\tM[i]\t|\tM_inverse[i]\t|\n";
    cout << "______________________________________________________________________________________________\n";

    for (int i = 0; i < count; i++)
    {
        cout << "|\t" << i + 1 << "\t|\t" << a[i] << "\t|\t" << m[i] << "\t|\t" << M_vector[i] << "\t|\t" << M_inverse_vector[i] << "\t\t|\n";
        cout << "______________________________________________________________________________________________\n";
    }
    cout << "\nUsing formula X= E (a[i]*m[i]*m^-1[i]) mod M \n";
    cout << "Value of X is approximate equal to  :  " << ans;
    return 0;
}