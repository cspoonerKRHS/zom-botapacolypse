import pygame, math, sys, random
from Man import Man
from Zombie import Zombie
from Robot import Robot
from MazeWall import MazeWall
from Stick import Stick
from Taser import Taser
from StunGun import StunGun
from Electricity import Electricity
from Pistol import Pistol
from Projectile import Projectile
from HealthBar import HealthBar

if pygame.mixer:
    pygame.mixer.init()

pygame.init()

clock = pygame.time.Clock()

screenWidth = 800
screenHeight = 600

screenSize = screenWidth, screenHeight
screen = pygame.display.set_mode(screenSize)

man = Man("man.png",5, [100, 100])
zombies = [] 
maxZombies = 4
robots = []
maxRobots = 3
mazewall = MazeWall()
stick = Stick([125, 100])
taser = Taser()
stunGun = StunGun()
electricity = Electricity()
pistol = Pistol()
projectile = Projectile()
healthBar = HealthBar()

bgColor = 0,0,0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP 
                or event.key == pygame.K_w):
                    man.direction("up")
            elif (event.key == pygame.K_DOWN 
                or event.key == pygame.K_s):
                    man.direction("down")
            elif (event.key == pygame.K_RIGHT 
                or event.key == pygame.K_d):
                    man.direction("right")
            elif (event.key == pygame.K_LEFT 
                or event.key == pygame.K_a):
                    man.direction("left")
            elif (event.key == pygame.K_SPACE):
                man.attack("attack")
        elif event.type == pygame.KEYUP:
            if (event.key == pygame.K_UP 
                or event.key == pygame.K_w):
                    man.direction("stop up")
            elif (event.key == pygame.K_DOWN 
                or event.key == pygame.K_s):
                    man.direction("stop down")
            elif (event.key == pygame.K_RIGHT 
                or event.key == pygame.K_d):
                    man.direction("stop right")
            elif (event.key == pygame.K_LEFT 
                or event.key == pygame.K_a):
                    man.direction("stop left")
            elif (event.key == pygame.K_SPACE):
                man.attack("stop attack")
            
                    
    if man.living:
        man.collideWall(screenWidth, screenHeight)
        man.collideMazeWall(mazeWall)
        for zombie in zombies
            man.collideZombie(zombie)
        for robot in robots
            man.collideRobot(robot)
        man.collideStick(stick)
        man.collideTaser(taser)
        man.collideStunGun(stunGun)
        man.collideElectricity(electricity)
        man.collidePistol(pistol)
        if man.attack(stick)
            if stick.attack(zombie)
                stick.useDown(zombie, 1)
            elif stick.attack(robot)
                stick.useDown(robot, 1)
            elif stick.attack(mazeWall)
                stick.useDown(mazeWall, 4)
        if man.attack(taser)
            if taser.attack(zombie)
                taser.useDown(zombie, 1)
            elif taser.attack(robot)
                taser.useDown(robot, 1)
            elif taser.attack(mazeWall)
                taser.useDown(mazeWall, 1)
        if man.attack(stunGun)
            if stunGun.attack(zombie)
                stunGun.useDown(zombie, 1)
            elif stunGun.attack(robot)
                stunGun.useDown(robot, 1)
            elif stunGun.attack(mazeWall)
                stunGun.useDown(mazeWall, 1)
        if man.attack(pistol)
            if pistol.attack(zombie)
                pistol.useDown(zombie, 1)
            elif pistol.attack(robot)
                pistol.useDown(robot, 1)
            elif pistol.attack(mazeWall)
                pistol.useDown(mazeWall, 1)
            
    
    while len(zombies) < maxZombies:
        zombieSpeed = [random.randint(1,6), 
                     random.randint(1,6)]
        zombiePos = [random.randint(100,screenWidth-100),
                   random.randint(100,screenHeight/2)]
        zombies += [Zombie(zombieSpeed, zombiePos)]
        
    for zombie in zombies:
        if zombie.unDead:
            zombie.move()
            zombie.collideMazeWall(mazeWall)
            zombie.collideWall(screenWidth, screenHeight)
            zombie.collideRobot(robot)
            zombie.collideElectricity(electricity)
            zombie.collideProjectile(projectile)
            zombie.sight(man)
            zombie.chase(man)
            zombie.bite(man)
            zombie.hurt(man)
            zombie.die(man)
            zombie.dropItem(man)
            if not zombie.unDead:
                zombies.remove(zombie)            
            
    
    while len(robots) < maxRobots:
        robotSpeed = [random.randint(1,6), 
                     random.randint(1,6)]
        robotPos = [random.randint(100,screenWidth-100),
                   random.randint(100,screenHeight/2)]
        robots += [Robot(robotSpeed, robotPos)]
        
    for robot in robots:
        if robot.living = True:
        robot.move()
        robot.collideMazeWall(mazeWall)
        robot.collideWall(screenWidth, screenHeight)
        robot.collideElectricity(electricity)
        robot.collideProjectile(projectile)
        robot.sight(man)
        robot.shootElect(man)
        robot.hurt(man)
        robot.dropItem(man)
        if not robot.living:
            robots.remove(robot)

    #stick.swing.whack.snapInHalf
       
    screen.fill(bgColor)
    
    screen.blit(mazeWall.surface, mazeWall.rect)    
    screen.blit(man.surface, man.rect)
    for zombie in zombies:
        if zombie.living
            screen.blit(zombie.surface, zombie.rect)
    for robot in robots:
        if robot.living
            screen.blit(robot.surface, robot.rect)
    if stick.living
        screen.blit(stick.surface, stick.rect)
    if taser.living
        screen.blit(taser.surface, taser.rect)
    if stunGun.living
        screen.blit(stunGun.surface, stunGun.rect)
    if stick.living
        screen.blit(stick.surface, stick.rect)    
    if pistol.living
        screen.blit(pistol.surface, pistol.rect)
    if pistol.living
        if pistol.attack
            screen.blit(projectile.surface, projectile.rect)
    if stunGun.living
        if stunGun.attack
            screen.blit(electricity.surface, electricity.rect)
    
    
    clock.tick(30)
    print clock.get_fps()

     
    
