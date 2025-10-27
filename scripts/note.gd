class_name Note
extends CharacterBody3D

var center = Vector3.ZERO
@onready var audio_stream_player_3d: AudioStreamPlayer3D = $AudioStreamPlayer3D

func setSound(sound : AudioStream):
	audio_stream_player_3d = $AudioStreamPlayer3D
	audio_stream_player_3d.stream = sound;
	audio_stream_player_3d.play()

func _process(_delta: float) -> void:
	move_and_slide()
