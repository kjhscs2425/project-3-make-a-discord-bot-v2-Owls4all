import random
from utility import *
gameState = "not playing"
choice = "none"
fairchoice = 'none'
playerchoice = 'none'
"""**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  global gameState
  if "Frost" in user_message:
    return True
  elif gameState != 'not playing':
    if 'rock' in user_message.lower():
      return True
    elif 'paper' in user_message.lower():
      return True
    elif 'scissors' in user_message.lower():
      return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  global gameState
  global playerchoice
  global fairchoice
  if user_message == 'Frost':
    return "That's me!"
  if "what can you do" in user_message:
    return """I can do lots of things! For instance I can...
    - give a number between 1 and 10
    - play rock paper scissors
    - be annoying
    - and so much more! [aka coming soon]
    """
  if 'give me a number' in user_message:
    choice = random.randint(0,1)
    if choice == 1:
      return "e"
    if choice == 0:
      return "π"
  if 'give me an integer' in user_message:
    return random.randint(1,10)
  if "let's play rock paper scissors" in user_message or "lets play rock paper scissors" in user_message:
    if gameState == 'not playing':
      gameState = 'fair'
      fairchoice = random.choice(['rock','paper','scissors'])
    return "All right. I've chosen something. What will you choose?"+f' gameState={gameState}'
  if gameState == 'cheat':
    if playerchoice == 'rock':
      gameState = 'not playing'
      return "I choose paper."
    if playerchoice == 'paper':
      gameState = 'not playing'
      return "I choose scissors."
    if playerchoice == 'scissors':
      gameState = 'not playing'
      return "I choose rock."
  if gameState == 'player wins':
    if playerchoice == 'scissors':
      gameState = 'not playing'
      return "I choose paper."
    if playerchoice == 'rock':
      gameState = 'not playing'
      return "I choose scissors."
    if playerchoice == 'paper':
      gameState = 'not playing'
      return "I choose rock."
  if gameState == 'fair':
    return f"I choose {fairchoice}."
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
        amIA = word
        amIA.replace('?','')
        if searchList(amIA,['robot','bot','computer','program']):
          return f"I am {state} {amIA}."
        else:
          return f"I am not {state} {amIA}."
  if 'what time is it' in user_message:
    return 'Time for you to get a watch.'
  return "I don't know what that means"
  

# For testing purposes:
'''
username = 'user'
quit = False
while not quit:
  userInput = input('>>>')
  if 'quit' in userInput:
    quit=True
  if should_i_respond(userInput,username):
    print(respond(userInput,username))
  
'''