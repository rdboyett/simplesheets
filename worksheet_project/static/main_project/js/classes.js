$(document).ready(function(){
    
    $("#create-class-form").validate({
            errorPlacement: function(error, element){
		element.parent().parent().prepend(error);
            },
	    highlight: function(element, errorClass, validClass) {
		$(element).addClass(errorClass).removeClass(validClass);
		$(element.form).find("label[for=" + element.id + "]")
		  .addClass(errorClass);
		var check = $(element).next();
		if (check.hasClass("register-check-good")) {
		    check.removeClass("register-check-good").addClass("register-check-error");
		}else{
		    
		}
		check.fadeIn(300);
	    },
	    unhighlight: function(element, errorClass, validClass) {
		$(element).removeClass(errorClass).addClass(validClass);
		$(element.form).find("label[for=" + element.id + "]")
		  .removeClass(errorClass);
		var check = $(element).next();
		if (check.hasClass("register-check-error")) {
		    check.removeClass("register-check-error").addClass("register-check-good");
		}
		check.fadeIn(300);
	    },
    });
    
    
    $("#create-class-form").ajaxForm({ 
            success:       function(responseText){
                console.log(responseText);
                if (responseText.error) {
                    alert(responseText.error);
                }else if (responseText.groupID) {
                    $('#new-class').modal('hide');
                    window.location.href = "/classes/"+responseText.groupID+"/";
                }
            },
            dataType:  'json',
            timeout:   4000 
        });
    
    
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
    
    $("#assign-worksheets-ajax").click(function(){
        var numWorksheets = $("#worksheet-display .sheetList-body").size();
        console.log("list size is: "+numWorksheets);
        if (numWorksheets==0) {
            //var lastWorksheetID = $("#worksheet-display .sheetList-body").last().data("options").worksheetID;
            //console.log("WorksheetID: "+lastWorksheetID);
            getWorksheets("false", "next");
        }
    });
    
    
    $("#nextWorksheet-button").click(function(){
        var lastWorksheetID = $("#worksheet-display .sheetList-body").last().data("options").worksheetID;
        //console.log("Last WorksheetID: "+lastWorksheetID);
        getWorksheets(lastWorksheetID, "next");
        if ($("#prevWorksheet-button").hasClass("disabled")) {
            $("#prevWorksheet-button").removeClass("disabled");
        }
    });
    
    
    $("#prevWorksheet-button").click(function(){
        var lastWorksheetID = $("#worksheet-display .sheetList-body").first().data("options").worksheetID;
        //console.log("First WorksheetID: "+lastWorksheetID);
        getWorksheets(lastWorksheetID, "prev");
        if ($("#nextWorksheet-button").hasClass("disabled")) {
            $("#nextWorksheet-button").removeClass("disabled");
        }
    });
    
    
    
function getWorksheets(lastID, next_prev) {
    var formData = {"lastID":lastID, "next_prev":next_prev};
    $.ajax({
        url : getWorksheetsURL,
        type: "POST",
        data : formData,
        success: function(data, textStatus, jqXHR)
        {
            console.log(data);
            if (data.indexOf('Sorry, no more next') > -1) {
                //var JSONdata = jQuery.parseJSON(data);
                //console.log(JSONdata.error);
                if (!$("#nextWorksheet-button").hasClass("disabled")) {
                    $("#nextWorksheet-button").addClass("disabled");
                    $("#prevWorksheet-button").removeClass("disabled");
                }
                $("#no-worksheets").fadeIn( 600, function() {
                    $( "#no-worksheets" ).delay(1000);
                    $( "#no-worksheets" ).fadeOut( 600 );
                });
                
            }else if (data.indexOf('Sorry, no more prev') > -1) {
                if (!$("#prevWorksheet-button").hasClass("disabled")) {
                    $("#prevWorksheet-button").addClass("disabled");
                    $("#nextWorksheet-button").removeClass("disabled");
                }
                $("#no-worksheets").fadeIn( 600, function() {
                    $( "#no-worksheets" ).delay(1000);
                    $( "#no-worksheets" ).fadeOut( 600 );
                });
                
            }else{
                //check if there are any items in list and remove them
                if ($("#worksheet-display a").size()>0) {
                    $("#worksheet-display a").remove();
                }else{
                    if (!$("#prevWorksheet-button").hasClass("disabled")) {
                        $("#prevWorksheet-button").addClass("disabled");
                        $("#nextWorksheet-button").removeClass("disabled");
                    }
                }
                $("#assign-worksheets #class-spinner").fadeOut(600);
                $("#worksheet-display").append(data);
                $("#worksheet-display").fadeIn(600);
            }
        },
        error: function (jqXHR, textStatus, errorThrown)
        {
            console.log(errorThrown);
        }
    });
}

    
    
    
    
    
    
    
});


































