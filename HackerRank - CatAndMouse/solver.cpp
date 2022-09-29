#include <iostream>

using namespace std;

int main()
{
    int q;
    cin >> q;
    while (q--)
    {
        int x, y, z;
        cin >> x >> y >> z;

        int a = abs(x - z);
        int b = abs(y - z);
        if (a < b)
        {
            cout << "Cat A" << endl;
        }
        else if (a > b)
        {
            cout << "Cat B" << endl;
        }
        else
        {
            cout << "Mouse C" << endl;
        }
    }
    return 0;
}