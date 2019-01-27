from core.data.models.Sound.Sound import Sound
from core.data.models.Sound.Note import Note

class NotePolicy():

    def __init__(self, allowedNotes: int,friendlyName:str):
        self.totalNotes=allowedNotes
        self.name=friendlyName

# Core  class for containing multiple notes
class MultiNotes(Sound):

    def __init__(self,
                 frequency: int,
                 notes: [Note],
                 policy: NotePolicy
                 ):

        super().__init__(frequency)

        # Validate notes passed
        self._policy=policy
        self._validate_notes(notes)
        self.notes=notes


    def _validate_notes(self, notes:[Note])->None:
        if len(notes) != self._policy.totalNotes:
            raise Exception(f"{str(type(self))} require exactly {self._policy.totalNotes} notes. {len(notes)} passed!")

    def friendly_name(self):
        return self._policy.name