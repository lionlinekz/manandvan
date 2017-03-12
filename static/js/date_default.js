    $(document).ready(function () {
	    var date = new Date();
		var dd = date.getDate() + 1;             
		var mm = date.getMonth() + 1;
		var yyyy = date.getFullYear();
		var to_date = yyyy + '/' + mm + '/' + dd + ' 15:00';
        $('#dep-date').val(to_date);
    });
