	function validate_length () {
		q=document.getElementById('len').value; 	
		if (q.length<3) {
			document.getElementsByName('query')[0].value="";
			document.getElementsByName('query')[0].placeholder="enter atleast three letters";
			return false
		};
	}
