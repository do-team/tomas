
def exports_Handler = (event, context, callback):
    import json
    incoming = json.dumps(event)
    valid = json.loads(incoming)

     if valid['operation'] == "sum":
        result = valid['numbera'] + valid['numberb']

    elif valid['operation'] == "sub":
        result = valid['numbera']-valid['numberb']

    elif valid['operation'] == "mult":
        result = valid['numbera']*valid['numberb']

    elif valid['operation'] == "div":
        result = valid['numbera']/valid['numberb']

    else:
        result = "unsupported operation: " + str(valid['operation']) + ", supported operations: \"sum\", \"div\", \"sub\", \"mult\"."

    response = {}
    response['result'] = result

    return (response)
