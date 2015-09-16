# Description #

The zombie is spawned in the maze game and his main goal is to chase down the man and eat him. He is spawned in the beginning of the game and he may move freely and lifelessly. Once he sees the man, he goes into a berserk and chases down the man and attempts to eat him. The man may kill him if he wishes and/or if he can. The zombie carries no weapons.

# Attributes #

  * Speed: two part list with x and y in integers
  * maxSpeed: the fastest speed the object can move
  * position: beginning position in the game
  * Rect: the basic length and width, in square, of the surface
  * Surface: the part that can be seen
  * Sight: the area in which the object can see something
  * Bite: the attack move in which this object does
  * Hurt: when the object is attacked, and hit
  * Dead: whether the object is there or not
  * lifebar: gives the object a life bar


# Methods #

  * def init: creates the object and allows it to have the attributes
  * def move: allows the object to move
  * def chase: allows the object to chase the player at a higher speed
  * def position: places the object on the maze
  * def sight: allows the object to see a certain distance
  * def distToPoint: the distance between the object and a certain point
  * def collideWall: when the object collides with the wall, can't pass
  * def collideMazeWall: when the object hits the maze wall
  * def collideRobot: when the object collides with robot
  * def collideZombie: when object collides with another of the same class
  * def biteMan: when the object attacks the player
  * def hurt: when the object gets hit by the player or robot
  * def undead: when the object is dead or living
  * def dropItem: when the object dies, it drops an item
  * def remove: removes the object from the game if not living