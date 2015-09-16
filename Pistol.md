# Description #

A lethal and rare weapon. It will be placed in a maze rarely and will usually be found at a dead end. It shoots the [Projectile](Projectile.md) and can kill Zombies in one hit and does 75% damage to Robots.

# Attributes #

  * SmallRect: The basic size, length and width, of the object
  * SmallSurface: The sprite itself
  * place: the starting position of the object at the beginning of the game
  * shoot: when the object shoots the [Projectile](Projectile.md)
  * uses: the amount of times the object can be used before it breaks
  * break: when the object breaks after a certain amount of uses

# Methods #

  * def init: creates the object and allows it to have the attributes
  * def spawn: places the object on the maze
  * def createProjectile: creates the projectile when attack is pressed
  * def shoot: object is used to attack
  * def useDown: the object is used once
  * def break: the object breaks after a certain amount of uses
  * def remove: removes the object from the game if not living


### Weapons ###
  * [Stick](Stick.md)
  * [Taser](Taser.md)
  * [StunGun](StunGun.md)
  * [Pistol](Pistol.md)