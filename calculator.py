#Kalkulacka do AWS

print (event)
A = event.numbera
B = event.numberb
C = 0
operation = event.operation
response = {"result": null,
           "numbera": A,
           "numberb": B,
           "operation": operation}

div_trigger = A / B
mult_trigger = A * B
add_trigger = A + B
sub_trigger = A - B

if operation == "mult":
  C = mult_trigger
  response.result = C

elif operation = "div":
  C = div_trigger
  response.result = C

elif operation = "add":
  C = add_trigger
  response.result = C  

elif operation = "sub":
  C = sub_trigger
  response.result = C
