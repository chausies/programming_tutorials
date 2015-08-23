"""This program is to make a Rock-Paper-Scissors framework for strategies to play RPS against each other.

"""

ROCK = "rock"
PAP = "paper"
SCIS = "scissors"

from random import random as rand, choice

def random_player():
  """Gives a player that randomly chooses rock, paper, or scissors.

  Returns
  -------
  player : a player function
    A function `player(x)` that, given the last symbol played by the
    opponent, randomly returns rock, paper, or scissors.

  Examples
  --------
  Find the fraction of rocks in 1000 moves by the random player, which
  should be about .3

  >>> player = random_player()
  >>> X = []
  >>> for _ in range(1000):
  ...   x = player(ROCK)
  ...   X.append(x)
  >>> round(X.count(ROCK)/1000.0, 1)
  0.3
  """
  def player(ignored):
    rps = [ROCK, PAP, SCIS]
    return choice(rps)
  return player

def memory_player(T = 10):
  """Gives a player that plays the symbol opposite to the one it's seen the
  most in its memory.

  The memory player keeps track of the last `T` symbols played against it,
  and plays the symbol opposite to the most prevelant one. It's memory is
  initialized to being `T` random symbols.

  Parameters
  ----------
  T : int
    The length of the memory of the player

  Returns
  -------
  player : a player function
    A function `player(x)` that, given the last symbol played by the
    opponent, returns the symbol opposite of the one the opponent has
    played most.

  Examples
  --------
  Play rock against the memory player 3 times, and paper against them 7
  times. Their move after this should be scissors.

  >>> player = memory_player()
  >>> for _ in range(3): _ = player(ROCK)
  >>> for _ in range(7): _ = player(PAP)
  >>> player(PAP) == SCIS
  True
  """
  return "NOT YET IMPLEMENTED"

def best_3_of_5(hist):
  """A win condition for best 3 out of 5.

  Given a the match history of who won, returns -1, 1, or 0 depending on
  whether p1 wins, p2 wins, or no one has won yet.

  Parameters
  ----------
  hist : list
    A list of the history of who's won. -1 indicates p1 won, 1 indicates p2
    won, and 0 indicates a tie.

  Returns
  -------
  winner : -1, 0, or 1
    Who has won the match. -1 indicates p1 won, 1 indicates p2 won, 0
    indicates no one has won yet and the match continues.

  Examples
  --------
  Various examples showing the how the best_3_of_5 win condition evalutes.

  >>> best_3_of_5([1, -1, 1, -1])
  0
  >>> best_3_of_5([0, 0, 0, 0, 0, 0, 0, 0, 0])
  0
  >>> best_3_of_5([1, 1, -1, -1, 1])
  1
  >>> best_3_of_5([1, -1, 1, -1, -1])
  -1
  >>> best_3_of_5([1, 0, -1, 0, 1, 0, -1, 0, 0])
  0
  >>> best_3_of_5([1, 0, -1, 0, 1, 0, -1, 0, 0, 1])
  1
  """
  return "NOT YET IMPLEMENTED"

