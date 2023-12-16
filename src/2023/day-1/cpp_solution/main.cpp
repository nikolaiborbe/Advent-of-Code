#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int get_numbers(const string &line) 
{
    char char_first_digit = '\0';
    char char_last_digit = '\0';

    for (char ch : line) {
        if (isdigit(ch)) {
            if (char_first_digit == '\0') {
                char_first_digit = ch;
            }
            char_last_digit = ch;
        }  
    }    

    int first_digit = char_first_digit - '0';
    int last_digit = char_last_digit - '0';

    int number = (first_digit*10) + last_digit;

    return number;
}




int main()
{
    int sum{};
    string line;
    ifstream file ("input.txt");

    if (file.is_open()) {
        while (getline(file, line)) {
            sum += get_numbers(line);
        }
    }
    file.close();

    cout << sum << '\n';
    
    return 0;
}