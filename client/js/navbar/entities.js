define(function(require) {
    var BB = require('backbone');

	var NavButton = BB.Model.extend({
		defaults: {
			'is_active': false
		}
	});
	var NavButtonCollection = BB.Collection.extend({
		model: NavButton,
		handleActiveState: function(url) {
			this.clear_stale();
			this.set_fresh(url);
		},
		clear_stale: function() {
			var stale_active = function(model) {
					return model.get('is_active');
				},
				stale_result = _.find(this.models, stale_active);
			if(stale_result != undefined){
				stale_result.set({is_active: false});
			}
		},
		set_fresh: function(url) {
			var fresh_active = function(model) {
					return model.get('url') == url;
				},
				fresh_result = _.find(this.models, fresh_active);
			fresh_result.set({is_active: true});
		}
	});

	return {
		collection: NavButtonCollection,
		button_list: [
	        {name: "Another", url: 'another'},
	        {name: "Bills", url: 'bills'},
	        {name: "Legislators", url: 'legislators'},
	        {name: "Home", url: ''}
    	]
	};
});