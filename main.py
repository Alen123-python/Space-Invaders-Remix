import pygame
import sys

# importing modules
pygame.init()
pygame.mixer.init()
# initializing pygame and mixer
width = 700
height = 600
res = (width, height)
# screen size variables
screen = pygame.display.set_mode(res,pygame.RESIZABLE)
# setting our window size
pygame.display.set_caption("Space Invaders")
# setting our window title
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
# defining our colours
clock = pygame.time.Clock()
frame_rate = 60
bg = pygame.image.load("Assets/Images/Background.jpeg").convert()#loading background image
bg = pygame.transform.scale(bg,res)#resizing background image to screen width and heigh
# setting up our frame rate meter
player = pygame.image.load("Assets/Images/Ship.png").convert_alpha()  # loading ship image
player = pygame.transform.scale(player, (100, 100))  # resizing ship image to 100 pixel width and 100 pixel height
playerX = width / 2 - 50  # setting our player X position
playerY = height - 100  # setting our player Y position
enemy = pygame.image.load("Assets/Images/Enemy.png").convert_alpha() # loading enemy image
enemy = pygame.transform.scale(enemy, (100,100)) # resizing enemy image to 100 pixel with and 100 pixel height
enemyX = 0#Enemy X position
enemyY = 0#Enemy Y position
enemySpeed = 2 #Speed of Enemy movement
DeadthSound = pygame.mixer.Sound("Assets/Music/Deadth.mp3")#loading deadth sound
pygame.display.set_icon(pygame.transform.scale(enemy,(32,32)))#making our enemy image as the icon and resizing it to 32 by 32 pixels
bullet = pygame.image.load("Assets/Images/Bullet.png").convert_alpha()#loading bullet image
bullet = pygame.transform.scale(bullet, (20,50))#setting bullet position
bulletX = playerX+50#setting bullet X position
bulletY = playerY#setting bullet Y position
bulletState = "ready"#definig bullet's state
bulletShootSound = pygame.mixer.Sound("Assets/Music/Laser.mp3")#loading bullet shoot sound effect
score = 0 #Score variable
font = pygame.font.SysFont(None, 72)#setting our font(instead of non you can define the location of your .tff and .otf files as a string)
scoreDisplay = font.render(str(score), True, white)#creating a text with the font 1st we give the text in this case score(note:the text can only be a string),
#second we made anti aliasing by making the second argument true, third is the color which is white variable which we defined before
pygame.mixer.music.load("Assets/Music/Music.mp3")#loading the music
pygame.mixer.music.set_volume(0.2)#setting the music volume to 0.2
pygame.mixer.music.play(-1)#playing the music
print("Thanks to Teminite & MDK for this awsome song!")#thanking the people behind the song
while True:
    scoreDisplay = font.render(str(score), True, white)#updating our scoreDisplay variable inside a while loop
    player_rect = player.get_rect(topleft=(playerX, playerY))#creating an invisible rectangle around our player(usefull for checking collisions)
    enemy_rect = enemy.get_rect(topleft=(enemyX,enemyY))#creating an invisible rectangle around our enemy(usefull for checking collisions)
    bullet_rect = bullet.get_rect(topleft=(bulletX,bulletY))#creating an invisible rectangle around our bullet(usefull for checking collisions)
    for event in pygame.event.get():#storing all events in a variable called event
        if event.type == pygame.QUIT:  # checking if the player clicked on the close button
            pygame.quit()
            sys.exit()
            # closing the application
        if event.type == pygame.VIDEORESIZE:#checking if the screen has been resized
            width,height = event.w,event.h #changing width and height
            res = (width,height)#changing resolution
            bg = pygame.transform.scale(bg, res)#resizing background to fit the screen
            playerY = height - 100  # setting our player Y position
    enemyX += enemySpeed#making the enemy move according to enemySpeed
    if enemyX >= width-100:#checking if enemy is going out of the screen
        enemySpeed = -abs(enemySpeed)
        enemyY += 50#changin enemyY position by 50
    elif enemyX <= 0:
        enemySpeed = +abs(enemySpeed)
        enemyY += 50
    keys = pygame.key.get_pressed()  # storing key presses in a vairlable called keys
    screen.blit(bg, (0,0))#rendering background
    if keys[pygame.K_LEFT]:  # checking left key is pressed
        playerX -= 5  # changing playerX position by -5
    elif keys[pygame.K_RIGHT]:  # checking  right key is pressed
        playerX += 5  # changing playerX position by +5
    if keys[pygame.K_SPACE]:
        if bulletState == 'ready':
            bulletShootSound.play()
            bulletState = 'fire'
    if bulletState == 'fire':#excuting the below code if bulletState is fire
        bulletY -= 15#shooting bullet upwards by 15 pixels
        screen.blit(bullet, bullet_rect)#rendering bullet to screen
        if bullet_rect.colliderect(enemy_rect):#checking if bullet_rect is colliding with enemy_rect
            score += 1#increasing score by 1
            DeadthSound.play()#playing deadth sound
            bulletX = playerX+50#changing playerX
            bulletY = playerY#changin playerY
            bulletState = "ready"#changing bullet state
            enemySpeed += +abs(0.5)#changing enemy speed to increase diffculty
            enemyX , enemyY = 0.1,0 #changing both enemyX and enemyY to 0 and 0
        if bulletY <= 0:#checking if bullet has gone out of screen
            bulletY = playerY#changin bullet Y
            bulletX = playerX+50#changing bullet X
            bulletState = "ready"#chaging bullet state to ready
    else:
        bulletX = playerX+50#setting bullet X position
    if playerX >= width - 100:  # checking if player is going out of window
        playerX = width - 100 #setting player position by substracting total screen width by player X scale
    elif playerX <= 0:  # checking if player is going out of window
        playerX = 0#setting player position to 0
    if player_rect.colliderect(enemy_rect):#checking if player_rect is colliding with enemy_rect
        DeadthSound.play()#playing deadth sound
        enemySpeed = 2#setting enemy speed to 2
        enemyX = 0 #setting enemy X to 0
        enemyY = 0#setting enemy Y to 0
        score = 0#setting score to 0
    screen.blit(player, player_rect)  # rendering player image
    screen.blit(enemy, enemy_rect) #rendering enemy image
    screen.blit(scoreDisplay, (0,0)) # rendering our score at 0,0 location
    pygame.display.update()  # updating the game
    clock.tick(frame_rate)  # telling our game to run in the given frame rate(which in this case is 60)
# our game mainloop
