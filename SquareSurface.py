# 1. function enter_side prompts user to key in the side length
# 2. function surface will calculate the surface of the square

def enter_side():
	"""Prompt the user to enter the side of the square"""
	side = int(input("key in the side of the square: "))
	return side


def surface(side_of_square):
	"""With the side, calculate the surface"""
	return side_of_square ** 2


side_value = enter_side()

the_surface = surface(side_value)

print("Since the length is %d, the surface of the square is %d" % (side_value, the_surface))