import sys
from renderoo.colors import COLORS, CEND
from renderoo.client import RenderooCommandLineClient


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f'{COLORS.get("error")}Please pass a valid argument or pass the argument "help" to learn more. {CEND}')
        exit()

    client = RenderooCommandLineClient(sys.argv[1])
    client.run_action()