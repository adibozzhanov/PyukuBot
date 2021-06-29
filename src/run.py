# driver code
import os
from pyuku import Pyuku

if __name__ == "__main__":
    env = os.environ
    if "BOT_TOKEN" in env:
        token = env["BOT_TOKEN"]
        Pyuku(token)
    else:
        print("There is no token present")
