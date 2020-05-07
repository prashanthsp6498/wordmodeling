$(document).ready(function () {
    var index = 0;
    $(document).bind('keypress', function (event) {
        var text = $.trim($('#textbox').val());
        var suggestion = '';
        if (event.ctrlKey && event.shiftKey && event.which == 3) {
            suggestion = $('#0').text();
            $('#textbox').val(text + " " + suggestion);
        }

        if (event.ctrlKey && event.shiftKey && event.which == 4) {
            var suggestion = $('#1').text();
            $('#textbox').val(text + " " + suggestion);
        }

        if (event.ctrlKey && event.shiftKey && event.which == 5) {
            var suggestion = $('#2').text();
            $('#textbox').val(text + " " + suggestion);
        }

        if (event.ctrlKey && event.shiftKey && event.which == 30) {
            var suggestion = $('#3').text();
            $('#textbox').val(text + " " + suggestion);
        }

        if (event.ctrlKey && event.shiftKey && event.which == 6) {
            var suggestion = $('#4').text();
            $('#textbox').val(text + " " + suggestion);
        }

        if (event.ctrlKey && event.shiftKey && event.which == 10) {
            var suggestion = $('#5').text();
            $('#textbox').val(text + " " + suggestion);
        }
    });

    $(document).bind('keypress', function (event) {
        if (event.which == 12) {
            $('#textbox').val('');
        }
        if (event.which == 7) {
            $('.help').toggle();
        }
    })

    $(document).bind('keypress', function (event) {
        index++;
        var bg = '';
        var fontColor = '';
        var mode = '';
        if (event.which == 26) {
            if (index % 2 == 0) {
                console.log("HE");
                bg = '#343a40';
                fontColor = 'white';
                mode = 'dark';
            }
            else {
                bg = 'white';
                fontColor = 'black';
                mode = 'light';
            }
            $('.background').css('background-color', bg);
            $('.background').css('color', fontColor);
            $('.navbar-brand').css('color', fontColor);
            $('.mode_button').text(mode);
        }
    })
})


$(document).ready(function () {
    $(".suggestion").on('click', function () {
        var text = $.trim($('#textbox').val());
        var suggestionText = $('#' + $(this).attr('id')).text();
        var concatinate = text + " " + suggestionText;
        $('#textbox').val(concatinate);
    })
})