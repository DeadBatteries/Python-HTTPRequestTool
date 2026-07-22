from modules.Utils.selectOptions import select_number
from modules.Requests.Headers.showHeaders import showHeaders


def requestOptions(item):

    while True:

        print(f"""
Request Options:
          
1-Show Headers
0-Back     
""")
    
        choice = select_number()

        match choice:

            case 1:
                
                showHeaders(item)
                break

            case 2:
                
                break

