import random

class DynamicClueGenerator:
    @staticmethod
    def generate_clue():
        clues = [
            "A set of footprints leading away from the scene.",
            "A torn piece of fabric matching the suspect's clothing.",
            "A dropped wallet with the suspect's ID.",
            "A mysterious note with a cryptic message.",
            "Fingerprints on the doorknob leading to the crime scene."
        ]
        return random.choice(clues)
