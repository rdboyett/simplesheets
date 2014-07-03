$(document).ready(function(){
    //$('#filAlreadyExistsPopup').modal('show');
    
    
$("#openPicker").click(function(){
    createPicker();
});



























    

});


var opts = {
  lines: 11, // The number of lines to draw
  length: 5, // The length of each line
  width: 3, // The line thickness
  radius: 12, // The radius of the inner circle
  corners: 1, // Corner roundness (0..1)
  rotate: 0, // The rotation offset
  direction: 1, // 1: clockwise, -1: counterclockwise
  color: '#FFF', // #rgb or #rrggbb or array of colors
  speed: 1.8, // Rounds per second
  trail: 100, // Afterglow percentage
  shadow: true, // Whether to render a shadow
  hwaccel: false, // Whether to use hardware acceleration
  className: 'spinner', // The CSS class to assign to the spinner
  zIndex: 2e9, // The z-index (defaults to 2000000000)
  top: '50%', // Top position relative to parent
  left: '50%' // Left position relative to parent
};
var target = document.getElementById('wait-spinner');
var spinner = new Spinner(opts).spin(target);


function toggleSpinner() {
    if ($('#wait').is(":visible")) {
        $("#wait").fadeOut(600);
        $("#wait-spinner").fadeOut(600);
    }else{
        $("#wait").show();
        $("#wait-spinner").show();
    }
}

    $( window ).resize(function() {
        resizeElements();
      });
    
    function resizeElements() {
	var windowWidth = $(window).width(); //retrieve current window width
	var windowHeight = $(window).height();
	
	// Spinner Center
	var waitLeft = (windowWidth/2)-30;
	var waitTop = (windowHeight/2)-10;
	//console.log("Window Height: "+windowHeight+" Window Width: "+windowWidth+" wait width: "+$("#wait-spinner").width()+" wait height: "+$("#wait-spinner").height())
	//console.log(waitLeft+" and "+waitTop);
	$(".spinner").css({
	    'left':waitLeft,
	    'top':waitTop,
	});
        
    }
    
resizeElements();









    /***************************** File Exists Check what user wants to do ************************************************************************/
    function checkWithUser(fileId) {
	$('#filAlreadyExistsPopup').modal('show');
	$("#CreateNew").unbind('click').click(function(){
          deleteOldProject(fileId);
          document.location.href = '/worksheet/startCreate/'+fileId;
	  closePopups();
          setTimeout(toggleSpinner(), 1);
	});
	$("#UpdateOld").unbind('click').click(function(){
          document.location.href = '/openMyFile/'+fileId;
	  closePopups();
          setTimeout(toggleSpinner(), 1);
	});
	$("#PickNew").unbind('click').click(function(){
	  closePopups();
          createPicker();
	});
    }
    
    
function closePopups() {
    $('#filAlreadyExistsPopup').modal('hide');
}
    

function redirectProject(data, fileId) {
  if (data.projectExist == 'true') {
    toggleSpinner();
    checkWithUser(fileId);
    
  }else{
    document.location.href = '/worksheet/startCreate/'+fileId;
    }
}

    //---------------- Ajax Calls -----------------------------------------------------------
    
    /************************** Check If project already exits ****************/
	function checkProjectExists(fileID){
		console.log('In checkProjectExists');
	    
            toggleSpinner();
            var csrftoken = getCookie('csrftoken');
            var uri = checkProjectExistsURI;
            var xhr = new XMLHttpRequest();
            var fd = new FormData();
            
            xhr.open("POST", uri, true);
            xhr.onreadystatechange = function() {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    // Handle response.
		    //console.log(xhr.responseText);
		    var data = JSON.parse(xhr.responseText)
		    console.log(data);
		    if (data.error) {alert(data.error);}
		    else{
                      redirectProject(data, fileID);
                      console.log(data, fileID);
		    }
                }
            };
	    xhr.timeout = 4000;
	    xhr.ontimeout = function () { location.reload(); }
            fd.append('fileID', fileID);
            
            // Initiate a multipart/form-data upload
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            xhr.send(fd);
	    console.log( xhr._object);
        }
	
        
    /************************** Delete Old Project ****************/
	function deleteOldProject(fileID){
		console.log('In deleteOldProject');
	    
            toggleSpinner();
            var csrftoken = getCookie('csrftoken');
            var uri = deleteOldProjectURI;
            var xhr = new XMLHttpRequest();
            var fd = new FormData();
            
            xhr.open("POST", uri, true);
            xhr.onreadystatechange = function() {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    // Handle response.
		    //console.log(xhr.responseText);
		    var data = JSON.parse(xhr.responseText)
		    console.log(data);
		    if (data.error) {alert(data.error);}
		    else{}
                }
            };
	    xhr.timeout = 30000;
	    xhr.ontimeout = function () { location.reload(); }
            fd.append('fileID', fileID);
            
            // Initiate a multipart/form-data upload
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            xhr.send(fd);
	    console.log( xhr._object);
        }
	
        



// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

