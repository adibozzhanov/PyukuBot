# PyukuBot
A telegram bot that can do stuff


# Commands Format

This section describes the format of creating a new command.
A script will iterate over the contents of the file and initialise all commands for the bot to support it.

 - All commands are stored in the `src/commands` directory.

 - Each command has it's own `.py` file.
 
 - The name of the file MUST be of the format `commandname.py`
 
 - A command MUST NOT contain any characters but lowercase alphabet.
 
 - A command SHOULD NOT be long
 
 - A command file MUST contain a function with the same name as the filename
 
	 - Sample command file template `mycommand.py`
	 ```python
	 
	 # This will be shown in the help section of the bot when user types /help
	 description = "This is a good description of my command"
	 
	 # the function name will be converted into a command
	 # user would have to type /mycommand to trigger this function.
	 def mycommand(update, context):
		 chat_id = update.message.chat.id
		 
		 response = "" 
		 
		 # code goes here...
		 # do some magic to the response text
		 
		 bot.sendMessage(chat_id = chat_id, text = response)
	 
	 
	 ```

 - A command file MUST contain a variable `description` declared, where the description of the command is stored.
 
 
