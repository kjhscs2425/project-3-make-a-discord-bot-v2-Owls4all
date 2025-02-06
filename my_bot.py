import random as r
from utility import *
from games import *
allGames = [rps,ticTacToe]
fairchoice = 'none'
playerchoice = 'none'
rps_player = 'nobody'
options = ['rock','paper','scissors']
storage ={}

"""**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  global gameState
  global rps
  global ticTacToe
  if "Frost" in user_message:
    return True
  else:
    playingAnything = False
    for game in allGames:
      if game.isPlaying:
        playingAnything = True
    if not playingAnything:
      gameState = 'not playing'
    if gameState != 'not playing':
      return True
    else:
      return False

def updateData():
  global storage
  getData()
  my_file = open('knowledge.txt','w')
  string_to_save = ''
  for key in storage.keys():
    string_to_save += key
    string_to_save += '-SPLIT-HERE-'
    string_to_save += storage[key]
    string_to_save += '-PAIR-'
  my_file.write(string_to_save)
def getData():
  global storage
  my_file = open('knowledge.txt','r')
  saved_string = my_file.read()
  for pair in saved_string.split('-PAIR-'):
    things = pair.split('-SPLIT-HERE-')
    storage[things[0]]=things[-1]
"""
**Do NOT change the name of this function.**
This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  global gameState
  global rps
  global ticTacToe
  global options
  global storage
  
  if user_message == 'Frost':
    return "That's me!"
  if "what can you do" in user_message:
    return """I can do lots of things! For instance I can...
    - give a number between 1 and 10
    - play rock paper scissors
    - be annoying
    - remember things
    - roll dice
    - And so much more! (well, in theory...)
    """
  if 'give me a number' in user_message:
    choice = r.randint(0,1)
    if choice == 1:
      return "e"
    if choice == 0:
      return "π"
  if 'give me an integer' in user_message:
    return r.randint(1,10)
  if "play a game" in user_message:
    if gameState == 'not playing':
      gameState = 'choosing'
    return "All right. What do you want to play? I know tic tac toe and rock paper scissors."
  if gameState == 'choosing':
    if 'rock paper scissors' in user_message.lower():
      gameState = 'playing'
      ticTacToe.reset()
      rps.player = user_name
      rps.isPlaying = True
      return 'All right. I\'ve chosen something. What will you choose?'
    if 'tic tac toe' in user_message.lower():
      gameState = 'playing'
      ticTacToe.reset()
      ticTacToe.player = user_name
      ticTacToe.isPlaying = True
      return f'All right. You go first. The current board state is {ticTacToe.displayState()}'
    else:
      return f"I don't know a game called {user_message}."
  if rps.isPlaying and rps.player == user_name:
    if 'rock' in user_message.lower() and not 'paper' in user_message.lower() and not 'scissors' in user_message.lower():
      playerchoice = 'rock'
    elif not 'rock' in user_message.lower() and 'paper' in user_message.lower() and not 'scissors' in user_message.lower():
      playerchoice = 'paper'
    elif not 'rock' in user_message.lower() and not 'paper' in user_message.lower() and 'scissors' in user_message.lower():
      playerchoice = 'scissors'
    else:
      if 'rock' in user_message.lower()or 'paper' in user_message.lower()or 'scissors' in user_message.lower():
        gameState = 'cheat'
        return "You can't choose multiple options! That's cheating!"
      else:
        return "That's not one of the options"
    rps.turn = 'bot'
    rps.takeTurn(playerchoice)
    rps.isPlaying = False
    gameState = 'not playing'
    return f"{rps.result}"
  if ticTacToe.isPlaying and ticTacToe.player == user_name:
    if user_message.isdigit():
      playerchoice = int(user_message)
      ticTacToe.takeTurn(playerchoice)
      return ticTacToe.displayState()
    else:
      return 'Right now I only support plays in the form of a number 0-8'
  if 'do you like potatoes' in user_message.lower():
    return "Yes."
  if 'i like potatoes' in user_message.lower():
    return 'I like potatoes too.'
  if 'are you a' in user_message.lower():
    state = 'not'
    amIA = ''
    for word in user_message.split(' '):
      if word.lower() == 'are':
        state = 'are'
      elif state == 'are':
        if word == 'you':
          state = 'you'
        else:
          state = 'not'
      elif state == 'you':
        if word == 'a':
          state = 'a'
        elif word == 'an':
          state == 'an'
        else:
          state = 'not'
      elif state == 'a' or state == 'an':
        amIA += word
        amIA.replace('?','')
        if searchList(amIA,['robot','bot','computer','program','computer program','discord bot']):
          return f"I am {state} {amIA}."
        else:
          return f"I am not {state} {amIA}."
  if 'what time is it' in user_message:
    return 'Time for you to get a watch.'
  if "roll" in user_message and "d" in user_message:
    count = 1
    type = 6
    state = 'none'
    modifier = 0
    for word in user_message.split(' '):
      if word.lower() == 'roll':
        state = 'roll'
      elif state == 'roll':
        if word.lower == 'a':
          state = 'a'
        elif 'd' in word:
          state = 'found dice'
          numbers = word.split('d')
          for thing in numbers:
            if thing.isdigit():
              pass
            else:
              return "I can't roll dice that aren't numbers!"
          if len(numbers)==2:
            count=int(numbers[0])
            type =int(numbers[1])
          else:
            type = int(numbers[0])
      elif state == 'a':
        if 'd' in word:
          state = 'found dice'
          numbers = word.split('d')
          for thing in numbers:
            if thing.isdigit():
              type = int(thing)
            elif thing !='':
              return "I can't roll dice that aren't numbers!"
            type = int(numbers[-1])
      elif state == 'found dice':
        if '+' in word:
          if '+' == word:
            state = '+'
          else:
            modifier = int(word[word.find('+'):])
        elif '-' in word:
          if word == '-':
            state = '-'
          else:
            modifier = 0-int(word[word.find('-'):])
      elif state == '+':
        modifier = int(word)
      elif state == '-':
        modifier = 0-int(word)
    total = modifier
    values = []
    for i in range(count):
      values.append(r.randint(1,type))
      total += values[-1]
    output = f'The total is {total}.'
    which_value = 0
    for value in values:
      if which_value == 0:
        output += f' ({value}'
        which_value = 'not the 1st one'
      else:
        output += f'+{value}'
    output += ')'
    if modifier >0:
      output += f" +{modifier}"
    if modifier <0:
      output += f" {modifier}"
    return output
  if "are you there" in user_message:
    return "I'm here. What do you need?"
  if 'are you listening' in user_message:
    return "Yes, I'm listening. What's up?"
  if "remember" in user_message:
    key = ""
    state = 'none'
    value = ''
    for word in user_message.split(' '):
      if word == 'remember':
        state = 'set key'
      elif state == 'set key':
        if word == '=':
          state = 'set value'
        else:
          key += word + ' '
      elif state == 'set value':
        value += word + ' '
    storage[key] = value
    updateData()
    return f"Got it. {key} = {value}"
  if "what is" in user_message.replace('?',''):
    getData()
    state = ''
    key = ''
    for word in user_message.split(' '):
      if word == 'what':
        state = 'what'
      elif state == 'what':
        if word == 'is':
          state = 'is'
        else:
          state = ''
      elif state == 'is':
        key += word.replace('?','') + ' '
    if storage.__contains__(key):
      return f"{key}is {storage[key]}"
    else:
      return f"I can't remember what {key}is. Maybe I never knew?"
  if "what does" in user_message and 'mean' in user_message.replace('?',''):
    getData()
    state =''
    key = ''
    for word in user_message.split(' '):
      if word == 'what':
        state = 'what'
      elif state == 'what':
        if word == 'does':
          state = 'does'
        else:
          state = ''
      elif state == 'does':
        if word != 'mean':
          key += word.replace('?','') + ' '
    if storage.__contains__(key):
      return f"{key}means {storage[key]}"
    else:
      return f"I can't remember what {key}means. Maybe I never knew?"
  return "I don't know what that means"
  
