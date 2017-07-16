import turtle

#TURTLES
backgorund_turtle = turtle.Turtle()

text_turtle = turtle.Turtle()

character_turtle = turtle.Turtle()

obstacle_turtles = []

gravity = -5
last_jump = 0

game_window = turtle.Screen()


#FUNCTIONS:
def draw_background(selected_turtle, witdth, height):
	set_speed_instant(selected_turtle)
	selected_turtle.penup()
	selected_turtle.goto(-witdth / 2, -height / 2)
	selected_turtle.pendown()
	selected_turtle.goto(witdth / 2, -height / 2)
	selected_turtle.goto(witdth / 2, height / 2)
	selected_turtle.goto(-witdth / 2, height / 2)
	selected_turtle.goto(-witdth / 2, -height / 2)

def lose_game():

def generate_obstacle():

def character_jump():

def character_gravity(selected_turtle):
	selected_turtle.sety(selected_turtle.ycor() - gravity * last_jump)
	last_jump *= 10 / 9.81

def frame():

def obstacle_shift():

def high_scores():

def clear_terminal():

def write_high_score():

def remove_obstacle():

def make_obstacle():

def print_start_game():

def print_score():

def set_speed_instant(selected_turtle):
	selected_turtle.speed(0)

#MAIN LOGIC
if __name__ == "__main__":
	draw_background(backgorund_turtle, 400, 250)