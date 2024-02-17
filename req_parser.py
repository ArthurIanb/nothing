

def parse_data(req: str):
    i = req.find(' ')
    command = req[:i]
    inf = req[i+1:]
    
    print(command, inf)
    if command == 'calc':
        return str(eval(inf))
    return "ERROR"