[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17886570&assignment_repo_type=AssignmentRepo)
Make a discord bot!

# Instructions  

## Step 1: Setup

1. [Create a bot in discord and get a token](https://web.archive.org/web/20230314183120/https://docs.replit.com/tutorials/python/build-basic-discord-bot-python#creating-a-bot-in-discord-and-getting-a-token)
2. Add your tokens to `secret.py`
2. [Set ALL permissions to ON](https://web.archive.org/web/20230314183120/https://docs.replit.com/tutorials/python/build-basic-discord-bot-python#privileged-gateway-intents)
3. [Add your bot to the server](https://docs.replit.com/tutorials/python/build-basic-discord-bot-python#adding-your-discord-bot-to-your-discord-server)
4. Make a channel for your bot
5. Add your bot to your bot channel

## Step 2: Programming

Modify the two functions in `my_bot.py`.

The `should_i_respond` function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users

The `respond` function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users

### Requirements

* Your code should use the following methods:
    * [ ] `.lower()`, `.upper()`, and/or `.capitalize()`
    * [ ] `.replace()`
* [ ] You should iterate through at least one string using a `for` loop
* [ ] You should use string string indexing (e.g. `my_string[3]`) and/or string slicing (e.g. `my_string[3:6]`)
* [ ] Your code should use at least one function from the `random` library
* [ ] Your bot should respond to at least 10 different messages that a user in your discord channel might send
