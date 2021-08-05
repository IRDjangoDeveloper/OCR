$(document).ready(function(){
	const $myForm = $('#myform');
	$myForm.submit(function(event){
		event.preventDefault();
		const $formData = $myForm.serialize();
		const $thisURL = $myForm.attr('action') || window.loaction.href;
		$("#msg").html('<div class="spinner-border text-ligh" role="status"></div>');
		$.ajax({
			method:'POST',
			url: $thisURL,
			data: new FormData(this), // Data sent to server, a set of key/value pairs (i.e. form fields and values)
			contentType: false, // The content type used when sending data to the server.
			cache: false, // To unable request pages to be cached
			processData: false,
			// success: handleSuccess,
			// error: handleError,
			success: function(data) {
			if (data.ok) {
				document.getElementById('fma').innerHTML = data.text
				$("#msg").html(
            '<div class="alert alert-info" style="color: green"><i class="fa fa-check"> </i> کامل شد</div>'
          );
			}
			else {
				alert('خطایی رخ داده است،لطفا دوباره امتحان کنید.')
			}
		}
		});
	});
});