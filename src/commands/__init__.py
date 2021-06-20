from os import walk
from importlib import import_module

f = []
commands = {}


# Make a list of command names
for (dirpath,dirnames,filenames) in walk("commands"):
    if dirpath == "commands":
        f.extend(filenames)
f.remove("__init__.py")

# Import each of them and populate the commands dictionary
for each in f:
    cm = each[:len(each)- 3] # Truncate the .py at the end
    module = import_module(f".{cm}", "commands")
    commands[cm] = module.main, module.description
