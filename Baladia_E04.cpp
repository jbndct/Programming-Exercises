#include <iostream>
#include <string>
using namespace std;

struct Node {
    int n;
    Node* next;
};

struct LinkedList {
    Node* head;
    int list_length;

    LinkedList();
    ~LinkedList();
    void insertion(int n);
    void display();
    void deletion();
    void refresh();
    void search(int n);
};

int main() {
    LinkedList* list = new LinkedList();
    char c;
    int n;
    bool b;
    while (cin >> c >> n) {
        switch (c) {
            case 'i': 
                list -> insertion(n);
                list -> display();
                break;
            case 'd':
            	b = list -> list_length == 0;
                list -> deletion();
                if (!b)
                {
                	list -> display(); }
                break;
            case 'r':
                list -> refresh();
                list -> display();
                break;
            case 's':
				list -> search(n);
                break;
            default:
                cout << "INVALID COMMAND" << endl;
            }
        
        }
    return 0;
}

LinkedList::LinkedList() {
    head = NULL;
    list_length = 0;
}

LinkedList::~LinkedList() {
    refresh();
    cout << "Linked List Deleted!" << endl;
}

void LinkedList::insertion(int n) {
    Node* newnode = new Node();
    newnode->n = n;
    newnode-> next = this -> head;
    this -> head = newnode;
    this -> list_length++;
}

void LinkedList::deletion() {
    if (this -> head == NULL) {cout << "THE LIST IS ALREADY EMPTY" << endl; return; }
    Node* temp = this -> head; 
    this -> head = temp -> next; 
    this -> list_length--; 
    delete temp;
    temp = nullptr;
}

void LinkedList::display() {
    Node* temp = this -> head;
    cout << "[" << this -> list_length << "] ";
    while (temp) {
        cout << temp -> n << " ";
        temp = temp -> next;
        }
    cout << endl;
    }

void LinkedList::refresh() {
    while (head!=NULL) {
        deletion();
        }
    head = NULL;
    } 

void LinkedList::search(int n) {
	Node* temp = this -> head;
	while (temp) {
		if (temp -> n == n) {
			cout << "VALUE FOUND" << endl;
			return;
		}
		temp = temp -> next;
	}
	cout << "VALUE NOT FOUND" << endl; return;
	}