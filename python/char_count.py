def char_count(str):

    dict = {}
    for n in str:
        key = dict.keys()
        if n in key:
            dict[n] += 1
            
        else:
            dict[n] = 1
            
    return dict
    


