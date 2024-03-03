import sqlalchemy

def parse_request(req):
    # return command and args
    i = req.find(' ')
    command = req[:i]
    inf = req[i+1:]
    return command, inf


def response(req: str):
    command, inf = parse_request(req)

    if command == 'calc':
        return str(eval(inf))

    if command == 'echo':
        return inf

    if command == 'add':
        ...

    return "ERROR"

