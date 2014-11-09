$(document).ready(function(){
    
    var opts = {
        lines: 11, // The number of lines to draw
        length: 7, // The length of each line
        width: 3, // The line thickness
        radius: 11, // The radius of the inner circle
        corners: 1, // Corner roundness (0..1)
        rotate: 0, // The rotation offset
        direction: 1, // 1: clockwise, -1: counterclockwise
        color: '#000', // #rgb or #rrggbb or array of colors
        speed: 1, // Rounds per second
        trail: 60, // Afterglow percentage
        shadow: false, // Whether to render a shadow
        hwaccel: false, // Whether to use hardware acceleration
        className: 'spinner', // The CSS class to assign to the spinner
        zIndex: 2e9, // The z-index (defaults to 2000000000)
        top: '50%', // Top position relative to parent
        left: '50%' // Left position relative to parent
    };
    var target = document.getElementById('class-spinner');
    var spinner = new Spinner(opts).spin(target);
    
    
    $(".card-edpuzzle.list-video-item").click(function(){
	$(this).toggleClass('active');
	$(this).find( ".checkButton" ).toggleClass('fa-check-square-o').toggleClass('fa-square-o');
	checkActive();
    });
    
    function checkActive() {
	if($(".card-edpuzzle.active").length<1){
	    if (!$("#new-worksheet").hasClass('disabled')) {
		console.log('disabling');
		$("#new-worksheet").addClass('disabled');
	    }
	}else{
	    if ($("#new-worksheet").hasClass('disabled')) {
		console.log('enabling');
		$("#new-worksheet").removeClass('disabled');
	    }
	}
    }
    
    $(".class-button").click(function(){
	$(this).toggleClass('btn-primary').toggleClass('btn-success');
	checkClassSelected();
    });
    
    function checkClassSelected() {
	if($(".class-button.btn-success").length<1){
	    if (!$("#assignThis-button").hasClass('disabled')) {
		$("#assignThis-button").addClass('disabled').toggleClass('btn-primary').toggleClass('btn-success');
	    }
	}else{
	    if ($("#assignThis-button").hasClass('disabled')) {
		$("#assignThis-button").removeClass('disabled').toggleClass('btn-primary').toggleClass('btn-success');
	    }
	}
    }
    
    
    $("#assignThis-button").click(function(){
	if($(".class-button.btn-success").length>0){
	    //get the project id's
	    var projectIDList = [];
	    var count = 0;
	    $(".card-edpuzzle.list-video-item.active").each(function(){
		projectIDList[count]=$(this).data("options").worksheet_id;
		count++;
	    });
	    console.log(projectIDList);
	    
	    //get the class id's
	    var classIDList = [];
	    count = 0;
	    $(".class-button.btn-success").each(function(){
		classIDList[count]=$(this).data("options").class_id;
		count++;
	    });
	    console.log(classIDList);
	    sendAssignments(projectIDList, classIDList)
	}
    });
    
    
    
    function sendAssignments(projectIDList, classIDList) {
	var formData = {"projectIDList":projectIDList, "classIDList":classIDList};
	$.ajax({
	    type: "POST",
	    data: formData,
	    url: sendAssignmentsURL,
	    success:  function(data, textStatus, jqXHR)
	    {
		console.log(data);
	    },
	    error: function (jqXHR, textStatus, errorThrown)
	    {
		console.log(errorThrown);
	    }
	 });
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
});
