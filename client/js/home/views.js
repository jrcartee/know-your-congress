define(function(require) {
	var M = require('marionette'),
		baseTemplate = require('tpl!home/templates/base.tpl'),
		AuthView = require('auth/views'),
		appChannel = require('app/channel');

	return M.LayoutView.extend({
		template: baseTemplate,
		regions: {
			"left_pane": "#left",
			"right_pane": "#right"
		},
		initialize: function() {
			_.bindAll(this, 'authorized')
			appChannel.commands.setHandler("set_auth", this.authorized);
		},
		onShow: function() {
			var is_authorized = appChannel.reqres.request('has_auth');
			if(!is_authorized) {
				this.right_pane.show(new AuthView());
			}
		},
		authorized: function() {
			this.right_pane.empty();
		}
	});
});