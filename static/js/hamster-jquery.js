$(document).ready(function(){
				$(".login_form_link").click(function(){
					$("#register_form").hide();
					$("#login_form").show();
				});
				$(".register_form_link").click(function(){
					$("#register_form").show();
					$("#login_form").hide();
				});
			});