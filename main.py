import turtle
import random

#TURTLES
backgorund_turtle = turtle.Turtle()

text_turtle = turtle.Turtle()

character_turtle = turtle.Turtle()

obstacle_positions = []

obstacle_turtles = []

gravity = -1
velocity = 10

game_window_width = 600
game_window_height = 600

score = 0

game_window = turtle.Screen()

#FUNCTIONS:
def setup_game_window(game_window):
	game_window.onkey(character_jump, "space")
	game_window.register_shape("flappybird.gif")
	game_window.register_shape("PipeDown.gif")
	game_window.register_shape("PipeUp.gif")
	game_window.bgpic("background.gif")
	game_window.screensize()
	game_window.listen()

def draw_borders(selected_turtle, width, height):
	selected_turtle.hideturtle()
	selected_turtle.penup()
	selected_turtle.goto(-width / 2, -height / 2)
	selected_turtle.pendown()
	selected_turtle.goto(width / 2, -height / 2)
	selected_turtle.goto(width / 2, height / 2)
	selected_turtle.goto(-width / 2, height / 2)
	selected_turtle.goto(-width / 2, -height / 2)

def lose_game():
	pass

def generate_obstacle():
	obstacle_turtles.append(make_obstacle(500, random.randint(-200, 200), 300))

	game_window.ontimer(generate_obstacle, 3000)

def make_obstacle(position, hole_position, hole_height):
	top_turtle = turtle.Turtle()
	bottom_turtle = turtle.Turtle()

	top_turtle.penup()
	bottom_turtle.penup()

	set_speed_instant(top_turtle)
	set_speed_instant(bottom_turtle)

	top_turtle.shape("PipeDown.gif")
	bottom_turtle.shape("PipeUp.gif")

	top_turtle.resizemode("user")
	bottom_turtle.resizemode("user")

	top_turtle.shapesize(2, 2)
	bottom_turtle.shapesize(2, 2)

	top_turtle.goto(position, hole_position + 80 + hole_height / 2)
	bottom_turtle.goto(position, hole_position - 80 - hole_height / 2)

	return top_turtle, bottom_turtle

def character_jump():
	global velocity
	velocity = 20

def character_gravity(selected_turtle, velocity):
	selected_turtle.sety(selected_turtle.ycor() + velocity)
	selected_turtle.settiltangle(30)

def change_gravity(velocity, gravity):
	return velocity + gravity

def obstacle_shift(selected_turtle, amount):
	selected_turtle.setx(selected_turtle.xcor() - amount)

def move_obstacles(obstacle_turtles):
	for obstacle_pair in obstacle_turtles:
		for obstacle_turtle in obstacle_pair:
			obstacle_shift(obstacle_turtle, 5)

# def high_scores():
# 	pass

# def write_high_score():
# 	pass

def render():
	global velocity
	move_obstacles(obstacle_turtles)
	velocity = change_gravity(velocity, gravity)
	character_gravity(character_turtle, velocity)
	game_window.ontimer(render, 34)

def set_invisible(selected_turtle):
	selected_turtle.hideturtle()

def remove_obstacle():
	pass

# def print_start_game(selected_turtle):
# 	selected_turtle.hideturtle()
# 	selected_turtle.penup()
# 	selected_turtle.goto(0, 100)
# 	selected_turtle.write("Press Enter to start the game", align = "center", font = ("Arial", "16", "normal"))

def print_score(selected_turtle, score, height):
	selected_turtle.penup()
	selected_turtle.goto(0, -height / 2 - 70)
	selected_turtle.write("Score: {}".format(score), align = "center", font = ("Arial", "24", "bold"))

def set_speed_instant(selected_turtle):
	selected_turtle.speed(0)

#MAIN LOGIC
if __name__ == "__main__":
	setup_game_window(game_window)
	set_speed_instant(backgorund_turtle)
	set_speed_instant(text_turtle)
	set_speed_instant(character_turtle)
	set_invisible(text_turtle)

	draw_borders(backgorund_turtle, game_window_width, game_window_height)
	character_turtle.penup()
	character_turtle.shape("flappybird.gif")
	print_score(text_turtle, score, game_window_height)
	game_window.ontimer(render, 300)
	game_window.ontimer(generate_obstacle, 3000)
	game_window.mainloop()