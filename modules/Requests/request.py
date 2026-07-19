import requests
from modules.Requests.format_response import format_b

def get_r():

    try:

        url = input("URL: ")
        r = requests.get(url, timeout=10)  
        r.raise_for_status()

        content_len = len(r.content)

        print(f"""
              
        URL: {r.url}

        Status Code: {r.status_code}

        Encoding: {r.encoding}
       
        Response-length: {format_b(content_len)}

        """)

    #Error Handling:
    except TypeError as error:
        print("ERRO: ! Invalid Data Type !")
        print(error)

    except requests.exceptions.HTTPError as error: 

        print("ERROR: ! Http Error !")
        print(error.args[0])

    except requests.exceptions.ConnectTimeout as error:

        print("ERROR: ! Connection TimeOut !")
        print(error.args[0])

    except requests.exceptions.ConnectionError as error:

        print("ERROR: ! Connection Error !")
        print(error.args[0])

    except requests.exceptions.ContentDecodingError as error:

        print("ERROR: ! Content-Decoding Error !")
        print(error.args[0])

    except requests.exceptions.TooManyRedirects as error:

        print("ERROR: ! Too Many Redirects !")
        print(error.args[0])

    except requests.exceptions.Timeout as error:

        print("ERROR: ! TimeOut !")
        print(error.args[0])

    except requests.exceptions.InvalidHeader as error:

        print("ERROR: ! Invalid Header !")
        print(error.args[0])

    except requests.exceptions.InvalidURL as error:

        print("ERROR: ! Invalid URL !")
        print(error.args[0])

    except requests.exceptions.JSONDecodeError as error:

        print("ERROR: ! JSON Decode Error !")
        print(error.args[0])

    except requests.exceptions.MissingSchema as error:

        print("ERROR: ! Missing SCHEMA ! ")
        print(error.args[0])

    except requests.exceptions.InvalidSchema as error:

        print("ERROR: ! Invalid SCHEMA ! ")
        print(error.args[0])

