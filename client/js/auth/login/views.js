define(function(require) {
	var $ = require('jquery'),
		M = require('marionette'),
		LoginModel = require('auth/login/model'),
		appChannel = require('app/channel'),
		template = require('tpl!auth/login/form.tpl');

	return M.ItemView.extend({
		model: new LoginModel(),
		template: template,
		tagName: "form",
		ui: {
			submit: "#loginButton"
		},
		events: {
			"change": "setModelField",
			"click @ui.submit": "save"
		},
		initialize: function() {
			_.bindAll(this, 'save', 'onError', 'onSuccess');
		},
		setModelField: function(evt) {
			var field = evt.target.id,
				value = evt.target.value;
			this.model.set(field, value);
		},
		onError: function(model, response, options) {
			var resp = response.responseJSON,
				keys = _.keys(resp),
				setErrorSpan = function(field) {
					if(resp[field] != undefined){
						var err_span = "#" + field + "_error";
						this.$el.find(err_span).html("^ " + resp[field]);
					}
				};
			_.each(keys, setErrorSpan, this);
		},
		onSuccess: function(model, response, options) {
			var token = response.token;
			appChannel.commands.execute('set_auth', token);
		},
		save: function(evt) {
			evt.preventDefault();
			this.$el.find('span').html("");
			this.model.save({},{
				error: this.onError,
				success: this.onSuccess
			});
		}
	});
});