import pygame, math, sys, random
from Man import Man
from Zombie import Zombie
from Robot import Robot
from MazeWall import MazeWall
from Stick import Stick
from Electricity import Electricity
from Pistol import Pistol
from Projectile import Projectile
from HealthBar import HealthBar
from mazeMap1 import level
from gameover import GameOver

if pygame.mixer:
    pygame.mixer.init()

#-------------Level----------------------
pygame.init()

clock = pygame.time.Clock()

screenWidth = 800
screenHeight = 600

screenSize = screenWidth, screenHeight
screen = pygame.display.set_mode(screenSize)

map = level("maze1.lvl", screenSize)

bgColor = 50, 50, 50

#----------------characters/environment--------------------
man = Man(3, [40, 40])
zombies = [] 
maxZombies = 25
robots = []
maxRobots = 25
#mazeWall = MazeWall([100,100])
#mazeWall.place([200, 200])
stick = Stick([125, 125])
electricitys = [] 
maxelectricitys = 2
pistol = Pistol([250,250])
projectiles = []
maxProjectiles = 2
healthBar = HealthBar([630, 10])

while len(zombies) < maxZombies:
    zombieSpeed = [random.randint(1,6), 
                 random.randint(1,6)]
    zombiePos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                             random.randint(map. mazeWallSize,screenHeight - map.mazeWallSize)]
    zombies += [Zombie(zombieSpeed, zombiePos, screenSize)]
    collided = True
    while collided:
        collided = False
        for mazeWall in map.mazeWalls:
            if zombies[-1].collideMazeWall(mazeWall):
                zombiePos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                             random.randint(map.mazeWallSize, screenHeight - map.mazeWallSize)]
                print zombiePos
                zombies[-1].place(zombiePos)
                collided = True
            elif zombies[-1].chase(man):
                zombiePos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                             random.randint(map.mazeWallSize, screenHeight - map.mazeWallSize)]
                print zombiePos
                zombies[-1].place(zombiePos)
                collided = True

while len(robots) < maxRobots:
    robotSpeed = [random.randint(1,6), 
                 random.randint(1,6)]
    robotPos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                             random.randint(map. mazeWallSize,screenHeight - map.mazeWallSize)]
    robots += [Robot(robotSpeed, robotPos, screenSize)]
    collided = True
    while collided:
        collided = False
        for mazeWall in map.mazeWalls:
            if robots[-1].collideMazeWall(mazeWall):
                robotPos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                             random.randint(map.mazeWallSize, screenHeight - map.mazeWallSize)]
                print robotPos
                robots[-1].place(robotPos)
                collided = True
            elif robots[-1].see(man):
                robotPos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                             random.randint(map.mazeWallSize, screenHeight - map.mazeWallSize)]
                print robotPos
                robots[-1].place(robotPos)
                collided = True
                     


#----------------------Game-----------------------
while True:
    while man.living:
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
                    projectiles += [Projectile(10, man.rect.center, man.heading, screenSize)]
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
             
#------------------------Man----------------------                    
        if man.living:
            man.move()
            man.collideWall(screenWidth, screenHeight)
            man.collideStick(stick)
            man.pickUpStick(stick)
            for robot in robots:
                man.collideRobot(robot)
            man.collideStick(stick)
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
            if man.attackWithPistol(pistol, Zombie):
                if pistol.attack(zombie):
                    pistol.useDown(zombie, 1)
            if man.attackWithPistol(pistol, Robot):    
                if pistol.attack(robot):
                    pistol.useDown(robot, 1)
            if man.attackWithPistol(pistol, MazeWall):    
                if pistol.attack(mazeWall):
                    pistol.useDown(mazeWall, 1)
            healthBar.downHealth(man)
            man.remove()

#--------Projectile Stuff-----------------
            for projectile in projectiles:
                if projectile.notBroken:
                    projectile.move()
                    projectile.collideWall(screenSize)
                    for zombie in zombies:  
                        projectile.collideAttackZombie(zombie)
                    for robot in robots:
                        projectile.collideAttackRobot(robot)
                if not projectile.notBroken:
                    projectiles.remove(projectile)
                
