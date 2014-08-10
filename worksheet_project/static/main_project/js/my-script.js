$(document).ready(function(){
    
    var cookie = getCookie('monitor-view');
    if (cookie=='grid') {
	$("#grid-students").fadeIn(600);
	startCircleDraw();
    }else{
	$("#list-students").fadeIn(600);
    }
    
    
    
  $('div [data-toggle="popover"]').popover();
  //$('#add-class').popover('show');
  //$('#class-code-container').popover('show');
  //$('#new-worksheet').popover('show');
  
  $('div [data-toggle="tooltip"]').tooltip();
  $('button[data-toggle="tooltip"]').tooltip();
  
  
    $('#grid-btn').click(function(){
	$('#list-students').fadeOut(600, function(){
	    $('#grid-students').fadeIn(600);
	});
	startCircleDraw();
	setCookie('monitor-view','grid',30);
    });
    
    $('#list-btn').click(function(){
	$('#grid-students').fadeOut(600, function(){
	    $('#list-students').fadeIn(600);
	});
	setCookie('monitor-view','list',30);
    });
    
    
});


    function resizeTop(element) {
	var halfScreenHeight = ($(window).height())/2;
	var halfElementHeight = (element.height())/2;
	var top = halfScreenHeight - halfElementHeight;
	element.css({
	    'top': top+"px",
	});
    }
    function resizeLeft(element) {
	var halfScreenWidth = ($(window).width())/2;
	var halfElementWidth = (element.width())/2;
	var left = halfScreenWidth - halfElementWidth;
	element.css({
	    'left': left+"px",
	});
    }
    
    function resizePopups() {
	//resizeTop($("#popup"));
	//resizeLeft($("#popup"));
        $("#height").html($(window).height());
	$("#width").html($(window).width());
    }
    
    
    
    
    
    //this won't work until your are on a server
/******************************************** Function **************************************************/

    function setCookie(cname,cvalue,exdays){
	var d = new Date();
	d.setTime(d.getTime()+(exdays*24*60*60*1000));
	var expires = "expires="+d.toGMTString();
	document.cookie = cname + "=" + cvalue + "; " + expires;
    }
	
	
    function getCookie(cname){
	var name = cname + "=";
	var ca = document.cookie.split(';');
	for(var i=0; i<ca.length; i++){
	    var c = ca[i].trim();
	    if (c.indexOf(name)==0) return c.substring(name.length,c.length);
	  }
	return "";
    }
    

var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

    
    function startCircleDraw(){
	$("#grid-students .studentBox").each(function(){
	    var total_number_of_questions = 10; //put the django template here
	    var id = $(this).attr('id');
	    var wrong = parseInt($(this).data("options").wrong/total_number_of_questions*100);
	    var right = parseInt($(this).data("options").right/total_number_of_questions*100)+wrong;
	    //console.log(scores);
	    if (wrong>=40) {
		$(this).css({
		    "background-color":"#ffb3b3",
		    "border-color":"#ff0000",
		});
	    }
	    drawCircle(id, 'right-green', parseInt(right));
	    drawCircle(id, 'wrong-red', parseInt(wrong));
	});
    }
    
    
    function drawCircle(studentID, bar, percentage) {
        var i = 0;
        var circle = $("#"+studentID+" ."+bar);
        var angle = 130;
        var radius = 50;
        var timer = window.setInterval(function() {
            angle +=5;
            angle %= 360;
            var radians= (angle/180) * Math.PI;
            var x = 62 + Math.cos(radians) * radius;
            var y = 64 + Math.sin(radians) * radius;
            var e = circle.attr("d");
            if(i==0) {
                var d = e+ " M "+x + " " + y;
            }
            else {
                var d = e+ " L "+x + " " + y;
            }  
            circle.attr("d", d);
	    if (i>(53*percentage/100)) {
		clearInterval(timer);
	    }
	    //console.log("i: "+i);
	    //console.log("angle: "+angle);
            i++;
        } 
	,10);
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    