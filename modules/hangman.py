import random, thread
from time import sleep

_in = ''
buf = []
#variable name sweg
the_end = False

def main(s, priv=False):
  global buf
 
  if 'start' in s:
    global the_end
    the_end = True
    sleep(2)
    the_end = False
    n = thread.start_new_thread(game, tuple()) 
    print n
  else:
    global _in
    _in = s
    
    
  while len(buf) == 0:
    pass
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
  
  
  
def game():
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
  words = 'aardvark alpaca antelope baboon badger beaver buffalo butterfly camel chimpanzee chipmunk cobra cougar coyote crane dolphin donkey dragonfly eagle elephant falcon ferret flamingo gecko giraffe goose hawk heron hippopotamus hyena jackal jaguar kangaroo leopard lizard llama mockingbird monkey moose mouse otter panda parrot penguin pigeon porcupine python rabbit raccoon raven reindeer rhinoceros salmon shark sheep sloth snake spider stork squirrel tiger tortoise trout turkey turtle whale wombat woodpecker zebra'.split()

  def getRandomWord(wordList):
     # This function returns a random string from the passed list of strings.
     wordIndex = random.randint(0, len(wordList) - 1)
     return wordList[wordIndex]

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
  secretWord = getRandomWord(words)
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
