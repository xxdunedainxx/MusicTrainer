"""
    IsCompoundInterval
    Ascending vs descending intervals default ascending
"""
from core.data.models.Sound.Note import Note
from core.data.models.Sound.MultiNotes import MultiNotes,NotePolicy
class Interval(MultiNotes):

    def __init__(self,
                 frequency: int, notes: [Note],
                 ascending_or_descending: bool,
                 is_compound_interval: bool =False):
        super().__init__(
            frequency,
            notes,
            NotePolicy(allowedNotes=2,
                       friendlyName="Two notes")
        )
        self._validate_interval(notes)
        self.ascend_or_descend=ascending_or_descending
        self.is_compound=is_compound_interval

    # Custom interval policy
    def _validate_interval(self, notes:[Note])->None:
        if(notes[0].value == notes[0].value):
            raise Exception("interval must be 2 different notes")