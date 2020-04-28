$(window).ready(function () {
    $('.container').hide();
    $(document).ready(function () {
        $('#loader').hide();
        $('.container').show();
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

$(document).ready(function () {
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
    })
})

$(document).ready(function () {
    $('#textbox').keypress(function (event) {
        if (event.keyCode == 32) {
            console.log("Space Pressed");
        }
    })
})

$(document).ready(function () {
    $('.language').on('click', function() {
        var id = $(this).attr('id');
        if (id == 'kannada') {
            $('.navbar-brand').text('ವರ್ಡ್ ಮಾಡೆಲ್');
            $('#textAreaLabel').text('ಬರಿಯುವ ಸ್ಥಳ');
            $('#textbox').attr('placeholder', 'ಇಲ್ಲಿ ಬರಿಯಿರಿ ');
            $('.language_button').text('ಕನ್ನಡ');
        }
        else if (id == 'english') {
            $('.navbar-brand').text('Word Model');
            $('#textAreaLabel').text('Text Area');
            $('.language_button').text('English');
            $('#textbox').attr('placeholder', 'Type here');
        }


    })
})