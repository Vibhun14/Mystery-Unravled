from game.ai.dynamic_clue_generation import DynamicClueGenerator

class Scenario1:
    def __init__(self):
        self.suspects = ["mrs. white", "mr. green", "colonel mustard"]
        self.culprit = "mrs. white"
        self.clues = []

    def play(self, game_engine):
        print("Welcome to Scenario 1: The Haunted Manor")
        print("You find yourself standing in front of a mysterious old manor.")
        print("As you enter, the door creaks ominously behind you.")
        print("You are now inside the haunted manor.")
        print("What will you do next?")
        print("")

    def explore(self):
        clue = DynamicClueGenerator.generate_clue()
        self.clues.append(clue)
        return clue

    def talk(self):
        print("You hear strange whispers echoing through the halls.")

    def examine(self):
        print("You see eerie portraits lining the walls.")

    def check_culprit(self, suspect):
        return suspect == self.culprit
