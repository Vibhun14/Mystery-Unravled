import random

class DynamicStoryteller:
    @staticmethod
    def generate_story():
        stories = [
            "An anonymous tip leads you to a crucial piece of evidence.",
            "A witness reports seeing someone suspicious near the scene.",
            "A hidden camera captures the suspect in the act.",
            "A diary entry reveals the suspect's motive.",
            "A phone call provides a critical lead in the investigation."
        ]
        return random.choice(stories)
