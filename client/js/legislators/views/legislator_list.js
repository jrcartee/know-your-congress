define(function(require) {
    var BB = require('backbone'),
        Legislators = require('models/legislator_collection'),
        list_template = require('tpl!templates/accordian_list.tpl'),
        term_template = require('tpl!templates/legislator/accordian_term.tpl'),
        definition_template = require('tpl!templates/legislator/accordian_definition.tpl');


    return BB.View.extend({
        el: "#legislators",
        events: {
            "click dt": "toggleDefinition"
        },

        initialize: function() {
            this.collection = new Legislators();
            var that = this;

            this.collection.fetch({
                success: function(list, response) {
                    that.list = list;
                    that.render();
                },
                error: function(list, response) {
                    that.$el.html("wahh wahh wah....");
                    console.log("400: ", response);
                }
            });
        },

        render: function() {
            if(this.list) {
                console.log("render", list_template);
                var template_data = {
                        items: this.list.models,
                        term: term_template,
                        definition: definition_template
                    },
                    fragment = list_template(template_data);
                this.$el.html(fragment);
            } else {
                this.$el.html("<h1>An Error Occured.. SORRY</h1>")
            }

        },

        toggleDefinition: function(event) {
            $(event.target).next().slideToggle(150);
        }

    });

});