function showResponse(responseText, statusText)  { 
	if (statusText == 'success') {
		$('#contact-container').html('<h3>Message sent</h3>'); 
		$('#output').html('<p>Thanks for contacting us! We will check your message within a few minutes.</p>'); 
	} else {
		alert('status: ' + statusText + '\n\nSomething is wrong here');
	}
}

function showRequest(formData, jqForm, options) { 
	var form = jqForm[0];
	var validRegExp = /^[^@]+@[^@]+.[a-z]{2,}$/i;
	// or use 
	// if (!$('input[@name=email]').fieldValue()) { 
	if (!form.author.value) { 
		$('#output').html('<div class="output2">Please fill the Name field!</div>'); 
		return false; 
	} else if (!form.email.value) {
		$('#output').html('<div class="output2">Please fill the Email field!</div>'); 
		return false; 
	} else if (form.email.value.search(validRegExp) == -1) {
		$('#output').html('<div class="output2">Please provide a valid Email address!</div>'); 
		return false; 
	}
	else if (!form.title.value) {
		$('#output').html('<div class="output2">Please fill the Subject field!</div>'); 
		return false; 
	}
	else if (!form.message.value) {
		$('#output').html('<div class="output2">Please fill the Message field!</div>'); 
		return false; 
	}
	 else {	   
	 $('#output').html('Sending message...!');  		
		return true;
	}
}

$(document).ready(function() { 
    var options = { success: showResponse, beforeSubmit: showRequest}; 
    $('#my-form').submit(function() { 
        $(this).ajaxSubmit(options); 
        return false; 
    });
}); 