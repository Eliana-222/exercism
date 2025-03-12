def eat_ghost(power_pellet_active, touching_ghost): 
    return power_pellet_active and touching_ghost
 # function that takes two parameters (if Pac-Man has a power pellet active and if Pac-Man is touching a ghost) and returns a Boolean value if Pac-Man is able to eat a ghost.
def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot
  #shows how pacman could potentially score, and returns boolean variable 
def lose(power_pellet_active, touching_ghost):
     return not power_pellet_active and touching_ghost
#if pacman is touching a ghost he dies and if he doesn't have an active pallet he dies 
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
   return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
#pacman wins 
