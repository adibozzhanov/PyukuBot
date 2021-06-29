import requests
from decorators import message

description = "shows the contributors of the bot"


@message
def main():
    try:
        resp = requests.get(
            "https://api.github.com/repos/adibozzhanov/PyukuBot/contributors?anon=1"
        )
        resp.raise_for_status()
    except requests.HTTPError:
        return "Error. Github API cannot be accessed."
    else:
        data = resp.json()
        contributors = [user["login"] for user in data]
        if len(contributors) == 1:
            return "The contributor to PyukuBot is" + contributors[0] + "."
        return ("The contributors to PyukuBot are " +
                ", ".join(contributors[:-1]) + " and " + contributors[-1] +
                ".")
