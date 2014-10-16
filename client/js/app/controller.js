define(function(require) {
	var $ = require('jquery'),
		M = require('marionette'),
		appChannel = require('app/channel');

	return M.Controller.extend({

		initialize: function() {
			this.authenticated = false;
			this.registerHandlers();
		},
		registerHandlers: function() {
			_.bindAll(this, 'setAuth', 'getAuth', 'setAuthHeader')

			appChannel.commands.setHandler("set_auth", this.setAuth);
			appChannel.reqres.setHandler("has_auth", this.getAuth);
		},
		getAuth: function() {
			return this.authenticated;
		},
		setAuth: function(token) {
			this.authenticated = true;
			this.token = "Token " + token;
			$.ajaxPrefilter(this.setAuthHeader);
		},
		setAuthHeader: function(options, origOptions, jqXHR){
			if(options.beforeSend == undefined) {
				options.beforeSend = function(xhr) {
					xhr.setRequestHeader("Authorization", this.token);
				};
			}
		}
	});
});