#------------Zombie---------------------
        """
        while len(zombies) < maxZombies:
            zombieSpeed = [random.randint(1,6), 
                         random.randint(1,6)]
            zombiePos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                                     random.randint(map. mazeWallSize,screenHeight - map.mazeWallSize)]
            zombies += [Zombie(zombieSpeed, zombiePos, screenSize)]
            collided = True
            while collided:
                collided = False
                for mazeWall in map.mazeWalls:
                    if zombies[-1].collideMazeWall(mazeWall):
                        zombiePos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                                     random.randint(map.mazeWallSize, screenHeight - map.mazeWallSize)]
                        print zombiePos
                        zombies[-1].place(zombiePos)
                        collided = True
                     
        """              
            
        for zombie in zombies:
            if zombie.unDead:
                zombie.move()
                zombie.collideZombie(zombie)
                zombie.collideMazeWall(mazeWall)
                zombie.collideWall(screenWidth, screenHeight)
                for robot in robots:
                    zombie.collideRobot(robot)
                if zombie.chase(man):
                    zombie.collideWall(screenWidth, screenHeight)
                    zombie.collideMazeWall(mazeWall)
                    for first in range(0,len(zombies)-2):
                        for second in range(first+1, len(zombies)-1):
                            zombies[first].collideZombie2(zombies[second])
                zombie.biteMan(man)
                zombie.dropItem()
                if zombie.unDead == False:
                    zombies.remove(zombie)
                

        for first in range(0,len(zombies)-2):
            for second in range(first+1, len(zombies)-1):
                zombies[first].collideZombie(zombies[second])
                
#------------------------Robot-------------------------    
        """
        while len(robots) < maxRobots:
            robotSpeed = [random.randint(1,6), 
                         random.randint(1,6)]
            robotPos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                                     random.randint(map. mazeWallSize,screenHeight - map.mazeWallSize)]
            robots += [Robot(robotSpeed, robotPos, screenSize)]
            collided = True
            while collided:
                collided = False
                for mazeWall in map.mazeWalls:
                    if robots[-1].collideMazeWall(mazeWall):
                        robotPos = [random.randint(map.mazeWallSize, screenWidth - map.mazeWallSize),
                                     random.randint(map.mazeWallSize, screenHeight - map.mazeWallSize)]
                        print robotPos
                        robots[-1].place(robotPos)
                        collided = True
            """
            
        for robot in robots:
            if robot.living:
                robot.checkLiving()
                robot.move()
                robot.collideMazeWall(mazeWall)
                robot.collideRobot(robot)
                robot.collideWall(screenWidth, screenHeight)
                if robot.see(man):
                    electricitys += [Electricity(man.rect.center, robot.rect.center, screenSize)]
                else:
                    robot.move()
            if not robot.living:
                robots.remove(robot)
                
        for first in range(0,len(robots)-2):
            for second in range(first+1, len(robots)-1):
                robots[first].collideRobot(robots[second])
#-----------------Electricity Stuff----------------

        for electricity in electricitys:
            if electricity.notBroken:
                electricity.move()
                electricity.collideWall(screenSize)
                electricity.collideAttackMan(man)
                for mazeWall in map.mazeWalls:
                    electricity.collideMazeWall(mazeWall)
                for zombie in zombies:
                    electricity.collideAttackZombie(zombie)
                if not electricity.notBroken:
                    electricitys.remove(electricity)
   

#------------------stick.swing.whack.snapInHalf--------------------------
        if stick.notBroken:
            stick.collideZombie(zombie)
            stick.collideRobot(robot)
            #for mazeWall in map.mazeWalls:
            #    stick.collideMazeWall(mazeWall)

#--------------------Blit-------------------    
        for mazeWall in map.mazeWalls:
            for zombie in zombies:
                zombie.collideMazeWall(mazeWall)
            for robot in robots:
                robot.collideMazeWall(mazeWall)
            for projectile in projectiles:
                projectile.collideMazeWall(mazeWall)
            man.collideMazeWall(mazeWall)
            screen.blit(mazeWall.surface, mazeWall.rect) 
        if man.living:
            screen.blit(man.surface, man.rect)
        for zombie in zombies:
            if zombie.unDead:
                screen.blit(zombie.surface, zombie.rect)
        for robot in robots:
            if robot.living:
                screen.blit(robot.surface, robot.rect)
        if stick.notBroken:
            screen.blit(stick.surface, stick.rect)   
        if pistol.notBroken:
            screen.blit(pistol.surface, pistol.rect)
        for projectile in projectiles:
            if projectile.notBroken:
                screen.blit(projectile.surface, projectile.rect)
        for electricity in electricitys:
            if electricity.notBroken:
                screen.blit(electricity.surface, electricity.rect)       
        screen.blit(healthBar.surface, healthBar.rect)
        
        pygame.display.flip()
        clock.tick(35)
        screen.fill(bgColor)
        #print clock.get_fps()

#--------------------EndGame--------------
    while not man.living:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        gameover = GameOver("rsc/Menus/gameover.png", [0,0], screenSize)
        screen.fill([0, 0, 0])
        screen.blit(gameover.surface, gameover.rect)
        gameover.place([400,300])
        pygame.display.flip()