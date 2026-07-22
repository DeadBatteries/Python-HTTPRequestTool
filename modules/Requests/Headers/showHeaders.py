def showHeaders(item):

    h = item["headers"]
    print("="*80)   
    print("Headers")    
    print("="*80)
     
    for key, value in h.items():
    
        print(f"{key:<25}:{value}")