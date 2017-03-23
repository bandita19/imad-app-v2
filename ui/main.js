//Counter code
var button = document.getElementById('counter');
button.onclick = function () {
    
    //Make a request to the counter endpoint.
    var request = new XMLHttpRequest();
    
    //Capture the response and store it in a variable
    reques.onreadystatechange = function () {
        if (request.readyState === XMLHttpRequest.DONE) {
            // TAKE SOME ACTION
            if (request.status === 200) {
                var counter = request.response.Text;
                var span = document.getElementById('count');
                span.innerHTML = counter.toString();
                
            }
        }
        //NOT DONE YET
    };
};