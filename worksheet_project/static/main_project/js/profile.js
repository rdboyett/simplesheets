$(document).ready(function(){
    
    $("#update-school-form").validate({
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
    
    // bind form using 'ajaxForm' 
    $('#update-teacherStudent-form').ajaxForm({ 
        //target:        '#output1',   // target element(s) to be updated with server response 
        //beforeSubmit:  function(formData, jqForm, options){},  // pre-submit callback 
        success:       function(responseText, statusText, xhr, $form){        // post-submit callback 
            //console.log(responseText.teacherStudent);
            if (responseText.error) {
                alert(responseText.error);
            }
        },
        //error: function(xhr, statusText, error){},  //when an error occurs
        
        // other available options: 
        //url:       url         // override for form's 'action' attribute 
        //type:      type        // 'get' or 'post', override for form's 'method' attribute 
        dataType:  'json',        // 'xml', 'script', or 'json' (expected server response type) 
        //clearForm: true        // clear all form fields after successful submit 
        //resetForm: true        // reset the form after successful submit 
 
        // $.ajax options can be used here too, for example: 
        timeout:   4000 
    }); 
    
    $('#update-school-form').ajaxForm({ 
        success:       function(responseText){
            if (responseText.error) {
                alert(responseText.error);
            }else if (responseText.schoolName) {
                $("#schoolName-span").html(responseText.schoolName);
            }
        },
        dataType:  'json',
        timeout:   4000 
    }); 
    
    
    
    
    
    
});

