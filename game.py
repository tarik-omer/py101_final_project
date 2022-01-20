import pygame
import sys

pygame.init()

# background image
width = 600
height = 800
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# background image
background = pygame.image.load("assets/bgd.jpg")

# text color
black = (0, 0, 0)

# brick colors
brick_type = [
			(120, 40, 31), (148, 49, 38), (176, 58, 46),
			(203, 67, 53), (231, 76, 60), (236, 112, 99),
			(241, 148, 138), (245, 183, 177), (250, 219, 216),
			(253, 237, 236), (254, 249, 231), (252, 243, 207),
			(249, 231, 159), (247, 220, 111), (244, 208, 63),
			(241, 196, 15), (212, 172, 13), (183, 149, 11),
			(154, 125, 10), (125, 102, 8), (126, 81, 9),
			(156, 100, 12), (185, 119, 14), (202, 111, 30),
			(214, 137, 16), (243, 156, 18), (245, 176, 65),
			(248, 196, 113),(250, 215, 160), (253, 235, 208),
			(254, 245, 231), (232, 246, 243), (162, 217, 206),
			(162, 217, 206), (115, 198, 182), (69, 179, 157),
			(22, 160, 133), (19, 141, 117), (17, 122, 101),
			(14, 102, 85), (11, 83, 69), (21, 67, 96), 
			(26, 82, 118), (31, 97, 141), (36, 113, 163),
			(41, 128, 185), (84, 153, 199), (127, 179, 213), 
			(169, 204, 227), (212, 230, 241), (234, 242, 248),
			(251, 238, 230), (246, 221, 204), (237, 187, 153),
			(229, 152, 102), (220, 118, 51), (211, 84, 0),
			(186, 74, 0), (160, 64, 0), (135, 54, 0), (110, 44, 0)
			]

brick_index = 0
brick_height = 20
brick_width = 120

score = 0
speed = 3

# single brick
class brick:
	def __init__(self, x, y, brick_type, speed):
		self.x = x
		self.y = y
		self.w = brick_width
		self.h = brick_height
		self.brick_type = brick_type
		self.speed = speed

	def draw(self):
		pygame.draw.rect(display, self.brick_type, (self.x, self.y, self.w, self.h))

	def move(self):
		self.x += self.speed
		if self.x > width:
			self.speed *= -1
		if self.x + self.w < 1:
			self.speed *= -1

# complete stack
class Stack:
	def __init__(self):
		global brick_index
		self.stack = []
		self.first_stack = 10
		for i in range(self.first_stack):
			new_brick = brick(width / 2 - brick_width / 2, height - (i + 1) * brick_height, brick_type[brick_index], 0)
			brick_index += 1
			self.stack.append(new_brick)

    # display all bricks on the stack
	def show(self):
		for i in range(self.first_stack):
			self.stack[i].draw()

    # whenever a brick is placed, move() will be called to move all the bricks down 1 level
	def move(self):
		for i in range(self.first_stack):
			self.stack[i].move()

    # function to add a new brick to the stack
	def addnew_brick(self):
		global brick_index, speed
		# reset the brick index
		if brick_index >= len(brick_type):
			brick_index = 0
		
		y = self.peek().y
		if score > 50:
			speed += 0
		elif score % 5 == 0:
			speed += 1
		
		new_brick = brick(width, y - brick_height, brick_type[brick_index], speed)
		brick_index += 1
		self.first_stack += 1
		self.stack.append(new_brick)

	def peek(self):
		return self.stack[self.first_stack - 1]

	def push_to_stack(self):
		global brick_width, score
		b = self.stack[self.first_stack - 2]
		b2 = self.stack[self.first_stack - 1]
		# check whether the player succesfuly pushed a new brick to the stack
		if b2.x <= b.x and not (b2.x + b2.w < b.x):
			self.stack[self.first_stack - 1].w = self.stack[self.first_stack - 1].x + self.stack[self.first_stack - 1].w - b.x
			self.stack[self.first_stack - 1].x = b.x
			if self.stack[self.first_stack - 1].w > b.w:
				self.stack[self.first_stack - 1].w = b.w
			self.stack[self.first_stack - 1].speed = 0
			score += 1

		elif b.x <= b2.x <= b.x + b.w:
			self.stack[self.first_stack - 1].w = b.x + b.w - b2.x
			self.stack[self.first_stack - 1].speed = 0
			score += 1
		# or he lost the game :(
		else:
			game_over()

		for i in range(self.first_stack):
			self.stack[i].y += brick_height

		brick_width = self.stack[self.first_stack - 1].w    

# game over
def game_over():
	loop = True
	# display losing text
	font = pygame.font.SysFont("Game Over", 100)
	text = font.render("Game Over!", True, black)
	textRect = text.get_rect()
	textRect.center = (width / 2, height / 2 - 80)

	# choose whether to restart the game or close it
	while loop:
		for event in pygame.event.get():
            # quit
			if event.type == pygame.QUIT:
				quit_game()
			if event.type == pygame.KEYDOWN:
                # quit
				if event.key == pygame.K_q:
					quit_game()
                # add brick
				if event.key == pygame.K_SPACE:
					GAME()
                # reset game
				if event.key == pygame.K_r:
					GAME()
            # add brick
			if event.type == pygame.MOUSEBUTTONDOWN:
				GAME()    
		display.blit(text, textRect)
		
		pygame.display.update()
		clock.tick()

# displaying the score on screen
def score_keeper():
	font = pygame.font.SysFont("Game Over", 60)
	text = font.render("Score: " + str(score), True, black)
	display.blit(text, (10, 10))

# close the game
def quit_game():
	pygame.quit()
	sys.exit()

# main game loop
def GAME():
	global brick_width, brick_height, score, brick_index, speed
	loop = True

	brick_height = 20
	brick_width = 120
	brick_index = 0
	speed = 3

	score = 0

	stack = Stack()
	stack.addnew_brick()

	# get input
	while loop:
		for event in pygame.event.get():
			# quitting the game
			if event.type == pygame.QUIT:
				quit_game()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					quit_game()
				if event.key == pygame.K_r:
					GAME()
				# adding the current brick to the stack
				if event.key == pygame.K_SPACE:
					stack.push_to_stack()
					stack.addnew_brick()
			# adding the current brick to the stack
			if event.type == pygame.MOUSEBUTTONDOWN:
				stack.push_to_stack()
				stack.addnew_brick()

		display.blit(background, (0, 0))

		stack.move()
		stack.show()

		score_keeper()
		
		pygame.display.update()
		clock.tick(60)