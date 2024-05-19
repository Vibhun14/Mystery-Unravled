import random
from game.scenarios import scenario_1, scenario_2, scenario_3
from game.ai.sentiment_analysis import SentimentAnalyzer

class GameEngine:
    def __init__(self):
        self.current_scenario = None
        self.scenarios = {
            '1': scenario_1.Scenario1(),
            '2': scenario_2.Scenario2(),
            '3': scenario_3.Scenario3()
        }
        self.inventory = []
        self.clues = []

    def start(self):
        print("Welcome to the Detective Mystery Game with AI!")
        self.display_scenario_menu()
        scenario_num = input("Enter the scenario number (1, 2, or 3): ")
        while scenario_num not in self.scenarios:
            print("Invalid scenario number. Please choose 1, 2, or 3.")
            self.display_scenario_menu()
            scenario_num = input("Enter the scenario number (1, 2, or 3): ")
        self.current_scenario = self.scenarios[scenario_num]
        self.current_scenario.play(self)
        self.play()

    def display_scenario_menu(self):
        print("Choose a scenario to begin:")
        print("1. The Haunted Manor")
        print("2. The Missing Heirloom")
        print("3. The Art Gallery Robbery")

    def add_clue(self, clue):
        self.clues.append(clue)
        print(f"Clue added: {clue}")

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Your inventory contains:")
            for item in self.inventory:
                print(f"- {item}")

    def show_clues(self):
        if not self.clues:
            print("You haven't found any clues yet.")
        else:
            print("You have collected the following clues:")
            for clue in self.clues:
                print(f"- {clue}")

    def accuse(self):
        if not self.clues:
            print("You don't have enough clues to make an accusation.")
            return

        print("Who do you accuse?")
        print("Possible suspects:")
        for suspect in self.current_scenario.suspects:
            print(f"- {suspect.capitalize()}")
        suspect = input("Enter the name of the suspect: ").strip().lower()
        result = self.current_scenario.check_culprit(suspect)
        if result:
            print("Congratulations! You've solved the mystery and caught the culprit!")
        else:
            print("Sorry, that's not the right suspect. Keep investigating.")
    
    def get_command(self):
        command = input("Enter your command (explore, talk, examine, inventory, clues, accuse, quit): ").lower()
        if command == "explore":
            clue = self.current_scenario.explore()
            self.add_clue(clue)
        elif command == "talk":
            self.current_scenario.talk()
        elif command == "examine":
            self.current_scenario.examine()
        elif command == "inventory":
            self.show_inventory()
        elif command == "clues":
            self.show_clues()
        elif command == "accuse":
            self.accuse()
        elif command == "quit":
            print("Exiting the game. Goodbye!")
            return False
        else:
            print("Invalid command. Please try again.")
        return True

    def play(self):
        while self.get_command():
            pass
