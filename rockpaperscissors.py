import random
import os
import re
os.system('cls' if os.name == 'nt' else 'clear')


while(1 < 2):
  print "Rock, Paper, Scissors, Shoot!"
  uChoice = raw_input("Choose your weapon -- [R]ock, [P]aper, or [S]cissors: ")
  if not re.match("[SsRrPp]", uChoice):
    print "Please choose a letter: "
    print "Rock, Paper, or Scissors: "
    continue
  print "You Chose " + uChoice.upper()
  
  
  choices = ['R', 'P', 'S']
  cpuChoice = random.choice(choices)
  cpuWordChoice = cpuChoice
  print "CPU Chose " + cpuWordChoice
  
  
  
  
  if cpuChoice == str.upper(uChoice):
    print "It's a tie!"
    continue
  elif cpuChoice == 'R' and uChoice.upper() == 'P':
    print "You Win!"
    continue
  elif cpuChoice == 'R' and uChoice.upper() == 'S':
    print "You Lose!"
    continue
  elif cpuChoice == 'P' and uChoice.upper() == 'R':
    print "You Lose!"
    continue
  elif cpuChoice == 'P' and uChoice.upper() == 'S':
    print "You Win!"
    continue
  elif cpuChoice == 'S' and uChoice.upper() == 'P':
    print "You Lose!"
    continue
  elif cpuChoice =='S' and uChoice.upper() =='R':
    print "You Win!"
    continue
  else:
    print "Something Happened! I'm Sorry, shutting down..."
