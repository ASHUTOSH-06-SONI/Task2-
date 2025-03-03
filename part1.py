#code for midi processing

import pretty_midi
import numpy as np

def midi_to_notes(midi_file):
    pm = pretty_midi.PrettyMIDI(midi_file)
    notes = []
    for instrument in pm.instruments:
        if not instrument.is_drum:
            for note in instrument.notes:
                notes.append([note.start, note.end, note.pitch, note.velocity])
    return np.array(notes)

# Example usage
notes = midi_to_notes("example.mid")
