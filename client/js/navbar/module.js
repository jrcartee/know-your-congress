define(function(require) {
    var App = require('app/module'),
        Controller = require("navbar/controller");

    console.log("Navbar Initializing")

    return App.module("Navbar", function(Navbar, App, BB, M) {
        Navbar.on("start", function() {
            console.log("Navbar Started");
        });
        Navbar.controller = new Controller();
    });
});