def tennis_match(hist, sets=2):
  """A win condition that corresponds to a tennis match.

  Ignoring all ties (0's) in `hist`, this is a win condition along the
  lines of a tennis match with `sets` number of sets.The tennis match, of
  course, includes dueces, the win-by-2-games condition, and tie-breaks. 

  Tennis games are first-to-4 wins, win-by-2. This means that the person
  who reaches 4 wins first wins the game, unless he doesn't have 2 more
  points than his opponent. In that case, the players keep playing until
  one of them is ahead by two points, and that player wins the game.
  Example games:
    0 to 0    3 to 1
    1 to 0    3 to 2
    2 to 0    4 to 2
    2 to 1    player 1 wins

    0 to 0    3 to 1    4 to 4    5 to 7
    1 to 0    3 to 2    4 to 5    player 2 wins.
    2 to 0    3 to 3    5 to 5
    2 to 1    4 to 3    5 to 6

  A tennis set is first-to-6 games, win-by-2. This means that the person
  who wins 6 games first wins the set, unless they're not beating the
  opponent by 2 games. If they're not winning by at least 2 games, they
  keep playing until one of them has 2 games over the other, or until both
  players have 6 games. If both players have 6 games in the set, then you
  do a tie-break to see who wins the set.

  A tie-break is final game to decide who wins a set. It's first-to-7 wins,
  win-by-2.

  The first competitor to get `sets` sets wins the whole match.

  Parameters
  ----------
  hist : list
    A list of -1's, 0's, and 1's determining who's been winning which
    rounds. Note that 0's are ignored in a tennis match.

  Returns
  -------
  winner : -1, 0, or 1
    -1 if p1 wins, 1 if p2 wins, or 0 if no one has won yet and the match should continue.

  Examples
  --------
  Plays a 2-set game of tennis 1 point at a time.

  >>> whole_match = [
  ...   0, 0, -1, -1, 1, -1, 1, -1, # p1 wins, 1 - 0
  ...   0, -1, -1, 0, 1, -1, 1, 1, -1, 0, 1, 1, -1, 1, 1, # p2 wins, 1 - 1
  ...   0, 0, -1, -1, 1, -1, 1, -1, # p1 wins, 2 - 1
  ...   0, -1, -1, 0, 1, -1, 1, 1, -1, 0, 1, 1, -1, 1, 1, # p2 wins, 2 - 2
  ...   0, 1, 1, 0, -1, 1, -1, -1, 1, 0, -1, -1, 1, -1, -1, # p1 wins, 3 - 2
  ...   1, 1, 1, 1, # p2 wins, 3 - 3
  ...   -1, -1, -1, -1, # p1 wins, 4 - 3
  ...   -1, -1, -1, -1, # p1 wins, 5 - 3
  ...   1, 1, 1, 1, # p2 wins, 5 - 4
  ...   1, 1, 1, 1, # p2 wins, 5 - 5
  ...   1, 1, 1, 1, # p2 wins, 5 - 6
  ...   -1, -1, 1, -1, -1, # p1 wins, 6 - 6. Enter into tie-breaker
  ...   1, 1, 1, 1, 1, 0, 0, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, # p2 wins the tie-break and the first set.
  ...   -1, -1, -1, -1,
  ...   -1, -1, -1, -1,
  ...   -1, -1, -1, -1,
  ...   -1, -1, -1, -1,
  ...   -1, -1, -1, -1,
  ...   -1, -1, -1, -1, # p1 wins second set
  ...   0, 0, -1, -1, 1, -1, 1, -1, # p1 wins, 1 - 0
  ...   0, -1, -1, 0, 1, -1, 1, 1, -1, 0, 1, 1, -1, 1, 1, # p2 wins, 1 - 1
  ...   0, 0, -1, -1, 1, -1, 1, -1, # p1 wins, 2 - 1
  ...   0, -1, -1, 0, 1, -1, 1, 1, -1, 0, 1, 1, -1, 1, 1, # p2 wins, 2 - 2
  ...   0, 1, 1, 0, -1, 1, -1, -1, 1, 0, -1, -1, 1, -1, -1, # p1 wins, 3 - 2
  ...   1, 1, 1, 1, # p2 wins, 3 - 3
  ...   -1, -1, -1, -1, # p1 wins, 4 - 3
  ...   -1, -1, -1, -1, # p1 wins, 5 - 3
  ...   1, 1, 1, 1, # p2 wins, 5 - 4
  ...   1, 1, 1, 1, # p2 wins, 5 - 5
  ...   1, 1, 1, 1, # p2 wins, 5 - 6
  ...   -1, -1, 1, -1, -1, # p1 wins, 6 - 6. Enter into tie-breaker
  ...   1, 1, 1, 1, 1, 0, 0, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, # p2 wins the tie-break and the whole match
  ...   ]
  >>> match = []
  >>> for i in range(len(whole_match)):
  ...   match.append(whole_match[i])
  ...   if i == len(whole_match) - 1: # If you're on the last point of the match
  ...     print tennis_match(match)
  ...   elif tennis_match(match) != 0: # The match should not be over until the last point
  ...     print "Made an error on point #" + str(i + 1)
  1
  """
  return "NOT YET IMPLEMENTED"

def play_rps(p1 = random_player, p2 = random_player, win_condition="standard", silent = False):
  """Plays a match of RPS with the given player strategies.

  Given two player strategies `p1` and `p2`, makes them play against one
  another until `win_condition` is reached.

  Parameters
  ----------
  p1 : strategy function
    This is a function that, when called, returns a function `s` that
    implements a strategy. `s` should take the last move played by the
    opponent, and return the next move it wants to play.
  p2 : strategy function
    Same as p1, but this represents the strategy for player 2
  win_condition : function of an array or "standard"
    A function that tells if a player has won, or if the match continues.
    Given a list of the match history (e.g. [-1, 1, -1, 0, 0, -1, 1, 1],
    where -1 means p1 wins, 0 means tie, and 1 means p2 wins),
    `win_condition` returns -1 if p1 wins, 1 if p2 wins, or 0 if no one has
    won yet. If "standard", then just goes with the standard rule "best 3
    out of 5".
  silent : Boolean
    Whether you want a blow-by-blow commentary on the match. If True, then
    `play_rps` won't print a thing and will just return the winner. Else,
    the result of every round will be printed out.

  Returns
  -------
  winner : int
    The winner of the match. -1 for p1, 1 for p2.

  Examples
  --------
  Make a rock-playing and a paper-playing player fight a first-to-10 match.

  >>> play_rock = lambda : lambda x : ROCK
  >>> play_paper = lambda : lambda x : PAP
  >>> win_condition = lambda hist : \\
  ...      1 if hist.count(1)>10 else -1 if hist.count(-1)>10 else 0
  >>> play_rps(play_rock, play_paper, win_condition, True)
  1
  >>> play_rps(play_paper, play_rock, win_condition, True)
  -1
  """
  if win_condition == "standard":
    win_condition = best_3_of_5
  return "NOT YET IMPLEMENTED"
 
# The code inside this if-clause is run when `python rps.py` is called from
# the command-line.k
if __name__ == "__main__":
  play_rps()
