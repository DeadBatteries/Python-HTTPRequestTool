from modules.Requests.History.history import history
from modules.Requests.format_response import format_b
from modules.Requests.previewHeaders import preview_header

def addToHistory(r):

    if r == False:
        print("Cannot Add Blank-Object to history")
        return None
    
    item = {

        "id":len(history)+1,
        "url":{r.url},
        "status":r.status_code,
        "headers":preview_header(r.headers),
        "encoding":r.encoding,
        "length":format_b(len(r.content)),
        "response":r
    
    }


    history.append(item)

    

    
