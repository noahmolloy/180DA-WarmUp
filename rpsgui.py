import random
import pygame

from pygame.locals import(
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_ESCAPE,
	KEYDOWN,
	QUIT,
	K_r,
	K_p,
	K_s,
)

class button():
	def __init__(self,x,y,pos,w,h):
		self.x = x
		self.y = y
		self.pos = pos
		self.w = w
		self.h = h
		
	def clicked(self,pos):
		self.pos = pygame.mouse.get_pos()
		if self.pos[0] > self.x and self.pos[0] < self.x + self.w:
			if self.pos[1] > self.y and self.pos[1] < self.y + self.h:
				return True
		return False

class game():
	def __init__(self):
		pygame.init()

		width = 800
		height = 600	
		self.screen = pygame.display.set_mode((width, height))

		self.bg = pygame.image.load("background.jpg")
		self.RB = pygame.image.load("rock.png").convert_alpha()
		self.PB = pygame.image.load("paper.png").convert_alpha()
		self.SB = pygame.image.load("scissors.png").convert_alpha()

		self.choose_RB = pygame.image.load("rock.png").convert_alpha()
		self.choose_PB = pygame.image.load("paper.png").convert_alpha()
		self.choose_SB = pygame.image.load("scissors.png").convert_alpha()

		self.screen.blit(self.bg, (0,0))
		self.screen.blit(self.RB, (20,400))
		self.screen.blit(self.PB, (400,400))
		self.screen.blit(self.SB, (600,400))

		self.RBO = button(30,400,(30,400),300, 140)
		self.PBO = button(400,400,(400,400),300, 140)
		self.SBO = button(600,400,(600,400),300, 140)

		self.font = pygame.font.Font('freesansbold.ttf',32)
		self.text = self.font.render(f" ", True, (0,0,0))

		self.pl_score = 0

	def player(self):
		if self.RBO.clicked(30):
			self.p_option = "rock"
			self.screen.blit(self.choose_RB, (120, 200))
		elif self.PBO.clicked(400):
			self.p_option = "paper"
			self.screen.blit(self.choose_PB, (120, 200))
		elif self.SBO.clicked(600):
			self.p_option = "scissors"
			self.screen.blit(self.choose_SB, (120, 200))

		return self.p_option

	def cpu(self):
		self.pc_random_choice = " "
		hands = ["rock", "paper", "scissors"]
		choice = random.choice(list(hands))
		if choice == "rock":
			self.pc_random_choice = "rock"
			choice = self.choose_RB
		elif choice == "paper":
			self.pc_random_choice = "paper"
			choice = self.choose_PB
		elif choice == "scissors":
			self.pc_random_choice = "scissors"
			choice = self.choose_SB
		choice = self.screen.blit(choice, (600, 200))
		return choice


	def pl_score(self):
		self.pl_score = 0

		pplay = self.p_option
		cplay = self.pc_random_choice

		if pplay == cplay:
			pass
		elif pplay == "rock" and cplay == "scissors":
			self.pl_score += 1
		elif pplay == "paper" and cplay == "rock":
			self.pl_socre += 1
		elif pplay == "scissors" and cplay == "paper":
			self.pl_score += 1
		else:
			self.pl_score += 1

		return self.pl_score

	def image_reset(self):
		self.screen.blit(self.text, (330,0))
		self.text = self.font.render(" ", True, (0, 0 ,0))
		self.screen.blit(self.bg, (0,0))
		self.screen.blit(self.RB, (20, 400))
		self.screen.blit(self.PB, (400, 400))
		self.screen.blit(self.SB, (600, 400))
		pass

	def game_loop(self):
		running = True
		clock = pygame.time.Clock()
		rps = game()

		while running:
			pygame.display.update()
			self.screen.blit(self.text, (330, 0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running == False
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						running = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					if self.RBO.clicked(30) or self.PBO.clicked(400) or self.SBO.clicked(600):
						rps.image_reset()
						rps.player()
						rps.cpu()

						self.pl_score += rps.pl_score()
						self.text = self.front.render(f"{self.pl_score}", True, (255, 255, 255))
			pygame.display.flip()
			clock.tick(30)
		pygame.quit()

if __name__ == '__main__':
	loop = game()
	loop.game_loop()

#
#pygame.init()

#SWIDTH = 800
#SHEIGHT = 600

#screen = pygame.display.set_mode([SWIDTH,SHEIGHT])
#pygame.display.set_caption('Show Text')

#font = pygame.font.Font('freesansbold.ttf',32)

#text = font.render("(r)ock (p)aper (s)icssors", True, (0,0,0))
#textRect = text.get_rect()
#textRect.center = (SWIDTH//2,SHEIGHT//2)

#running = True

#while running:

#	hands = ["R", "P", "S"]
#	cplay = "R"
	#cplay = random.choice(hands)

#	for event in pygame.event.get():
#		if event.type == KEYDOWN:
#			if event.key == K_ESCAPE:
#				running = False
#			if event.key == K_r:
#				running = False
#				pplay = "R"
#				if pplay == cplay:
#					result = font.render('Tie!',True,(0,0,0))
#					resultRect = result.get_rect()
#					resultRect.center = (SWIDTH//2, 2*SHEIGHT//3)
#					result.blit(result, resultRect)
#					pygame.display.flip()

#		elif event.type == QUIT:
#			running == False

#	screen.fill((222,222,222))
#	screen.blit(text, textRect)

	#surf = pygame.Surface((50,50))
	#surf.fill((200,0,0))
	#rect = surf.get_rect()
	#screen.blit(surf,(SWIDTH/4,SHEIGHT/2))

	#surf2 = pygame.Surface((50,50))
	#surf2.fill((0,200,0))
	#rect = surf2.get_rect()
	#screen.blit(surf2,(SWIDTH/1.5,SHEIGHT/2))

	#surf3 = pygame.Surface((50,50))
	#surf3.fill((0,0,200))
	#rect = surf3.get_rect()
	#screen.blit(surf3,(SWIDTH/2,SHEIGHT/2))

#	pygame.display.flip()

#pygame.quit()
