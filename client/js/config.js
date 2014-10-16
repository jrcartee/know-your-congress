require.config({
	paths: {
		"tpl": 					"_lib/require.tpl",
		"jquery": 				"_lib/jquery",
		"underscore": 			"_lib/underscore",
		"backbone": 			"_lib/backbone",
		"backbone.wreqr": 		"_lib/backbone.wreqr",
		"backbone.babysitter": 	"_lib/backbone.babysitter",
		"marionette": 			"_lib/backbone.marionette"
	}
});

require(['init']);