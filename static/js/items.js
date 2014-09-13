function fetchItems(item_type, query, callback){
    $.ajax({
        url: '/fetchitems',
        type: 'POST',
        data: {'item_type': item_type, 'query': JSON.stringify(query)},
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

function bindItemClick(specific_item_class, item_id){
    // alert('binding ' + item_id);
    $("#"+item_id).bind('click', function () {
        // Clear previous tasks if any
        $("#task_pane").html("");
        selectItem(specific_item_class, item_id);
    });
}

function selectItem(specific_item_class, item_id){
    // Clear item selection
    $("."+specific_item_class).css("border", "none");

    // Select current job
    $("#"+item_id).css("border", "1px solid");
    $("#"+item_id).css("borderColor", "#35bce3");
    $("#task_pane").css("display", "block");
}