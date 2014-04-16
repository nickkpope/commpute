function fetchItems(id, item_type){
    $.ajax({
        url: '/fetchitems',
        type: 'POST',
        data: {pane_id: id, item_type: item_type},
        success: function (result){
            $('#' + id).html(result);
        }
    });
}

function deleteItem(pane, id, item_type) {
    $('#' + id).fadeOut(400, function () {
        $.ajax({
            url: '/deleteitem',
            type: 'POST',
            data: {pane_id: pane.id, item_id: id, item_type: item_type},
            success: function (result){
                $('#' + pane.id).html(result);
            }
        });
    });
}
