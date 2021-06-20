# PyukuBot
A telegram bot that can do stuff...

It can do all sorts of random things. 

Add it to your telegram group chat and some of the features will definitely brighten up your group chat.

# Contributing
You can contribute to the pyuku bot in multiple ways. Generally, any sort of feature supported by a new command is very much pleased. 


## Adding a new command

If you want to add a new command for the bot to support, add a new `nameofyourcommand.py` file in `/src/commands` directory.

The format of the command file.

 - The file MUST contain a `main` function that takes in parameters depending on the chosen decorator
 
 - The `main` function MUST use one of the predefined decorators. See next section on what decorators are available.
 
 - The file MUST contain a `description` variable declared at the outer most scope, that has a short description of the command. 
 
