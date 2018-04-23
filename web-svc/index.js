"use strict";

var express = require("express");
var app = express();
var hb = require("express-handlebars").create({defaultLayout: "main"});

app.engine("handlebars",hb.engine);
app.set("view engine","handlebars");

app.get("/",function(req,res){

    res.render("home");
});

app.get("/login",function(req,res){

    res.redirect("login");
});
app.get("/registrar",function(req,res){

    res.render("registrar");
});

app.get("/main",function(req,res){
    res.render("main");
});

var server = app.listen(8080, "127.0.0.1", function(){
    var host = server.address().address;
    var port = server.address().port;
    console.log("lintening at http://%s:%s", host, port);

});