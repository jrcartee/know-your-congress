<h3> Legislators </h3>
<dl>
    <% _.each(items, function(item) { %>
        <dt>
            <%= term({"item": item}) %>
        </dt>
        <dd style="display:none">
            <%= definition({"item": item}) %>
        </dd>
    <% }); %>
</dl>