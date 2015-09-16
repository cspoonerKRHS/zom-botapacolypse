# Description #

> In this game, you, the player are trapped in a maze. Your goal is to escape the maze. However, zombies and robots are dispersed throughout the maze and can kill you. Robots can shoot and if you are shot your life goes down. Zombies can bite you and if this happens, your life will slowly drain and you will turn into a zombie. You, the player, can pick up weapons to defend yourself and get safely to the end. There will be a level with just zombies and another with just robots, and  another level with both robots and zombies.


# Controls #
  * Forward: W
  * Back: S
  * Right: D
  * Left: A

# Objects #

## [Man](Man.md) ##
The player character that you move throughout the maze trying to get to the end and avoiding/attacking the zombies and robots

## [Zombie](Zombie.md) ##
An enemy character that will wander throughout the maze. It will chase the man if it sees it and will attempt to kill him. The Zombie can be killed by the man or by a robot.

## [Robot](Robot.md) ##
An enemy character that wanders through the maze. It can shoot and will chase the man if it sees him. The robot will attempt to kill the man but the man is also able to kill the robot. It will also try to kill zombies.

## [MazeWall](MazeWall.md) ##
The object that makes up the maze. It is unbreakable, and cannot be jumped over or dug under.

## [Stick](Stick.md) ##
A promising, reliable object for protection. It can be picked up by the man to be used to kill robots and zombies. It will break after a certain amount of hits.

## [Taser](Taser.md) ##
A short range weapon that shoots electricity. It can be used on both robots and zombies, but it will kill robots in one hit. It can only be used twice before it breaks.

## [StunGun](StunGun.md) ##
A long range weapon that shoots electricity. It can be used on both robots and zombies, but it will kill robots in one hit. It can only be used once before it breaks.

## [Electricity](Electricity.md) ##
Damaging object that comes out of a Stun Gun or Taser. Robots also shoot electricity but can be easily be killed by it.

## [Pistol](Pistol.md) ##
A lethal and rare weapon. It will be placed in a maze rarely and will usually be found at a dead end.

## [Projectile](Projectile.md) ##
Damaging object that is shot by the pistol. It will damage both robots and zombies and has the longest range.

## Game ##
  * Create Screen
  * Create Menu
  * Create Man
  * Create Stick (in front of man)
  * Create Zombie
  * Create Robot with stun gun
  * Create Walls
  * Create Taser
  * Create Stun Gun
  * Create Pistol
  * Create Weapon Spawns
  * Create Projectile
  * Create Electricity
  * Create Health Bar

## Play Loop ##
  * Man Moves
  * Zombie Moves
  * Robot Moves
  * Man collides with Wall
  * Zombie collides with Wall
  * Robot collides with Wall
  * Man collides with Maze Wall
  * Zombie collides with Maze Wall
  * Robot collides with Maze Wall
  * Man collides with Zombie
  * Man collides with Robot
  * Zombie collides with Robot
  * Zombie collides with zombie
  * Robot collides with Robot
  * Man attacks Zombie
  * Man attacks Robot
  * Zombie attacks Man
  * Robot shoots man with stun gun
  * Robot shoots zombie with stun gun
  * Man attacks Zombie with stick
  * Man attacks Robot with stick
  * Man picks up Stun gun
  * Man shoots stun gun
  * Man attacks Zombie with stun gun
  * Man attacks Robot with stun gun
  * Man picks up taser
  * Man shoots taser
  * Man attacks Zombie with taser
  * Man attacks Robot with taser
  * Man picks up Pistol
  * Man shoots pistol
  * Man attacks zombie with pistol
  * Man attacks robot with pistol
  * Man dies
  * Robot dies
  * Zombie dies
  * Game over