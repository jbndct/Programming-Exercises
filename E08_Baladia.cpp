#include <iostream>
#include <string>
#include <sstream>
#include <cctype>

using namespace std;

class Queue {
	string* queue;
	int size, front, rear;

public:
	Queue(int);
	bool isEmpty();
	bool isFull();
	void enqueue(string);
	void dequeue();
	string peek();
	void display();
};


int main()
{
	int N, prio; // number of expressions, priority of person
	string y, command, name; // line catcher, command (arrive or serve), name of person
	cin >> N; // input number of expressions
	cin.ignore(); // ignore null
	Queue vip(N); // queue for vip
	Queue regular(N); // queue for regular

	for (int i = 0; i<N; i++) {
		getline(cin, y); // get whole line 
		stringstream ss(y);
		ss >> command >> prio >> name; // separate line from command, priority, and name

		if (command == "ARRIVE") { // if command is arrive, put person in respective queue
			if (prio == 1) { 
				vip.enqueue(name);
			}
			else if (prio == 2) {
				regular.enqueue(name);
			}
			else {
				cout << "ERROR";
				return -1;
			}

		}
		else if (command == "SERVE") { // if command is serve
			if (!vip.isEmpty()) { // check if vip is empty. if it isn't, dequeue first in vip. if not empty, dequeue in regular.
				vip.dequeue();
				cout << endl;
			}

			else {
				regular.dequeue();
				cout << endl;

			}


		}

		else { // invalid commands
			cout << "ERROR!";
			return -1;
		}
	}
	return 0;

}

Queue::Queue(int s) {
	size = s;
	front = rear = -1;
	queue = new string[s];
}
bool Queue::isEmpty() {
	if (front == -1 && rear == -1) {
		return true;
	}
	else {
		return false;
	}
}
bool Queue::isFull() {
	if (front == (rear+1) % size) {
		return true;
	}
	else {
		return false;
	}
}
void Queue::enqueue(string data) {
	if (isFull()) {
		cout << "The queue is already full." << endl;
		return;
	}
	else {
		if (isEmpty()) {
			front = rear = 0;
		}
		else {
			rear = (rear + 1) % size;
		}
	}
	queue[rear] = data;
}
void Queue::dequeue() {
	if (isEmpty()) {
		cout << "EMPTY";
	}
	else if (front == rear) {
		cout << queue[front];
		front = rear = -1;
	}
	else {
		cout << queue[front];
		front = (front + 1) % size;
	}
}

string Queue::peek() {
	if (isEmpty()) {
		cout << "The queue is empty!" << endl;
		return "";
	}
	return queue[front];
}

void Queue::display() {
	int count = (rear+size-front) % size +1;
	cout << "Queue content: ";
	for (int i=0; i<count; i++) {
		int index = (front + i) % size;
		cout << queue[index] << " - ";
	}

	cout << endl;
}
