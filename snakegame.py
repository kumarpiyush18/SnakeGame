import pygame,sys,random,time

check_errors=pygame.init()
if check_errors[1]>0:
	print("(!) had {0} initializing errors,exiting...".format(check_errors[1]))
	sys.exit(-1)
else:
	print("(+) Pygame successfully initialized")

#play surface
playSurface=pygame.display.set_mode((720,460))
#title bar
pygame.display.set_caption('Snake Game')

#color
red=pygame.Color(255,0,0)#game over
green=pygame.Color(0,255,0)#snake
black=pygame.Color(0,0,0)#score
white=pygame.Color(255,255,255)#backgound
brown=pygame.Color(165,42,42)#food

#fps (frame per second controller)
fpsController=pygame.time.Clock()
#variable
SnakePos =[100,50]
SnakeBody=[[100,50],[90,50],[80,50]]
foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpwan=True

direction='RIGHT'
changeto=direction

score=0

#game over function
def gameOver():
	myFont=pygame.font.SysFont('monaco',72)
	GOsurf=myFont.render('Game over!',True,red)
	GOrect=GOsurf.get_rect()
	GOrect.midtop=(360,15)
	playSurface.blit(GOsurf,GOrect)
	showScore(2)
	pygame.display.flip()
	time.sleep(4)
	pygame.quit()#pygame exit
	sys.exit()#console
def showScore(choice=1):
	sFont=pygame.font.SysFont('monaco',24)
	Ssurf=sFont.render('Score {0}'.format(score),True,white)
	Srect=Ssurf.get_rect()
	if choice==1:
		Srect.midtop=(80,10)
	else:
		Srect.midtop=(360,120)
	
	playSurface.blit(Ssurf,Srect)
	pygame.display.flip()
'''def changeBackground():

	if showScore()==0:
		return white
	if showScore()>0 and showScore()<10:
		return black
	if showScore()>10:
		return green



c=changeBackground()'''



# main logic of the game
while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT or event.key==ord('d'):
				changeto='RIGHT'
			if event.key==pygame.K_RIGHT or event.key==ord('a'):
				changeto='LEFT'
			if event.key==pygame.K_RIGHT or event.key==ord('w'):
				changeto='UP'
			if event.key==pygame.K_RIGHT or event.key==ord('s'):
				changeto='DOWN'
			if event.key==pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))
	#validation of direction
	if changeto=='RIGHT' and not direction=='LEFT':
		direction='RIGHT'
	if changeto=='LEFT' and not direction=='RIGHT':
		direction='LEFT'
	if changeto=='UP' and not direction=='DOWN':
		direction='UP'
	if changeto=='DOWN' and not direction=='UP':
		direction='DOWN'
	#update snake [x,y] position
	if direction=='RIGHT':
		SnakePos[0]+=10
	if direction=='LEFT':
		SnakePos[0]-=10
	if direction=='UP':
		SnakePos[1]-=10
	if direction=='DOWN':
		SnakePos[1]+=10
	#snake body mechanism
	SnakeBody.insert(0,list(SnakePos))
	if SnakePos[0]==foodPos[0] and SnakePos[1]==foodPos[1]:
		score+=1
		foodSpwan=False
	else:
		SnakeBody.pop()
	if foodSpwan==False:
		foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
	foodSpwan=True

	playSurface.fill(black)
	#pygame.display.flip()
	for pos in SnakeBody:
	    pygame.draw.rect(playSurface,green,
	    pygame.Rect(pos[0],pos[1],10,10))#three argu
	pygame.draw.rect(playSurface,brown,
		pygame.Rect(foodPos[0],foodPos[1],10,10))
	if SnakePos[0]>710 or SnakePos[0]<0:
		gameOver()
	if SnakePos[1]>450 or SnakePos[1]<0:
		gameOver()
	for block in SnakeBody[1:]:
		if SnakePos[0]==block[0] and SnakePos[1]==block[1]:
			gameOver()
  
    	
	if score==0 or score>5:
		speed=10
	if score>10:
		speed=score
	pygame.display.flip()
	showScore()
	fpsController.tick(speed)









