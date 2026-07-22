from modules.Requests.request import get_r
from modules.Interface.interface import appInterface, appBanner
from modules.Utils.selectOptions import select_number
from modules.Requests.History.addToHistory import addToHistory
from modules.Requests.History.history import history
from modules.Requests.History.showHistory import showHistory
from modules.Requests.History.historyOptions import historyOptions

def showBanner():
    appBanner()
    
def initApp():

    while True:

        try:

            appInterface()

            choice = select_number()

            match choice:

                case 1:
                    r = get_r()
                    
                    if r:
                        addToHistory(r)
                        
                case 2:
                    
                    showHistory(history)
                    historyOptions()

                case 0:
                    print("Returning to the base...Farewell!")
                    break

        except TypeError as error:

            print(error)

appBanner()
initApp()


