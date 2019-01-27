from core.data.models.Sound.Sound import Sound

class Note(Sound):

    def __init__(self, frequency, value):
        super().__init__(frequency)

        self.value=value