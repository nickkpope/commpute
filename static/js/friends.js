var searching;

$(document).ready(function (){
    searching = false;
    loadPanes();
});

function loadPanes(){
    fetchItems("friends", null, function (result){
        $('#friends_pane').html(result.html);
        selectFriend(result);

    });

    fetchItems('friend_suggestions', null, function (result){
        $('#suggestions_pane').html(result.html);
        selectFriend(result);
    });
}

function selectFriend (result){
    $('.friend').bind('click', {result: result}, function (event){
        selectItem('friend', $(this).attr('id'));
        // Display their computers
        var friend_username;
        for (var i in result.item_data){
            var friend = result.item_data[i];
            if (friend.id === $(this).attr('id')){
                friend_username = friend.username;
            }
        }
        if (friend_username !== undefined){
            $.ajax({
                url: '/fetch_user_computers/' + friend_username,
                success: function (result){
                    $('#computers_pane').html(result.html);
                }
            });
        }
    });
}

$('#search_button').click(function(){
    searchFriends();
});
function searchHandler(e){
    if (e.keyCode === 13){
        searchFriends();
    }

}
function searchFriends(){
    if (searching){
        $('#main_pane')[0].style.display = "block";
        $('#results_pane')[0].style.display = "none";
        $("#search_button").html('<span class="glyphicon glyphicon-search"></span>');
        searching = false;
    }
    else{
        $('#main_pane')[0].style.display = "none";
        $('#results_pane')[0].style.display = "block";
        $("#search_button").html('<span class="glyphicon glyphicon-remove-circle"></span>');
        searching = true;
    }
    fetchItems('friends_results', {'name': $('#search_box').val()}, function (result){
        $('#friends_results_pane').html(result.html);
    });
    fetchItems('friends_suggestions_results', {'name': $('#search_box').val()}, function(result){
        $('#friends_suggestions_results_pane').html(result.html);
    });
    
}

function addFriend(friend_username) {
    manageFriend(friend_username, '/add_friend');
}

function removeFriend(friend_username){
    manageFriend(friend_username, '/remove_friend');
}

function manageFriend(friend_username, url){
    $.ajax({
        url: url,
        type: 'POST',
        data: {friend_username:friend_username},
        success: function (result){
            if (result.nailedit){
                loadPanes();
            }
        }
    });
}
