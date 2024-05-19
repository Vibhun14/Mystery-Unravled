import random

class DynamicPuzzleGenerator:
    @staticmethod
    def generate_puzzle():
        puzzles = [
            "A complicated lock that requires a unique key.",
            "A riddle that needs to be solved to proceed.",
            "A series of switches that must be flipped in the correct order.",
            "A hidden message revealed by UV light.",
            "A safe that requires a combination to open."
        ]
        return random.choice(puzzles)
