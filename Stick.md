# Description #

This is the starting weapon, it breaks after 4 uses, or 1 use if it hits the walls


## Details ##

  * Drops from [Zombie](Zombie.md)
  * Does 25 DMG
  * Can kill 1 enemy if at full condition
  * Is the weakest weapon

# Attributes #

  * place: beginning position in the game
  * Rect: the basic length and width, in square, of the surface
  * Surface: the part that can be seen
  * attack: when the actual object attacks
  * uses: the amount of times it may be used
  * break: when the object breaks
  * stickSound: the shock sound of the taser

# Methods #

  * def init: creates the object and allows it to have the attributes
  * def place: places the object on the maze
  * def attack: when the object is used to attack
  * def collideZombie: when the object collide with zombie
  * def collideRobot: when the object collides with robot
  * def collideMazeWall: when the object collides with the maze wall
  * def useDown: when the object is used once
  * def break: when the object "dies"
  * def remove: removes the object from the game if not living

### Weapons ###
  * [Stick](Stick.md)
  * [Taser](Taser.md)
  * [StunGun](StunGun.md)
  * [Pistol](Pistol.md)