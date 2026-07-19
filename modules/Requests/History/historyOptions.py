from utils.selectOptions import select_number
from modules.Requests.History.history import history
from modules.Requests.History.showHistory import showHistory

def historyOptions():

    while True:

        print(f"""
    {"="*20}
    History Options:
    {"="*20}
    1-Select Item (By ID)
    0-Back
""")

        choice = select_number()

        match choice:

            case 1:

                id = int(input("ID: "))
                g = get_history_by_id(id)
                showHistory([g])

            case 0:
                break



def get_history_by_id(id):

    for item in history:

        if item["id"] == id:
            return item
        
    return None