def preview_header(r, limit=3):

    count = 0

    for key, value in r.items():

        print(f"{key}, {value}")

        count += 1 

        if count >= limit:
            break
