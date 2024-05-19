from game.ai.dynamic_puzzle_generation import DynamicPuzzleGenerator

class Scenario2:
    def __init__(self):
        self.suspects = ["the butler", "the maid", "the gardener"]
        self.culprit = "the butler"
        self.clues = []

    def play(self, game_engine):
        print("Welcome to Scenario 2: The Missing Heirloom")
        print("You've been hired to find a valuable heirloom that has gone missing.")
        print("The search leads you to a grand mansion owned by a wealthy family.")
        print("You enter the mansion's foyer and look around.")
        print("What will you do next?")
        print("")

    def explore(self):
        clue = DynamicPuzzleGenerator.generate_puzzle()
        self.clues.append(clue)
        return clue

    def talk(self):
        print("You overhear the butler discussing recent events.")

    def examine(self):
        print("You notice a suspicious-looking painting on the wall.")

    def check_culprit(self, suspect):
        return suspect == self.culprit
