$(window).ready(function () {
    $('.container').hide();
    $('.help').hide();
    // $('.suggestion_row').hide();
    $(document).ready(function () {
        $('#loader').hide();
        $('.container').show();
    })
})



$(document).ready(function () {
    $('.language').on('click', function () {
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


// dark-mode function
$(document).ready(function () {
    $('.color_mode').on('click', function () {
        var id = $(this).attr('id');
        var bg = '#343a40';
        var fontColor = 'white';
        if (id == 'dark') {
            bg = '#343a40';
            fontColor = 'white';
        }
        else {
            bg = 'white';
            fontColor = 'black';
        }
        $('.background').css('background-color', bg);
        $('.background').css('color', fontColor);
        $('.navbar-brand').css('color', fontColor);
        $('.mode_button').text(id);

    })
})