#include <iostream>

using namespace std;

int main()
{
    int n = 5;
    long int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    long int min = 0;
    for (int i = 0; i < n-1; i++) {
        min += arr[i];
    }

    long int max = 0;
    for (int i = 1; i < n; i++)
    {
        max += arr[i];
    }

    cout << min << " " << max << endl;
}