/*
	Last K Lines: Write a method to print the last K lines of an input file using C++
*/

// use circular array 

#include <fstream>
#include <iostream>
#include <string>

using namespace std;

void printLastKLines (const string filename){
	cout << "Hi, i am a function that will print last K lines from a file!" << endl;
	cout << "Filename: " << filename << endl;

	const int K = 5;
	ifstream file;
	file.open(filename);
	string L[K];
	int size = 0;

	while (file.peek() != EOF){
		getline (file, L[size % K]);
		size++; 
	}

	// compute start of circular array and the size of it
	int start = size > K ? (size % K) : 0;
	int count = min (K, size);

	cout << "start: " << start << " count: " << count << endl; 

	for (int i=0 ; i<count ; i++) {
		cout << L[(start+i) % K] << endl;
	}

}

int main(){
	string filename; 

	cout << "Input filename: "; 
	cin >> filename;

	printLastKLines(filename);

	return 0;
}

