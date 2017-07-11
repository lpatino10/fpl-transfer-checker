var response = $.post(window.location.href);
response.done(function(data) {
    var playerData = data.all_player_info;
    constructEngine(playerData);
});

function transformData(playerData) {
    return $.map(playerData, function (player) {
        return {
            name: player.player_name,
            team: player.team_name
        };
    });
}

function constructEngine(playerData) {
    // constructs the suggestion engine
    var playerData = new Bloodhound({
        datumTokenizer: function (datum) {
            return Bloodhound.tokenizers.whitespace(datum.name);
        },
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        local: transformData(playerData)
    });

    $('#bloodhound .typeahead').typeahead({
        hint: true,
        highlight: false,
        minLength: 1
    },
    {
        name: 'playerData',
        source: playerData,
        display: 'name',
        templates: {
            suggestion: Handlebars.compile('<div>{{name}} ({{team}})</div>')
        }
    });
}