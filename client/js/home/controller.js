define(function(require) {
	var M = require('marionette'),
		HomeView = require('home/views');

	return M.Controller.extend({
		initialize: function() {
			this.initView();
		},
		initView: function() {
			this.view = new HomeView();
		}
	});
});