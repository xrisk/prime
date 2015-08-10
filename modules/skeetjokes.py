s = """
Jon Skeet is immutable. If something's going to change, it's going to have to be the rest of the universe. 
Jon Skeet's addition operator doesn't commute; it teleports to where he needs it to be.
Anonymous methods and anonymous types are really all called Jon Skeet. They just don't like to boast.
Jon Skeet's code doesn't follow a coding convention. It is the coding convention.
Jon Skeet doesn't have performance bottlenecks. He just makes the universe wait its turn.
Jon Skeet is the only person who has ranked higher than Jon Skeet in the SO all-time rep league.
Users don't mark Jon Skeet's answers as accepted. The universe accepts them out of a sense of truth and justice. 
Jon Skeet can divide by zero.
Jon Skeet's SO reputation is only as modest as it is because of integer overflow (SQL Server does not have a datatype large enough)
Jon Skeet is the only top 100 SO user who is human. The others are bots that he coded to pass the time between questions.
Jon Skeet coded his last project entirely in Microsoft Paint, just for the challenge.
Jon Skeet does not use exceptions when programming. He has not been able to identify any of his code that is not exceptional.
When Jon Skeet's code fails to compile the compiler apologises.
Jon Skeet does not use revision control software. None of his code has ever needed revision.
When you search for "guru" on Google it says "Did you mean Jon Skeet?"
There are two types of programmers: good programmers, and those that are not Jon Skeet.
Jon Skeet can recite pi. Backwards.
Jon Skeet once answered one of my questions 42 seconds before I asked it. It is my belief that he employed a super computer and Infinite Improbability Drive technology to achieve this result.
When Jon Skeet points to null, null quakes in fear.
Donald Knuth wears a "Jon Skeet is my Homeboy" t-shirt to show off at parties.
Jon Skeet is the traveling salesman. Only he knows the shortest route.
Jon Skeet can make the Kessel run in under twelve parsecs.
Jon Skeet took the red pill and the blue pill, and can phase-shift in and out of the Matrix at will.
Jon Skeet has root access to your system.
The Dining Philosophers wait while Jon Skeet eats.
Jon Skeet knows the air speed velocity of an unladen swallow, both African and European.
Jon Skeet has more "Nice Answer" badges than you have badges.
Jon Skeet saved the Princess.
Jon Skeet can ask a question that even Jon Skeet can't answer. And he can answer it, too.
When Jon Skeet gives a method an argument, the method loses.
When Jon Skeet pushes a value onto a stack, it stays pushed.
There is no 'CTRL' button on Jon Skeet's computer. Jon Skeet is always in control.
The only time Jon Skeet was wrong was when he thought he had made a mistake.
Jon Skeet does not run his programs. He just whispers, "You better run."
"""

l = s.split('\n')
from random import choice

def main(s, priv=False):
	return choice(l)

