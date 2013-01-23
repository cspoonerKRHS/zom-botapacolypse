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

man = Man(5, [400, 400])
zombies = [] 
maxZombies = 4
robots = []
maxRobots = 4
mazeWall = MazeWall([100,100])
mazeWall.place([200, 200])
stick = Stick([125, 100])
taser = Taser([300,300])
stunGun = StunGun([150,200])
electricity = Electricity([1,1], [130,206])
pistol = Pistol([250,250])
projectile = Projectile([2,2], [500,500])
healthBar = HealthBar([630, 10])


bgColor = 100,100,10

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
        man.move()
        man.collideWall()
        man.collideMazeWall(mazeWall)
        for zombie in zombies:
            man.collideZombie(zombie)
        for robot in robots:
            man.collideRobot(robot)
        man.collideStick(stick)
        man.collideTaser(taser)
        man.collideStunGun(stunGun)
        man.collideElectricity(electricity)
        man.collidePistol(pistol)
        if man.attackWithStick(stick, Zombie):
            if stick.attack(zombie):
                stick.useDown(zombie, 1)
        if man.attackWithStick(stick, Robot):    
            if stick.attack(robot):
                stick.useDown(robot, 1)
        if man.attackWithStick(stick, MazeWall):    
            if stick.attack(mazeWall):
                stick.useDown(mazeWall, 4)
        if man.attackWithTaser(taser, Zombie):
            if taser.attack(zombie):
                taser.useDown(zombie, 1)
        if man.attackWithTaser(taser, Robot):    
            if taser.attack(robot):
                taser.useDown(robot, 1)
        if man.attackWithTaser(taser, MazeWall):    
            if taser.attack(mazeWall):
                taser.useDown(mazeWall, 1)
        if man.attackWithStunGun(stunGun, Zombie):
            if stunGun.attack(zombie):
                stunGun.useDown(zombie, 1)
        if man.attackWithStunGun(stunGun, Robot):    
            if stunGun.attack(robot):
                stunGun.useDown(robot, 1)
        if man.attackWithStunGun(stunGun, MazeWall):    
            if stunGun.attack(mazeWall):
                stunGun.useDown(mazeWall, 1)
        if man.attackWithPistol(pistol, Zombie):
            if pistol.attack(zombie):
                pistol.useDown(zombie, 1)
        if man.attackWithPistol(pistol, Robot):    
            if pistol.attack(robot):
                pistol.useDown(robot, 1)
        if man.attackWithPistol(pistol, MazeWall):    
            if pistol.attack(mazeWall):
                pistol.useDown(mazeWall, 1)
            
    
    while len(zombies) < maxZombies:
        zombieSpeed = [random.randint(1,6), 
                     random.randint(1,6)]
        zombiePos = [random.randint(100,screenWidth-100),
                   random.randint(100,screenHeight/2)]
        zombies += [Zombie(zombieSpeed, zombiePos, screenSize)]
        
    for zombie in zombies:
        if zombie.unDead:
            zombie.move()
            zombie.collideZombie(zombie)
            zombie.collideMazeWall(mazeWall)
            zombie.collideWall(screenWidth, screenHeight)
            for robot in robots:
                zombie.collideRobot(robot)
            if zombie.chase(man):
                for first in range(0,len(zombies)-2):
                    for second in range(first+1, len(zombies)-1):
                        zombies[first].collideZombie2(zombies[second])
            zombie.biteMan(man)
            zombie.dropItem()
        if not zombie.unDead:
            zombies.remove(zombie)  

    for first in range(0,len(zombies)-2):
        for second in range(first+1, len(zombies)-1):
            zombies[first].collideZombie(zombies[second])
            
    
    while len(robots) < maxRobots:
        robotSpeed = [random.randint(1,6), 
                     random.randint(1,6)]
        robotPos = [random.randint(100,screenWidth-100),
                   random.randint(100,screenHeight/2)]
        robots += [Robot(robotSpeed, robotPos, screenSize)]
        
    for robot in robots:
        if robot.living:
            robot.move()
            robot.collideMazeWall(mazeWall)
            robot.collideRobot(robot)
            robot.collideWall(screenWidth, screenHeight)
            robot.shootElect(man)
            if not robot.shootElect(man):
                robot.move()
            robot.hurt()
            robot.dropItem()
        if not robot.living:
            robots.remove(robot)
            
    for first in range(0,len(robots)-2):
        for second in range(first+1, len(robots)-1):
            robots[first].collideRobot(robots[second])

    #stick.swing.whack.snapInHalf
       
    screen.fill(bgColor)
    
    screen.blit(mazeWall.surface, mazeWall.rect)    
    screen.blit(man.surface, man.rect)
    for zombie in zombies:
        if zombie.unDead:
            screen.blit(zombie.surface, zombie.rect)
    for robot in robots:
        if robot.living:
            screen.blit(robot.surface, robot.rect)
    if stick.notBroken:
        screen.blit(stick.surface, stick.rect)
    if taser.notBroken:
        screen.blit(taser.surface, taser.rect)
    if stunGun.notBroken:
        screen.blit(stunGun.surface, stunGun.rect)
    if stick.notBroken:
        screen.blit(stick.surface, stick.rect)    
    if pistol.notBroken:
        screen.blit(pistol.surface, pistol.rect)
    if pistol.notBroken:
        if pistol.attack:
            screen.blit(projectile.surface, projectile.rect)
    if stunGun.notBroken:
        if stunGun.attack:
            screen.blit(electricity.surface, electricity.rect)
    screen.blit(healthBar.surface, healthBar.rect)
    
    pygame.display.flip()
    #print "-----------------------"
    clock.tick(35)
    #print clock.get_fps()
    #print "-----------------------"

     
    
