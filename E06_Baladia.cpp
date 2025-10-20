// BALADIA

#include <iostream>
#include <string>
using namespace std;

struct Node {
    int n;
    Node* next;
};

struct Stack {
    Node* top;
    int list_length;

    Stack();
    ~Stack();
    void push(int n);
    void display();
    void pop();
    void refresh();
    void search(int n);
};

int main() {
    int x, y;
    Stack* stack = new Stack();
    
    while (cin >> x >> y) {
        if (y > 1 && y <= 36) {
        while (x!=0) {
            stack -> push (x%y);
            x = x/y;
            }
        stack -> display();
        stack -> refresh(); }
        
        else {
            }
        }
}

    Stack::Stack() {
    top = NULL;
    list_length = 0;
}

Stack::~Stack() {
    refresh();}

void Stack::push(int n) {
    Node* newnode = new Node();
    newnode->n = n;
    newnode-> next = this -> top;
    this -> top = newnode;
    this -> list_length++;
}

void Stack::pop() {
    if (this -> top == NULL) {cout << "THE STACK IS ALREADY EMPTY" << endl; return; }
    Node* temp = this -> top; 
    this -> top = temp -> next; 
    this -> list_length--; 
    delete temp;
    temp = nullptr;
}

void Stack::display() {
    Node* temp = this -> top;
    while (temp) {
        if (temp->n >=10 && temp->n<=35) {
            cout << char('A' + (temp->n - 10));
            }
        else {
        cout << temp -> n;}
        temp = temp -> next;
        }
    cout << endl;
    }

void Stack::refresh() {
    while (top!=NULL) {
        pop();
        }
    top = NULL;
    } 

void Stack::search(int n) {
	Node* temp = this -> top;
	while (temp) {
		if (temp -> n == n) {
			cout << "VALUE FOUND" << endl;
			return;
		}
		temp = temp -> next;
	}
	cout << "VALUE NOT FOUND" << endl; return;
	}

// BALADIA


