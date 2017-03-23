//Counter code
var button = document.getElementById('counter');
button.onclick = function () {
    
    //Create a request
    var request = new XMLHttpRequest();
    
    //Capture the response and store it in a variable
    reques.onreadystatechange = function () {
        if (request.readyState === XMLHttpRequest.DONE) {
            // TAKE SOME ACTION
            if (request.status === 200) {
                var counter = request.responseText;
                var span = document.getElementById('count');
                span.innerHTML = counter.toString();
            }
        }
    };
    //Make a request to the counter endpoint.
    request.open('GET' , 'http://bandita19.imad.hasura-app.io/counter' , true);
    request.send(NULL);
};