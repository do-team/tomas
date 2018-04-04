#Kalkulacka do AWS

exports.handler = (event, context, callback) => {

print(event)
A = event.numbera
B = event.numberb
C = 0
operation = event.operation
response = {
    "result": null,
    "numbera": A,
    "numberb": B,
    "operation": operation
    }


#operators

if operation == "*":
    C = ('{} * {} ='.format(A, B)
    response.result = C

elif operation == "/":
    C = ('{} / {} ='.format(A, B)
    response.result = C

elif operation == "+":
    C = ('{} + {} ='.format(A, B)
    response.result = C

elif operation == "-":
    C = ('{} - {} ='.format(A, B)
    response.result = C

  callback(null, response);
}
