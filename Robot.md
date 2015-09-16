# Description #

An enemy character that wanders through the maze. It can shoot and will chase the man if it sees him. The robot will attempt to kill the man but the man is also able to kill the robot. It will also try to kill zombies.

The Robot is an enemy in the game.

# Attributes #

  * Speed: two part list with x and y in integers
  * Place: beginning position in the game
  * Rect: the basic length and width, in square, of the surface
  * Surface: the part that can be seen
  * Sight: the area in which the object can see something
  * Shoot: The object shoots electricity in order to hurt and kill
  * Hurt: when the object is attacked, and hit
  * Dead: whether the object is there or not
  * lifebar: gives the object health


# Methods #

  * def init: creates the object and allows it to have the attributes
  * def move: allows the object to move
  * def place: places the object on the maze
  * def sight: allows the object to see a certain distance
  * def distToPoint: the distance between the object and a certain point
  * def wallCollide: when the object collides with the wall, can't     pass
  * def collideRobot: when the object collides with another of same class
  * def shootElect: when the object attacks the player
  * def hurt: when the object gets hit by the player
  * def dropItem: when the object dies, it drops an item
  * def remove: removes the object from the game if not living