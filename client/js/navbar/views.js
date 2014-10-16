define(function(require) {
    var BB = require('backbone'),
    	M = require('marionette'),
    	itemTemplate = require('tpl!navbar/templates/button_item.tpl'),
    	listTemplate = require('tpl!navbar/templates/button_list.tpl');

	var ButtonItem = M.ItemView.extend({
		template: itemTemplate,
		className: "nav_button",
		tagName: "li",
		events: {
		},
		initialize: function() {
			this.model.bind("change:is_active", this.updateActiveStyle, this)
		},
		updateActiveStyle: function() {
			if(this.model.get('is_active')) {
				this.$el.addClass('active');
			} else {
				this.$el.removeClass('active')
			}

		},
	});

	return M.CompositeView.extend({
		template: listTemplate,
		childView: ButtonItem,
		childViewContainer: "ul",
		initialize: function() {
		},
		updateActiveButton: function() {
			var currentURL = BB.history.location.hash,
				currentURL = currentURL.replace("#", "");
			this.collection.handleActiveState(currentURL);
		}

	});
});