$(document).ready(function () {
    window.setInterval(refreshProgress, 2000); // repeat forever, polling every second
    fetchItems('jobs', null, function (result){
        $("#job_pane").html(result.html);
        $('.job').click(function (){
            selectItem('job', $(this).attr('id'));
        });
    });
});

$('#submit_job').click(function (){
    $.ajax({
        url: '/submit_job',
        type: 'POST',
        data: {username: null},
        success: function (result){
            if (result.job_id === null) {
                error('Your job was not submitted: ' + result.error);
            }
            else {
                success("Job (" + result.job_id + ") submitted successfully.");
                fetchItems("jobs", null, function (result){
                    $("#job_pane").html(result.html);
                });
                bindItemClick(result.job_id);
                $('#no_jobs').css('display', 'none');
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