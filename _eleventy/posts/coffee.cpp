#include <iostream>

int main() {
    bool coffee;
    bool expectations = false;

    std::cin >> coffee;
    while (coffee) {
        if (expectations) {
          std::cout << "Code";
        } else {
          std::cout << "Bug";
        }
        std::cin >> coffee;
    }
    std::cout << "Sleep";

    return 0;
}
