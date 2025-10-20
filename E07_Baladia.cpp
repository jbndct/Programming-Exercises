#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

// node, struct, function prototypes
struct Node {
	char x;
	Node* next;
};

class Stack {
	private:
		Node* top;
	public:
		int list_length;
		Stack();
		~Stack();
		void push(char x);
		char pop();
		char peek();
		void display();
		void refresh();
};

struct IntNode {
    int x;
    IntNode* next;
};

class StackInt {
private:
    IntNode* top;
public:
    int list_length;
    StackInt();
    ~StackInt();
    void push(int x);
    int pop();
    int peek();
    void refresh();
};
int precedence(char a); 

// main
int main() {
	Stack* operatorList = new Stack(); // stack for conversion
	StackInt* operandList = new StackInt(); // stack for evaluation
	vector<char> outputList; // vector list for output
	int E;
	string y;
	bool balanced = true; // bool checker if invalid or not
	cin >> E; // user input 
	getline (cin,y); // null catcher from cin
	
	for (int i=0; i<E; i++) { // loop for E number of expressions
		getline (cin,y);
		balanced = true; // resetter to valid
		if (y.length()==0) {
			cout << "INCORRECT MATH EXPRESSION" << endl;
			continue;
		}
		for (int j=0; j < y.length(); j++) { // loop checker of every character in expression
			if (isalnum(y[j])) { // if alphanumeric, put to vector list
				outputList.push_back(y[j]);
			}
			else if (y[j] == '(') { // if opening parenthesis, put to stack
				operatorList -> push(y[j]);
			}
			else if (y[j] == ')') { // if closing parenthesis, pop all operators in stack and put to vector until theres a opening parenthesis
				while (operatorList -> peek() != '(' && operatorList->peek() != '\0') {
					outputList.push_back(operatorList->peek());
					operatorList->pop();
				}
				if (operatorList->peek() == '\0') {  // if no opening parenthesis, just empty, expression is unbalanced
            	balanced = false;
            	break;
        }
				operatorList -> pop();
			}
			else if (y[j] == '*' || y[j] == '/' || y[j] == '-' || y[j] == '+') { // if operators except exponentiation
				while (precedence(operatorList -> peek()) >= precedence(y[j])) { // while precedence of operator in stack is greater than or equal to current operator, pop all operators in stack to the output vector
					outputList.push_back(operatorList->pop());
				}
				operatorList -> push(y[j]); // push current operator to stack after
			}
			else if (y[j] == '^') { // exception for exponentiation
				while (precedence(operatorList -> peek()) > precedence(y[j])) {
					outputList.push_back(operatorList->pop());
				}
				operatorList -> push(y[j]);
			}
			else if (y[j] == ' ') { // if space, ignore
				continue;
			}
		}
		while (operatorList->peek() != '\0') { 
		    if (operatorList->peek() == '(') {//checker for validity for opening parenthesis
		        balanced = false; 
		        operatorList->pop();
		    } 
			else {
		        outputList.push_back(operatorList->pop()); // put rest of operators to vector
		    }
		}
		if (!balanced) { // if unbalanced, output error
			cout << "INCORRECT MATH EXPRESSION";
		}
		else { // if valid, print converted to postfix expression
			for (char c : outputList) {
    		cout << c << " ";
		}
		}
		
		if (balanced) { // for balanced, evaluation part
		    for (char c : outputList) { //check every character from output vector
		        if (isdigit(c)) { // transform char to integer, push to stack
		            operandList->push(c - '0');
		        } else { // get operands for evaluation
		            int b = operandList->pop();
		            int a = operandList->pop();
		            if (a == -1 || b == -1) { // checking for invalid
		                balanced = false;
		                break;
		            }
		            int res = 0; // initialize result to 0
		            switch (c) { // evaluation depending on operator
		                case '+': res = a + b; break;
		                case '-': res = a - b; break;
		                case '*': res = a * b; break;
		                case '/':
		                    if (b == 0) {
		                        balanced = false;
		                    } else {
		                        res = a / b;
		                    }
		                    break;
		                case '^': res = pow(a, b); break;
		            }
		            if (!balanced) break;
		            operandList->push(res); // push result to stack, repeats until done
		        }
		    }
		    if (balanced) { // if balanced, output result
		        int res = operandList->pop();
		        cout << " = " << res;
		    } else { // if not, error
		        cout << "INCORRECT MATH EXPRESSION";
		    }
		}

	// refresh for another line of expression
	cout << endl;
	outputList.clear();
	operatorList->refresh();
	operandList->refresh();

	}
	
	// avoiding memory leak
	delete operatorList;
	delete operandList;
	return 0; }

// function to determine precedence of operator
int precedence(char a) {
	if (a == '^') {return 3;
	}
	else if (a == '*' || a == '/') {return 2;
	}
	else if (a == '+' || a == '-') {return 1;
	}
	return 0;
}

// stack implementations
Stack::Stack() {
    top = NULL;
    list_length = 0;
}

Stack::~Stack() {
    refresh();
}

void Stack::push(char n) {
	Node* newNode = new Node();
	newNode -> x = n;
	newNode -> next = top;
	list_length++;
	top = newNode;
}

char Stack::pop() {
    if (list_length == 0) {
        return '\0';
    }
    Node* temp = top;
    char val = temp->x;
    top = temp->next;
    list_length--;
    delete temp;
    return val;
}

void Stack::display() {
	Node* temp =top;
	while (temp!=NULL) {
		cout << temp-> x;
		temp = temp -> next;
	}
}

void Stack::refresh() {
	while (list_length!=0) {
		this -> pop();
	}
	top = NULL;
}

char Stack::peek(){
	if (list_length == 0) {
        return '\0'; }
	return top->x;
} 

StackInt::StackInt() {
    top = NULL;
    list_length = 0;
}
StackInt::~StackInt() {
    refresh();
}

void StackInt::push(int n) {
    IntNode* newNode = new IntNode();
    newNode->x = n;
    newNode->next = top;
    list_length++;
    top = newNode;
}
int StackInt::pop() {
    if (list_length == 0) {
        return -1;
    }
    IntNode* temp = top;
    int val = temp->x;
    top = temp->next;
    list_length--;
    delete temp;
    return val;
}
int StackInt::peek() {
    if (list_length == 0) {
        return -1;
    }
    return top->x;
}
void StackInt::refresh() {
    while (list_length != 0) {
        pop();
    }
    top = NULL;
}

// BALADIA
