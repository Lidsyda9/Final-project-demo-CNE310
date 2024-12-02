#Text-Based Adventure Game: Create an interactive game where players make choices to navigate a story.

def start_game():
    print("Welcome to the Interactive Story Game!")
    choice1 = input("You wake up in a mysterious forest. Do you go LEFT towards the river or RIGHT towards the mountains? (left/right): ").lower()
    if choice1 == "left":
        river_path()
    elif choice1 == "right":
        mountain_path()
    else:
        print("Invalid choice. Please choose again.")
        start_game()
def river_path():
    print("You arrive at the river and see a boat.")
    choice2 = input("Do you GET ON the boat or GO BACK? (get on/go back): ").lower()
    if choice2 == "get on":
        print("The boat takes you to an island filled with treasure! You win!")
    elif choice2 == "go back":
        start_game()
    else:
        print("Invalid choice. Please choose again.")
        river_path()
def mountain_path():
    print("You climb the mountain and find a cave.")
    choice2 = input("Do you ENTER the cave or GO BACK? (enter/go back): ").lower()
    if choice2 == "enter":
        print("Inside the cave, you find a sleeping dragon. You quietly exit and live to tell the tale.")
    elif choice2 == "go back":
        start_game()
    else:
        print("Invalid choice. Please choose again.")
        mountain_path()
# Start the game
start_game()