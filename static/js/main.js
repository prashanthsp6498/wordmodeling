$(document).ready(function () {
    $(".suggestion").on('click', function () {
        var text = $.trim($('#textbox').val());
        var suggestionText = $('#' + $(this).attr('id')).text();
        var concatinate = text + " " + suggestionText;
        $('#textbox').val(concatinate);
    })
})



$(document).ready(function () {
    $(document).bind('keypress', function (event) {
        var text = $.trim($('#textbox').val());
        var suggestion = '';
        if (event.ctrlKey && event.shiftKey && event.which == 3) {
            suggestion = $('#0').text();
        }

        if (event.ctrlKey && event.shiftKey && event.which == 4) {
            var suggestion = $('#1').text();
        }

        if (event.ctrlKey && event.shiftKey && event.which == 5) {
            var suggestion = $('#2').text();
        }

        if (event.ctrlKey && event.shiftKey && event.which == 30) {
            var suggestion = $('#3').text();
        }

        if (event.ctrlKey && event.shiftKey && event.which == 6) {
            var suggestion = $('#4').text();
        }

        if (event.ctrlKey && event.shiftKey && event.which == 10) {
            var suggestion = $('#5').text();
        }
        $('#textbox').val(text + " " + suggestion);
    });
})

$(document).ready(function () {
    $('#textbox').keypress(function (event) {
        if (event.keyCode == 32) {
            console.log("Space Pressed");
        }
    })
})