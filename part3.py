from midiutil import MIDIFile

def notes_to_midi(notes, filename="output.mid"):
    midi = MIDIFile(1)
    midi.addTempo(0, 0, 120)
    for note in notes:
        midi.addNote(0, 0, note, 0, 1, 100)
    with open(filename, "wb") as f:
        midi.writeFile(f)

# Example usage
generated_notes = [60, 62, 64, 65, 67, 69, 71, 72]  # Sample output from model
notes_to_midi(generated_notes)
