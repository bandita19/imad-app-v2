//Counter code
var button = document.getElementById('counter');
button.onclick = function () {
    
    //Create a request
    var request = new XMLHttpRequest();
    
    //Capture the response and store it in a variable
    request.onreadystatechange = function () {
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
    request.send(null);
};

//Submit name
var nameInput = document.getElementById('name');
var name = nameInput.value;
var submit = document.getElementById("submit_btn");
submit.onclick = function () {
    //Make a request to the server and send the name
    //Capture the list of names and render it as a list
    var names = ['names1', 'names2', 'names3', 'name4'];
    var list = '';
    for(var i=0; i<names.length; i++){
        list += '<li>' + names[i] + '</li>';
    }
    var ul = document.getElementById("namelist");
    ul.innerHTML = list;
    
};