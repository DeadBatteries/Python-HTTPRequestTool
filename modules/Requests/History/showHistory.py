
def showHistory(h):
    print("="*80)

    print("RESPONSE HISTORY")

    print("="*80)
    
    if h:
        for item in h:

            print(f"""
{"="*80}
ID:{item["id"]}
URL: {item["url"]}
STATUS: {item["status"]}
LENGTH: {item["length"]}
{"="*80}""")

            

            