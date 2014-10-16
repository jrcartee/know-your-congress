define(function(require) {
	var M = require('marionette'),
		baseTemplate = require('tpl!auth/base.tpl'),
		LoginView = require('auth/login/views'),
		RegisterView = require('auth/register/views');

	return M.LayoutView.extend({
		template: baseTemplate,
		regions: {
			"nav":"#users_nav",
			"main_content": "#users_content"
		},
		events: {
			"click #users_login": "showLogin",
			"click #users_register": "showRegister"
		},
		initialize: function() {
		},
		onShow: function() {
			this.showLogin();
		},
		showLogin: function(e) {
			this.main_content.show(new LoginView());
		},
		showRegister: function(e) {
			this.main_content.show(new RegisterView());
		}
	});
});