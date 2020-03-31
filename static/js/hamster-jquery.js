
// function used in the start.html to change the displayed form
$(document).ready(function(){
				// if an element with the class "login_form_link" is clicked:
				// hide the element with the id "register_form" and display
				// the element with the id "login_form"
				$("#login_form_link").click(function(){
					$("#register_form").hide();
					$("#login_form").show();
					$(this.parentNode).addClass('active');
					$(document.getElementById('register_form_link').parentNode).removeClass('active');
				});
				// converse of the above
				$("#register_form_link").click(function(){
					$("#register_form").show();
					$("#login_form").hide();
					$(this.parentNode).addClass('active');
					$(document.getElementById('login_form_link').parentNode).removeClass('active');
				});
});

