$(document).ready(fetchInstructions('linux_instructions'));
$(document).ready(fetchInstructions('other_instructions'));

function fetchInstructions(id) {
    $('#'+id).html(function () {
        $.ajax({
            url: $('#'+id).attr('url'),
            type: 'get',
            success: function (raw_markdown){
                $.ajax({
                    "url": 'http://api.github.com/markdown',
                    "text": raw_markdown,
                    "mode": "gfm",
                    "context": "github/gollum",
                    result: function (converted_html){
                    $('#'+id).html(converted_html);
                  }
                });
            }
        });
    });
}