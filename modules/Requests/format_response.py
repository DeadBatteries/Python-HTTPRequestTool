def format_b(c):

    if type(c) != int:

        raise TypeError("Function parameter must be INT")
    

    f_list = ["B", "KB", "MB", "GB", "TB"]
        
    for unit in f_list:

        if c < 1024:
                
            return f"{c:.2f} {unit}"
            
        c /= 1024

        


            



