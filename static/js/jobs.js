$(document).ready(function () {
    window.setInterval(refreshProgress, 2000); // repeat forever, polling every second
    fetchItems('jobs', null, function (result){
        $("#job_pane").html(result.html);
        for (var job in result.item_data){
            bindJobClick(result.item_data[job].id);
        }
    });
});

function bindJobClick(job_id){
    // alert('binding ' + job_id);
    $("#"+job_id).bind('click', function () {
        // Clear previous tasks if any
        $("#task_pane").html("");

        // Clear job selection
        $(".job").css("border", "none");

        // Select current job
        $("#"+job_id).css("border", "1px solid");
        $("#"+job_id).css("borderColor", "#35bce3");
        $("#task_pane").css("display", "block");

    });
}

$('#submit_job').click(function (){
    $.ajax({
        url: '/submit_job',
        type: 'POST',
        data: {username: null},
        success: function (result){
            if (result.job_id === null) {
                error('Your job was not submitted.');
            }
            else {
                success("Job (" + result.job_id + ") submitted successfully.");
                fetchItems("jobs", null, function (result){
                    $("#job_pane").html(result.html);
                });
                bindJobClick(result.job_id);
            }
        }
    });
});

function kill_job(job_id){
    $.ajax({
        url: '/kill_job',
        type: 'POST',
        data: {job_id: job_id},
        success: function (result){
            if (result.nailedit) {
                success("Removed job successfully.");
                fetchItems("jobs", null, function (result){
                    $("#job_pane").html(result.html);
                });
            }
            else {
                error('Your job was not removed. ' + result.error);
            }
        }
    });
}

function refreshProgress() {
    $.ajax({
        url: '/progress',
        type: 'POST',
        data: {username: null},
        success: function (result){
            // for each job: set progress
            for (var i in result.jobs_progress){
              var d = result.jobs_progress[i];
              $('#'+ d.jid + '_active').css('width', d.progress.active/d.progress.total*100 + '%');
              $('#'+ d.jid + '_finished').css('width', d.progress.finished/d.progress.total*100 + '%');
              $('#'+ d.jid + '_error').css('width', d.progress.error/d.progress.total*100 + '%');
              // for each task in selected job: set progress  
            }
            
        }
    });
}