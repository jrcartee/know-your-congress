define(function(require) {
    var _ = require('underscore'),
    	M = require('marionette'),
	    entities = require('navbar/entities'),
        navView = require("navbar/views"),
        appChannel = require("app/channel");

    console.log("Setting Up Navbar Controller..")
	return M.Controller.extend({
		initialize: function() {
			this.initView();
			this.registerHandlers();
		},
		initView: function() {
			var buttonCollection = new entities.collection(
				entities.button_list
			);
			this.view = new navView({collection: buttonCollection});
		},
		registerHandlers: function() {
			_.bindAll(this, 'update');

			appChannel.commands.setHandler("navbar:update", this.update)
		},
		update: function() {
			this.view.updateActiveButton();
		}
    });
});