extends Node2D

@onready var health_bar = $HealthBar

var max_health = 100
var current_health = 100

func _ready():
	update_health_bar()
	take_damage(25)

func take_damage(amount):
	current_health = max(current_health - amount, 0)
	update_health_bar()
	if current_health <= 0:
		enemy_defeated()

func update_health_bar():
	health_bar.value = current_health

func enemy_defeated():
	print("Enemy defeated!")
	$EnemySprite.hide()
	# Or add a death animation, etc.
