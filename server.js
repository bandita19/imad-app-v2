var express = require('express');
var morgan = require('morgan');
var path = require('path');

var app = express();
app.use(morgan('combined'));

var articles = {
    'article-one':{
                title: "Article One | Bandita",
                head: "Article One",
                content:`
                    <p>
                        My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.
                    </p>
                    <p>
                        My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.
                    </p>
                    <p>
                        My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.My Article One.
                    </p>`
    },
    'article-two':{
                title: "Article Two | Bandita",
                head: "Article Two",
                content:`
                        My Article Two.`
    },
    'article-three':{
                title: "Article Three | Bandita",
                head: "Article Three",
                content:`
                        My Article Three.`
    },
};
function createTemp(data){
    var title=data.title;
    var head=data.head;
    var content=data.content;
    
    var htmltemp=`
    <html>
        <head>
            <title>
                ${title}
            </title>
            <meta name="viewport" content="width=device-width, initial-scale-1">
            <link href="/ui/style.css" rel="stylesheet" />
        </head>
        <body>
            <div class="head">
            <h1>${head}</h1>
            </div>
            <hr>
            <div class="content">
            ${content}
            </div>
        </body>
    </html>
    `;
}
app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname, 'ui', 'index.html'));
});
var counter=0;
app.get('/counter', function(req,res) {
    counter=counter + 1; 
    res.send(counter.toString());
});
app.get('/test-db',function(req,res){
    // make a select request 
    //return a response with the results
});

var names = [];
aap.get('submit-name', function(res,req) {
    //Get the name from the request
    var name = req.query.name;//1000
    
    names.push(name);
    // JSON: Javascript Object Notation
    
    res.send(JSON.stringify(names)); //1000
});


app.get('/:articleName', function (req, res) {
 var articleName=req.params.articleName;
 res.send(createTemp(articleName));
});

app.get('/ui/style.css', function (req, res) {
  res.sendFile(path.join(__dirname, 'ui', 'style.css'));
});

app.get('/ui/main.js', function (req, res) {
  res.sendFile(path.join(__dirname, 'ui', 'main.js'));
});



var port = 8080; // Use 8080 for local development because you might already have apache running on 80
app.listen(8080, function () {
  console.log(`IMAD course app listening on port ${port}!`);
});
