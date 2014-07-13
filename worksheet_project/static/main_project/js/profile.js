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
            }else{$('#teacher-student').modal('hide');}
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
		$('#update-school').modal('hide');
            }
        },
        dataType:  'json',
        timeout:   4000 
    }); 
    
    

//add the custom validation method
$.validator.addMethod("wordCount",
   function(value) {
      var typedWords = jQuery.trim(value).split(' ').length;
 
      if(typedWords == 2) {
         return true;
      }else{return false}
      
   },"first and last name.");

    $("#profile-form").validate({
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
	
	    rules: {
		'fullName': {
		   wordCount: true
		}
	    },
    });
    
    
    $('#profile-form').ajaxForm({ 
        success:       function(responseText){
            if (responseText.error) {
                alert(responseText.error);
            }else if (responseText.fullName) {
                $("#fullName-input").val(responseText.fullName);
            }
        },
        dataType:  'json',
        timeout:   4000 
    }); 
    
    
    
    
    
    
    
    
    
    
    
    
    
$.validator.addMethod("noWhitespace",
   function(value) {
    var noWhitespaces = /^\w+$/;
    if (noWhitespaces.test(value)){
        return true
    }else{return false}
   },'no spaces');
    
$.validator.addMethod("needANumber",
   function(value) {
    var number = /[0-9]/;
    if (number.test(value)){
        return true
    }else{return false}
   },'at least 1 number');
    
$.validator.addMethod("lowerCase",
   function(value) {
    var lowerLetter = /[a-z]/;
    if (lowerLetter.test(value)){
        return true
    }else{return false}
   },'at least 1 lowercase');

$.validator.addMethod("upperCase",
   function(value) {
    var upperLetter = /[A-Z]/;
    if (upperLetter.test(value)){
        return true
    }else{return false}
   },'at least 1 uppercase');
    
    
    
    
    $("#reset-password-form").validate({
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
	    rules: {
		password1: {
		    required: true,
		    minlength: 6,
		    maxlength: 30,
		    noWhitespace: true,
		    needANumber: true,
		    lowerCase: true,
		    upperCase: true,
		},
		password2: {
		    required: true,
		    equalTo: "#password1"
		},
	    },
	    messages: {
		password2: {
		    required: "confirm",
		    equalTo: "same password as above"
		},
	    }
});
    
    
    
    $('#reset-password-form').ajaxForm({ 
        success:       function(responseText){
            if (responseText.error) {
                alert(responseText.error);
            }else if (responseText.success) {
		$('#reset-password').modal('hide');
            }
        },
	clearForm: true,
	resetForm: true,
        dataType:  'json',
        timeout:   4000 
    }); 
    
    
    
    
    $("#change-username-form").validate({
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
	    rules: {
		userName: {
		    noWhitespace: true,
		},
	    },
});
    
    
    /************************** check username ****************************************************************************88*******/
	function doesUsernameExist(username) {
		console.log('In doesUsernameExist');
	    var labelHolder = $('#change-username-form :input[name="userName"]').parent().parent(),
		badge = $('#change-username-form :input[name="userName"]').next(),
		label = '<div class="error my_error">username already exists</div>',
		input = $('#change-username-form :input[name="userName"]');
		
            var csrftoken = getCookie('csrftoken');
            var uri = checkUsernameURI;
            var xhr = new XMLHttpRequest();
            var fd = new FormData();
            
            xhr.open("POST", uri, true);
            xhr.onreadystatechange = function() {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    // Handle response.
		            console.log(xhr.responseText);
                    var data = JSON.parse(xhr.responseText)
		            //console.log(data);
		    if (data.error) {
                        //alert(data.error);
                    }else{
                        if (data.exists == 'true'){
			    labelHolder.prepend(label);
			    if (badge.hasClass("register-check-good")) {
				badge.removeClass("register-check-good").addClass("register-check-error");
			    }
			    badge.fadeIn(300);
                        }else{
			    try{
				$('#change-username-form .my_error').fadeOut(300);
			    }catch(err){}
			    if (badge.hasClass("register-check-error")) {
				badge.removeClass("register-check-error").addClass("register-check-good");
			    }
			    badge.fadeIn(300);
			}
                    }
                }
            };
	        xhr.timeout = 4000;
	        xhr.ontimeout = function () { location.reload(); }
            fd.append('username', username);
            // Initiate a multipart/form-data upload
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            xhr.send(fd);
	    //console.log( xhr._object);
        }
	

    
    $('#change-username-form').ajaxForm({ 
        success:       function(responseText){
	    var labelHolder = $('#change-username-form :input[name="userName"]').parent().parent(),
		badge = $('#change-username-form :input[name="userName"]').next(),
		label = '<div class="error my_error">'+ responseText.error +'</div>',
		input = $('#change-username-form :input[name="userName"]');
		
            if (responseText.error) {
                //alert(responseText.error);
		labelHolder.prepend(label);
		if (badge.hasClass("register-check-good")) {
		    badge.removeClass("register-check-good").addClass("register-check-error");
		}
		badge.fadeIn(300);
		input.unbind("keyup").keyup(function(){
		    doesUsernameExist($(this).val());
		});
		
            }else if (responseText.username) {
		try{
		    $('#change-username-form .my_error').fadeOut(300);
		}catch(err){}
		if (badge.hasClass("register-check-error")) {
		    badge.removeClass("register-check-error").addClass("register-check-good");
		}
		badge.fadeIn(300);
		$("#username-label").html(responseText.username);
		input.unbind("keyup");
		$('#change-username').modal('hide');
		$('#change-username-form').resetForm();
		$('#change-username-form').clearForm();
		badge.fadeOut(300);
            }
        },
        dataType:  'json',
        timeout:   4000 
    }); 
    
    
    
    
});

