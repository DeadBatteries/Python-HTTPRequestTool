from modules.Requests.request import get_r
from modules.interaction.interface import appInterface
from utils.selectOptions import select_number
import sys

def initApp():
    try:

        appInterface()

        choice = select_number()

        match choice:

            case 1:
                get_r()
            case 0:
                print("Returning to the base...Farewell!")
                sys.exit(0)

    except TypeError as error:

        print(error)


initApp()


