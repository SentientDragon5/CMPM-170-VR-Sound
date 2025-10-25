import mido
import json
import glob, os
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
songNames = []
# get songs from ./Songs
os.chdir("./Songs")
for file in glob.glob("*.mid"):
    songName = file.split(".mid")[0]
    songNames.append(songName)

    new_song = mido.MidiFile("./" + songName + ".mid")
    data = {
        "notes": []
    }
    # make the .json
    with open("../Outputs/" + songName + ".json", "w") as file:
        for message in new_song:
            msg_list = str(message).split(" ")
            if (msg_list[0] == "note_on"):
                note = {
                    "index" : msg_list[2].split("=")[1],
                    "time" : msg_list[4].split("=")[1]
                }
                data["notes"].append(note)
            
        json.dump(data, file, indent=True)