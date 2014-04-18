function fetchItems(item_type, query, callback){
    $.ajax({
        url: '/fetchitems',
        type: 'POST',
        data: {item_type: item_type, query: query},
        success: function (result){
            callback(result);
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
