import funcs

def parse_request(req):
    # return command and args
    i = req.find(' ')
    if i == -1:
        return req, "all"
    command = req[:i]
    inf = req[i+1:].strip()
    return command, inf


def response(req: str):
    command, inf = parse_request(req)
    if not inf:
        return "no inf"
    if command == 'calc':
        return str(eval(inf))

    if command == 'echo':
        return inf

    if command == 'add':
        return funcs.create_user_command(inf)
    
    if command == 'get':
        return funcs.get_user_command(inf)
    
    if command == "rem":
        return funcs.remove_user_command(inf)
    
    if command == "flush":
        return funcs.flush_bd(inf)
    
    return "Wrong command"

