
def exports_Handler = (event, context, callback):
    import json
    incoming = json.dumps(event)
    valid = json.loads(incoming)


    result = valid['numbera'] + valid['numberb']

    response = {}
    response['result'] = result

    return (response)
