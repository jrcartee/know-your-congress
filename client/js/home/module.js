define(function (require) {
    var App = require('app/module'),
        Controller = require('home/controller');

    console.log("Home initializing");

    return App.module("Home", function(Home, App) {
        Home.on("start", function() {
            console.log("Home Started");
        });
        Home.controller = new Controller();
    });
});
