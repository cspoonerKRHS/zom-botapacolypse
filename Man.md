# Description #
Player character (You!) that has to escape the maze


## Controls ##
  * **W** to move up
  * **S** to move down
  * **A** to move left
  * **D** to move right
  * **Space** to use weapons (see [Stick](Stick.md))

## Attributes ##
  * life bar: shows health of man
  * rect: shape and hitbox
  * surface: the sprite that you see
  * position: where he starts in the maze
  * hurt: when the object is attacked, and hit
  * speed: two part list with x and y in integers
  * attack: calls on weapon objects to use
## Methods ##
  * def init: creates the object and the attributes
  * def position: places the man in the maze
  * def collide maze wall: when he collides with the walls
  * def collide zombie: damages the man
  * def collide robot: collides with robot, no damage
  * def collide wall: collides with the side of the window
  * def collide stick: collides with stick in order to pick it up
  * def collide Stun Gun: collides with stun gun in order to pick it up
  * def collide taser: collides with taser in order to pick it up
  * def collide pistol: collides with pistol in order to pick it up
  * def pickUpStick: picks up stick if he collides with it
  * def pickUpStunGun: picks up stun gun if he collides with it
  * def pickUpTaser: picks up taser if he collides with it
  * def pickUpPistol: picks up pistol if he collides with it
  * def attackWithStick: attacks with weapon
  * def attackWithStunGun: attacks with weapon
  * def attackWithTaser: attacks with weapon
  * def attackWithPistol: attacks with weapon
  * def hurt: used by other methods to cause damage
  * def dead: man dies in the game
  * def remove: removes man from the game when he dies