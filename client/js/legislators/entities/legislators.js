define(function(require) {
    var BB = require("backbone"),
    	appChannel = require("channel");

    var Legislator = BB.Model.extend({

    });

    var Legislators = BB.Collection.extend({
        url: 'api/legislators/read.json',
        model: Legislator
    });

    appChannel.reqres.setHandler("collection:legislators", function() {
    	return new Legislators();
    })
    appChannel.reqres.setHandler("model:legislator", function() {
    	return new Legislator();
    })
});