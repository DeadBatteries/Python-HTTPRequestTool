from modules.Utils.selectOptions import select_number
from modules.Requests.History.history import history
from modules.Requests.History.showHistory import showHistory
from modules.Requests.requestOptions import requestOptions

def historyOptions():

    while True:

        print(f"""
{"="*80}
History Options:
{"="*80}
1-Show History
2-Select Item (By ID)
0-Back
""")

        choice = select_number()

        match choice:

            case 1:

                showHistory(history)

            case 2:

                id = int(input("ID: "))
                g = get_history_by_id(id)

                showHistory([g])

                requestOptions(g)


            case 0:

                break



def get_history_by_id(id):

    for item in history:

        if item["id"] == id:
            return item
        
    return None

def get_item_by_param(param):

    for item in history:

        if item[f"{param}"] == param:
            return item

    return None