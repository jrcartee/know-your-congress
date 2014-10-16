define(function(require) {
    var BB = require('backbone');

	return BB.Model.extend({
		url: function() {
			return 'users/login/'
		}

	});
});