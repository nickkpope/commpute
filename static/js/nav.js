$(document).ready(function (){
    setCurrentPillState();
    $(document).ready(function () {
    if ($("[rel=tooltip]").length) {
        $("[rel=tooltip]").tooltip();
    }
});
    
});


function setCurrentPillState(){
    if (location.pathname.substring(0, 5) == "/home"){
        $('#home-nav-pill')[0].setAttribute("class", "active");
    }
    else if (location.pathname.substring(0, 8) == "/friends"){
        $('#friends-nav-pill')[0].setAttribute("class", "active");
    }
    else if (location.pathname.substring(0, 5) == "/jobs"){
        $('#jobs-nav-pill')[0].setAttribute("class", "active");
    }
    else if (location.pathname.substring(0, 9) == "/settings"){
        $('#settings-nav-pill')[0].setAttribute("class", "active");
    }
    else{

    }
}

function error(message){
    displayAlert('alert-danger', message);
}

function success(message){
    displayAlert('alert-success', message);
}

function displayAlert(type, message){
    $("#global-alert").html('<div class="alert ' + type + ' fade in out"><p>' + message + '</p></div>');
    $(".alert").alert();
    window.setTimeout(function (){
        $(".alert").alert('close');
    }, 3000);
}