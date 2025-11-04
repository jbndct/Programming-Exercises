#include <iostream>
#include <algorithm>
using namespace std;

int interpolationSearch(int array[], int n, int value); // function declaration

int main() {
    int n;
    cin >> n;
    int arr[n];
    
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }
    
    sort(arr, arr+n);
    
    int value;
    cin >> value;

    int index = interpolationSearch(arr, n, value);
    
    if (index!=-1) {
        cout << "Value found at index " << index;
    }
    else {
        cout << "Value not found";
    }
    
    return 0;
}

int interpolationSearch(int array[], int n, int value) {
    int high = n - 1;
    int low = 0;
    int counter = 0;
    
    while (value >= array[low] && value <= array[high] && low<=high) {
        if (array[high] == array[low]) {
            if (array[low] == value)
                return low;
            else
                break;
        }

        int probe = low + (high-low) * (value - array[low]) / (array[high] - array[low]);
        counter++;
        
        if (array[probe]==value) {
            cout << "Number of iterations: " << counter << endl;
            return probe;
        }
        else if (array[probe]>value) {
            high = probe - 1;
        }
        else {
            low = probe + 1;
        }
    }
    
    cout << "Number of iterations: " << counter << endl;
    return -1;
}

