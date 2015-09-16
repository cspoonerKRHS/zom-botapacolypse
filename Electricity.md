# Introduction #

The electricity is used by the Robot, when the Robot attacks, the electricity is moved out of it and is used as a projectile. If it hits the Man, it will cause damage. Does 1% DMG on zombies, 1% DMG on the Man.

# Attributes #

  * shotSpawn: when the stun gun attacks, object will appear  in the direction of the player, only few units in front of the robot
  * speed: two part list with x and y integers
  * Rect: the basic length and width, in square, of the surface
  * Surface: the part that can be seen
  * 

# Methods #

  * def init: creates the object and allows it to have the attributes
  * def shotSpawn: when the object is spawned and begins to move
  * def move: when the object moves using speed
  * def collideMan: when object hits the player
  * def collideZombie: when the object collides with the zombie
  * def kill: when the objects hits the enemy, and kills
  * def living: if the object is still living or not