#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main(void){
    std::string input;
    std::string output = "";

    char vowels[6] = {'a', 'e', 'i', 'o', 'u', 'y'};

    std::cin >> input;

    for (char &c : input) {
        c = std::tolower(c);
    }

    for(int i=0; i < input.length(); i++){
        bool isVowel = false;
        for(char vowel : vowels) {
            size_t position = input.substr(i, 1).find(vowel);

            if (position != std::string::npos) {
                isVowel = true;
            }
        }

        if(!isVowel){
            output += "." + std::string(1, tolower(input[i]));
        }
    }

    std::cout << output;
}