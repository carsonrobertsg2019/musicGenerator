import random
from midiutil import MIDIFile

scales = [ 
    [60, 62, 64, 66, 67, 69, 71, 72], #Lydian
    [60, 62, 64, 65, 67, 69, 71, 72], #Major/Ionian
    [60, 62, 64, 65, 67, 69, 70, 72], #Mixolydian
    [60, 62, 63, 65, 67, 69, 70, 72], #Dorian
    [60, 62, 63, 65, 67, 68, 70, 72], #Minor/Aeolian
    [60, 61, 63, 65, 67, 68, 70, 72], #Phrygian
    [60, 61, 63, 64, 67, 68, 70, 72], #Locrian
]
wholeNote = 4
numNotes = 128

for i in range(len(scales)):
    chosenScale = scales[i]
    degrees = [random.choice(chosenScale) for i in range(numNotes)]
    degrees[0] = chosenScale[0]
    degrees[numNotes - 1] = chosenScale[7]

    track    = 0
    channel  = 0
    time     = 0    # In beats

    durations = [wholeNote/(0.5*2**(random.randint(2, 4))) for i in range(numNotes)]

    tempo    = 80   # In BPM
    volume   = 100  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(numTracks=1)  # One track, defaults to format 1 (tempo track is created automatically)
    MyMIDI.addTempo(track, time, tempo)

    totalTime = 0

    for j in range(numNotes):
        MyMIDI.addNote(track, channel, degrees[j], totalTime, durations[j], volume)
        totalTime += durations[j]
    
    str_i = str(i)
    with open("file" + str_i + ".mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)