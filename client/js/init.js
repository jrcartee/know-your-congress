define(function(require) {
	var $ = require('jquery'),
		App = require('app/module'),
		Router = require('app/router');

	$.ajaxPrefilter(function(options, origOptions, jqXHR){
		options.url = App.config.api + options.url;
	});


	// router's controller requires access to App
	// so router is loaded here
	App.appRouter = new Router();

	console.log("Starting App..");
	App.start();

});