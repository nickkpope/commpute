$(document).ready(function (){
    setCurrentPillState();
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