var response = $.post(window.location.href);
response.done(function(data) {
    var names = data.names;
    constructEngine(names)
});

function constructEngine(names) {
    // constructs the suggestion engine
    var players = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.whitespace,
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        local: names
    });

    $('#bloodhound .typeahead').typeahead({
        hint: true,
        highlight: true,
        minLength: 1
    },
    {
        name: 'players',
        source: players
    });
}