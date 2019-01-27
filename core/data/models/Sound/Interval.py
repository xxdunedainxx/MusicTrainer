"""
    IsCompoundInterval
    Ascending vs descending intervals default ascending
"""
from core.data.models.Sound.Sound import Sound
from core.data.models.Sound.Note import Note
class Interval(Sound):

    def __init__(self,
                 frequency: int, notes: [Note],
                 ascending_or_descending: bool,
                 is_compound_interval: bool =False):
        super().__init__(frequency)

        # Validate notes passed
        self._validate_notes(notes)

        self.ascend_or_descend=ascending_or_descending
        self.is_compound=is_compound_interval

    def _validate_notes(self, notes:[Note])->None:
        if len(notes) != 2:
            raise Exception(f"Intervals require exactly 2 notes. {len(notes)} passed!")

        if(notes[0].value == notes[0].value):
            raise Exception("interval must be 2 different notes")