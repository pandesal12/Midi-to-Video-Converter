from moviepy.editor import *
import mido

# Load the MIDI file
mf = mido.MidiFile('midi_export.mid')

right = []
left = []

for i, track in enumerate(mf.tracks):
    print(f"Track {i}: {track.name}")

    for message in track:
        if message.type in ["note_on", "note_off"]:
            if i == 1 and message.time != 0: right.append([message.note, message.time])
            elif i==2 and message.time != 0: left.append([message.note, message.time])

# right = right[:-1]

# print(sorted(right))
videos = [VideoFileClip(f"vid/vid ({x}).mp4") for x in range(1, 50)]
results = concatenate_videoclips([videos[x[0]-37].subclip(0, x[1]/1300) for x in right])
results.write_videofile('Final.mp4')