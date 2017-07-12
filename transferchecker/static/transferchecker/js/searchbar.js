// constructs the suggestion engine
var engine = new Bloodhound({
    initialize: false,
    datumTokenizer: function (datum) {
        return Bloodhound.tokenizers.whitespace(datum.name);
    },
    queryTokenizer: Bloodhound.tokenizers.whitespace
});

function transformData(playerData) {
    return $.map(playerData, function (player) {
        return {
            name: player.player_name,
            team: player.team_name,
            id: player.player_id
        };
    });
}

var takenPlayers = null;
var response = $.post(window.location.href);
response.done(function(data) {
    var playerData = data.all_player_info;
    takenPlayers = new Set(data.taken_list);
    playerData = transformData(playerData);
    engine.local = playerData;

    // initializes suggestion engine here
    engine.initialize();
});

$('.typeahead').typeahead({
    hint: true,
    source: engine.ttAdapter(),
    displayText: function (player) {
  	    return player.name + '<span class="dropdown-item-extra">' + player.team + '</span>'
    },
    highlighter: Object,
    afterSelect: function(player) { 
        // makes sure we don't show HTML in text box
        $('.typeahead').val(player.name).change(); 

        // does check against rest of the league's players
        if (takenPlayers.has(player.id)) {
            $('#result').toggleClass('invis').toggleClass('glyphicon-minus').toggleClass('glyphicon-remove').toggleClass('red');
        }
        else {
            $('#result').toggleClass('invis').toggleClass('glyphicon-minus').toggleClass('glyphicon-ok').toggleClass('green');
        }
    }
});

$('.typeahead').on('input', function() {
    window.scrollTo(0,document.body.scrollHeight);
    if (!$('#result').hasClass('invis')) {
        $('#result').removeClass();
        $('#result').addClass('glyphicon glyphicon-minus invis');
    }
});