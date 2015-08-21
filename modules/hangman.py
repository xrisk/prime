import random, thread
from time import sleep
from urllib import urlopen

_in = ''
buf = []
#variable name sweg
the_end = False
read_input = False

def main(s, priv=False):
  global buf
  global _in
  if 'start' in s:
	global the_end
	the_end = True
	buf = []
	_in = ''
	sleep(2)
	the_end = False
	word = [urlopen('http://randomword.setgetgo.com/get.php').read().strip()]
	n = thread.start_new_thread(game, tuple(word))
	print n
  else:
	_in = s


  while len(buf) == False:
	pass
  # read_input = False
  print buf, _in
  cp = buf[:]
  buf = []
  return '\n'.join(cp)


def raw_input():
  global _in
  _in = '$$$'
  #scary magic :6
  while _in == '$$$':
	if the_end == True:
	  import sys
	  sys.exit(0)
	pass
  return _in

def brint(s):
  global buf
  buf.append(s)



def game(word):
  HANGMANPICS = ['''

   +---+
   |   |
   |
   |
   |
   |
  =====''', '''

   +---+
   |   |
   |   O
   |
   |
   |
  =====''', '''

   +---+
   |   |
   |   O
   |   |
   |
   |
  =====''', '''

   +---+
   |   |
   |   O
   |  /|
   |
   |
  =====''', '''

   +---+
   |   |
   |   O
   |  /|\\
   |
   |
  =====''', '''

   +---+
   |   |
   |   O
   |  /|\\
   |  /
   |
  =====''', '''

   +---+
   |   |
   |   O
   |  /|\\
   |  / \\
   |
  =====''']

  def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
	 brint(HANGMANPICS[len(missedLetters)])
	 brint('')

	 if len(missedLetters) == 0:
		brint('Missed letters: None')
	 else:
		brint('Missed letters: ' + ' '.join(missedLetters))

	 blanks = '_' * len(secretWord)

	 for i in range(len(secretWord)): # replace blanks with correctly guessed letters
		 if secretWord[i] in correctLetters:
			 blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

	 brint(' '.join(blanks))

  def getGuess(alreadyGuessed):
	 while True:
		 brint('Guess a letter.')
		 guess = raw_input()
		 guess = guess.lower()
		 if len(guess) != 1:
			 brint('Please enter a single letter.')
		 elif guess in alreadyGuessed:
			 brint('You have already guessed that letter. Choose again.')
		 elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			 brint('Please enter a LETTER.')
		 else:
			 return guess


  brint('H A N G M A N')
  missedLetters = ''
  correctLetters = ''
  secretWord = word
  gameIsDone = False

  while not gameIsDone:
	 displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

	 print secretWord,'ALIBABA AND THE FORTY CHORS'
	 guess = getGuess(missedLetters + correctLetters)
	 if guess in secretWord:
		 correctLetters = correctLetters + guess

		 foundAllLetters = True
		 for i in range(len(secretWord)):
			 if secretWord[i] not in correctLetters:
				 foundAllLetters = False
				 break
		 if foundAllLetters:
			 brint('You win! The word was "' + secretWord + '". You missed '+str(len(missedLetters))+' and guessed '+str(len(correctLetters))+' correct.')
			 gameIsDone = True
	 else:
		 missedLetters = missedLetters + guess


		 if len(missedLetters) == len(HANGMANPICS) - 1:
			 displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
			 brint('You lose. The word was "' + secretWord + '". You missed '+str(len(missedLetters))+' and guessed '+str(len(correctLetters))+' correct.')
			 gameIsDone = True
