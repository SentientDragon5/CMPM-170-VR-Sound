import mido
import json
import glob, os
import math

lanes_total = 12
data = {
    "notes": []
}

'''
Including this in case we wanna look at other midi "message" types

messageTypes = [
    "MetaMessage", "program_change", "polytouch", 
    "control_change", "aftertouch", "pitchwheel",
    "sysex", "quarter_frame", "songpos", "song_select",
    "tune_request", "clock", "start", "continue", "stop",
    "active_sensing", "reset", "note_off", "note_on"
]
'''
# get songs from ./Songs
songNames = []
os.chdir("./Songs")
for file in glob.glob("*.mid"):
    songName = file.split(".mid")[0]
    songNames.append(songName)

    new_song = mido.MidiFile("./" + songName + ".mid")
    
    os.chdir("../Outputs")
    # make the .json
    with open("./" + songName + ".json", "w") as file:
        max = 0
        for message in new_song:
            msg_list = str(message).split(" ")
            if (msg_list[0] == "note_on"):
                # make new index smaller
                note = {
                    "index" : msg_list[2].split("=")[1],
                    "time" : msg_list[4].split("=")[1]
                }
                data["notes"].append(note)
            
        json.dump(data, file, indent=True)

    '''
    cant use a single lane for each note since notes can go from
    0-127 so find a way to fit that much into however many lanes
    we want
    '''
    # get largest index from notes
    with open('./' + songName + '.json', 'r') as file:
        data = json.load(file)
        max = 0
        for note in data["notes"]:
            if (int(note["index"]) > max):
                max = int(note["index"])
    # make it so every X notes are in the same lane index
    # where X = max/Y
    with open('../Outputs/' + songName + '.json', 'w') as file:
        notes_per_lane = max / lanes_total
        for note in data["notes"]:
            note["index"] = math.floor(int(note["index"])/notes_per_lane)

        json.dump(data, file, indent=True)