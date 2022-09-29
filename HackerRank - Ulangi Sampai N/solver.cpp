#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        if (i % 5 == 0) {
            continue;
        } else if (i % 10 == 3) {
            cout << "Nice" << endl;
        } else if (i >= 113) {
            cout << "Error" << endl;
            break;
        } else {
            cout << i << endl;
        }
    }
}