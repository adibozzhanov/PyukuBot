# driver code
from pyuku import Pyuku


if __name__ == "__main__":
    try:
        with open(".token", "r") as tokenFile:
            token = tokenFile.readline().strip()
            Pyuku(token)

    except IOError:
        print("No token file detected.")

