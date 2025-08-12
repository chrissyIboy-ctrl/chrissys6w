extends Node2D

# ---- Variables and Data Types ----
const DRAG_LAYER_MASK = 1   # Constant for the collision layer to detect cards
var card_being_dragged: Node2D = null
var offset_from_mouse := Vector2.ZERO
var original_position := Vector2.ZERO

func _input(event):
	# Mouse button pressed
	if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT:
		if event.pressed:
			var card = raycast_check_for_card()
			if card:
				card_being_dragged = card
				offset_from_mouse = card.global_position - get_global_mouse_position()
				original_position = card.global_position
				card.rotation_degrees = 5 # ---- Modify node property #1: rotation ----
		else:
			if card_being_dragged:
				card_being_dragged.global_position = original_position # ---- Modify node property #2: position ----
				card_being_dragged.rotation_degrees = 0
				card_being_dragged = null

	# Mouse motion while dragging
	elif event is InputEventMouseMotion and card_being_dragged:
		card_being_dragged.global_position = get_global_mouse_position() + offset_from_mouse

func raycast_check_for_card() -> Node2D:
	var space_state = get_world_2d().direct_space_state
	var params = PhysicsPointQueryParameters2D.new()
	params.position = get_global_mouse_position()
	params.collide_with_areas = true
	params.collision_mask = DRAG_LAYER_MASK # Using our constant

	var result = space_state.intersect_point(params)
	if result.size() > 0:
		var collider = result[0]["collider"]
		return collider.get_parent()
	return null
	
