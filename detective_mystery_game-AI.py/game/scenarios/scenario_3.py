from game.ai.dynamic_storytelling import DynamicStoryteller

class Scenario3:
    def __init__(self):
        self.suspects = ["the curator", "the security guard", "the art dealer"]
        self.culprit = "the art dealer"
        self.clues = []

    def play(self, game_engine):
        print("Welcome to Scenario 3: The Art Gallery Robbery")
        print("A daring art heist has taken place at the city's renowned art gallery.")
        print("As the lead detective on the case, you arrive at the scene to investigate.")
        print("The gallery is filled with valuable artworks and suspicious characters.")
        print("What will you do next?")
        print("")

    def explore(self):
        clue = DynamicStoryteller.generate_story()
        self.clues.append(clue)
        return clue

    def talk(self):
        print("You question the museum curator about the security measures.")

    def examine(self):
        print("You discover a torn piece of fabric near the crime scene.")

    def check_culprit(self, suspect):
        return suspect == self.culprit
