from models import Athlete


class Coach:

    def __init__(self):

        self.athlete = Athlete()

    def recommendation(self):

        return {
            "title": "Recovery ride",
            "duration": "60–90 min",
            "power": "170–180 W",
            "reason": "No training data loaded yet."
        }
