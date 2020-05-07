$(document).ready(function () {
    var word_url = '/api/wordpredict?word=';
    $('#textbox').keypress(function (event) {
        var text = '';
        if (event.keyCode == 32) {
            text = $('#textbox').val();
            text = $.trim(text);
            text = text.split('  ').join(' ');
            $('#textbox').val(text);
            var information = {
                type: 'GET',
                url: word_url + text,
            }
            send_request(information);
            // $.ajax({
            //     data: {
            //         textbox: text,
            //     },
            //     type: 'POST',
            //     url: '/wordpredict',
            // })

        }
    })


    $('#englishtextbox').bind('keypress', function (event) {
        if (event.which == 12) {
            var text = $.trim($(this).val());
            var textbox = $.trim($('#textbox').val());
            var base_url = '/api/translator?word=' + text;
            var information = {
                data: {
                    word: text,
                },
                type: 'GET',
                url: base_url,
            }
            if (text) {
                $.ajax(information).done(function (data) {
                    var predict_information = {
                        type: 'GET',
                        url: word_url + data['word'],
                    };
                    send_request(predict_information);
                    console.log(textbox);
                    $('#textbox').val(textbox + " " + $.trim(data['word']));
                })
            }
        }
    })


    function send_request(information) {
        $.ajax(information).done(function (data) {
            if (data) {
                console.log(data.result);
                // $('.suggestion_row').show();
                for (var i = 0; i < data.result.length; i++) {
                    $('#' + i.toString()).text(data.result[i]);
                }
            }
            else {
                console.log("May be something went wrong");
            }
        });
    }
})



$(document).ready(function () {
    $('#englishtextbox').keypress(function (event) {
        var text = '';
        var data = { "nanage": "kannadaNanage" }
        var flag = false;
        console.log(event.which);
        if (event.keyCode == 12) {
            text = $(this).val();
            console.log(text);
            console.log(data[text]);
            $('#englishtextbox').val("");
            $(this).val($(this).val().replace(/^\\s*/g, ''));
        }
        var de = $('#englishtextbox').val();
        console.log(de.length);
    })
})


$(document).ready(function () {
    var base_url = '/api/files?filename=';
    $(document).on('click', '.files', function () {
        var filename = $(this).children().children().text();
        var editor = 'editor?filename=' + filename;
        $(location).attr('href', editor);

    })
})

$(document).ready(function () {
    $('.filebutton').on('click', function () {
        var filename = $('.filename').val();
        if (filename) {
            $(location).attr('href', '/editor?filename=' + filename);
        }
    })

})

$(document).ready(function () {
    var url = $(location).attr('href').split('?')[0];
    var file_name = $(location).attr('href').split('?')[1].split('=')[1];
    console.log(file_name)
    $('.filename_btn').text(file_name);
    if (url == "http://127.0.0.1:5000/editor") {
        if (file_name) {
            var information = {
                data: {
                    filename: file_name,
                },
                type: 'GET',
                url: '/api/files?filename=' + file_name,
            };
            $.ajax(information).done(function (data) {
                if (data) {
                    $('#textbox').val(data['filedata']);
                    $('.filename_btn').text(file_name);
                }
            })
        }
    }

    $('#save_text').on('click', function () {
        var text = $('#textbox').val();
        var filename = $('.filename_btn').text();
        console.log(text);
        var information = {
            data: {
                text: text,
                filename: filename,
            },
            type: 'POST',
            url: '/api/save_text',
        };
        $.ajax(information).done(function (data) {
            if (data.success) {
                $('.save_hide_btn').parent().toggle();
                $('.save_status').val("Saved Successfully");
            }
        })
    })
})


$(document).ready(function () {
    $('.save_status').hide();
    var url = $(location).attr('href').split('?')[0];
    var file_name = $(location).attr('href').split('?')[1].split('=')[1];
    if (url == "http://127.0.0.1:5000/editor") {
        if (file_name) {
            var information = {
                data: {
                    filename: file_name,
                },
                type: 'GET',
                url: '/api/files?filename=' + file_name,
            };
            $.ajax(information).done(function (data) {
                if (data) {
                    $('#textbox').val(data['filedata']);
                    $('.filename_btn').text(file_name);
                }
            })
        }
    }

    $('#save_text').on('click', function () {
        var text = $('#textbox').val();
        var filename = $('.filename_btn').text();
        console.log(text);
        var information = {
            data: {
                text: text,
                filename: filename,
            },
            type: 'POST',
            url: '/api/save_text',
        };
        $.ajax(information).done(function (data) {
            if (data.success) {
                $('.save_hide_btn').parent().toggle();
                $('.save_status').val("Saved Successfully");
            }
        })
    })

    $('.help_hide_btn').on('click', function () {
        $(this).parent().toggle();
    })

    $('.save_hide_btn').on('click', function () {
        $(this).parent().toggle();
    })

})