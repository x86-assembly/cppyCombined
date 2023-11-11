using namespace std;

int main() {

std::cout << "Welcome to this game" << std::endl;
int chosen_range;
std::cout << "Up to what number do you want to guess?" << std::endl;
std::cin >> chosen_range;
while (true) {
    int number = 1 + rand() % chosen_range;
    while (true) {
        int guess;
        std::cout << "What number do you guess?" << std::endl;
        std::cin >> guess;
        if (guess == number) {
            std::cout << "You won!" << std::endl;
            break;
        } else if (guess > number) {
            std::cout << "Too large!" << std::endl;
        } else {
            std::cout << "Too small!" << std::endl;
        }
    }
    char play_again;
    std::cout << "Do you want to play again? (y/n)" << std::endl;
    std::cin >> play_again;
    if (play_again == 'n') {
        break;
    }
}
}