$(document).ready(function () {
    // window.setInterval(refreshProgress, 2000); // repeat forever, polling every second
    fetchItems('job_pane', null, function (result){
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
                    alert(result.item_data);
                });
                bindJobClick(result.job_id);
            }
        }
    });
});

function refreshProgress() {
    $.ajax({
        url: '/progress',
        type: 'POST',
        data: {username: null},
        success: function (result){
            // for each job: set progress
            // for each task in selected job: set progress
        }
    });
}


   // var task = job.tasks[j];

   //  var taskRow = document.createElement('div');
   //  taskRow.setAttribute('id', job.id+'_'+task.id+'_'+'_row');
   //  taskRow.setAttribute('class','row text-left');
   //  document.getElementById("task_list").appendChild(taskRow);

   //      var taskNameCol1 = document.createElement('div');
   //      taskNameCol1.setAttribute('class', 'col-sm-6');
   //      taskRow.appendChild(taskNameCol1);

   //          var taskNameSpan = document.createElement('span');
   //          taskNameSpan.textContent = task.name;
   //          taskNameSpan.setAttribute('style', 'font-size: 1.3em;');
   //          taskNameCol1.appendChild(taskNameSpan);

   //      var taskNameCol2 = document.createElement('div');
   //      taskNameCol2.setAttribute('class', 'col-sm-6');
   //      taskRow.appendChild(taskNameCol2);

   //          var taskProgContainer = document.createElement('div');
   //          taskProgContainer.setAttribute('class', 'progress progress-striped active');
   //          taskNameCol2.appendChild(taskProgContainer);

   //          var taskProgBar = document.createElement('div');
   //          taskProgBar.setAttribute('id', job.id+'_'+task.id+'_pbar');
   //          taskProgBar.setAttribute('class', 'progress-bar');
   //          taskProgBar.setAttribute('role', 'progressbar');
   //          taskProgBar.setAttribute('aria-valuenow','0');
   //          taskProgBar.setAttribute('aria-valuemin','0');
   //          taskProgBar.setAttribute('aria-valuemax','100');
   //          taskProgBar.setAttribute('style','width: 0%');
   //          taskProgContainer.appendChild(taskProgBar);