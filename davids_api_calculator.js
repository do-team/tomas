exports.handler = (event, context, callback) => {
    console.log(event);
    let A = event.numbera;
    let B = event.numberb;
    let C = 0;
    let operation = event.operation;
    let response = {
        "result": null,
        "numbera": A,
        "numberb": B,
        "operation": operation
    }

    switch(operation) {
    case "mult":
        C = A * B;
        response.result = C;
        break;
    case "div":
        C = A / B;
        response.result = C;
        break;
    case "sum":
       C = A + B;
       response.result = C;
    break;
    case "sub":
       C = A - B;
       response.result = C;
    break;
    default:
        response = {
            "result": "Unsupported operation!"
        }
}

    callback(null, response);
};
