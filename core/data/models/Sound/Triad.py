"""
type of chord -- major. minor, diminished augmented

TODO :: function to randomly determine if note / interval or triad
TODO :: funciton to generate note, interval, triad
interval -- ascending or descending, range?, no duplicate notes
triad / chord -- quality (major / minor / dminished / augmented), inversions root vs 2nd inversion etc, 3 notes, no chord extensions for now (7th, 10th etc), root

"""
from core.data.models.Sound.Note import Note
from core.data.models.Sound.MultiNotes import MultiNotes,NotePolicy
class Triad(MultiNotes):

    def __init__(self,
                 frequency: int,
                 notes: [Note],
                 chordType: str,
                 is_inversion: bool=False,
                 inversion_type: str = "N/A"
                 ):
        super().__init__(
            frequency,
            notes,
            NotePolicy(allowedNotes=3,
                       friendlyName="chord"),

        )

        self.notes=notes
        self.chord_type=chordType
        self.is_inversion=is_inversion
        self.inversion=inversion_type