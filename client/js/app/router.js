define(function(require) {
    var M = require('marionette'),
        App = require('app/module');

    console.log("Router Initializing");

    var Controller = M.Controller.extend({
        initialize: function(options) {
            this.showNavbar();
        },
        showNavbar: function() {
            Navbar = require('navbar/module');
            App.header.show(Navbar.controller.view);
        },
        showHome: function() {
            Home = require('home/module');
            App.container.show(Home.controller.view);
        },
        showLegislators: function() {
            console.log("welcome to legislators!");
            // App.container.show(new LegislatorView());
        },
        showBills: function() {
            console.log("welcome to bills!");
            // App.container.show(new HomeView());
        },
        showAnother: function() {
            console.log("welcome to another!");
            // App.container.show(new HomeView());
        }
    });

    return M.AppRouter.extend({

        appRoutes: {
            '': 'showHome',
            'legislators': 'showLegislators',
            'bills': 'showBills',
            'another': 'showAnother'
        },

        controller: new Controller(),

        onRoute: function(name, path, args) {
            App.channel.commands.execute("navbar:update");
        }
    });

});