class_name Spawner
extends Node3D

const C_4 = preload("res://chromaticNotes/c4.mp3")
const D_4 = preload("res://chromaticNotes/d4.mp3")
const E_4 = preload("res://chromaticNotes/e4.mp3")
const F_4 = preload("res://chromaticNotes/f4.mp3")
const G_4 = preload("res://chromaticNotes/g4.mp3")
const A_5 = preload("res://chromaticNotes/a5.mp3")
const B_5 = preload("res://chromaticNotes/b5.mp3")
const C_5 = preload("res://chromaticNotes/c-5.mp3")

const NOTE = preload("res://prefabs/note.tscn")

var notes : Array = []
const song_path = "res://Python/Outputs/Super Mario 64 - Medley.json"

@export var radius = 5;
@export var speed = 1;

func get_angle(index : int) -> float:
	var n = len(notes)
	return inverse_lerp(0,n, index)

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	notes = [C_4,D_4,E_4,F_4,G_4,A_5,B_5,C_5,
	C_5,C_5,C_5,C_5,C_5,C_5]
	load_notes_from_json(song_path)

func load_notes_from_json(json_file_path: String) -> void:
	var file = FileAccess.open(json_file_path, FileAccess.READ)
	var json_text = file.get_as_text()
	file.close()
	
	var json = JSON.new()
	var _error = json.parse(json_text)

	var data = json.get_data()
	var notes_array = data["notes"]
	
	for note_data in notes_array:
		var index: int = note_data["index"]
		var time_string: String = note_data["time"]
		
		queueNote(index, time_string.to_float())
	print("Done Queueing")

func queueNote(index: int, time: float) -> void:
	await get_tree().create_timer(time).timeout 
	print("Queueing Note -> Index: %d, Time: %f" % [index, time])
	makeNote(index)

func makeNote(index : int):
	var g : Note = NOTE.instantiate(PackedScene.GEN_EDIT_STATE_INSTANCE)
	await call_deferred("add_child", g)
	g.setSound(notes[index])
	
