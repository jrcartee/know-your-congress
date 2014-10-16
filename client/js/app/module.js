define(function(require) {
    var BB = require("backbone"),
        M = require("marionette"),
        Controller = require('app/controller'),
        channel = require('app/channel');

    console.log("App Initializing");

    var App = new M.Application();

    App.config = {
        'api': "http://127.0.0.1:7000/"
    };

    App.addRegions({
        header: "#header",
        container: "#container",
        footer: "#footer"
    });

    App.controller = new Controller();
    App.channel = channel;

    App.addInitializer(function () {
        BB.history.start();
    });

    return App;
});