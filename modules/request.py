import requests
from modules.format_response import format_b

def get_r(url):

    try:

        r = requests.get(f"{url}'")     
        content_len = len(r.content)

        print(f"""
              
        URL: {r.url}

        Status Code: {r.status_code}

        Encoding: {r.encoding}
       
        Response-length: {format_b(content_len)}

        """)

    except requests.exceptions: 

        print("Error")



