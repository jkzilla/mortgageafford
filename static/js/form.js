	var form = $('#myForm');
	
	form.validate();
	
	$('#Submit').click(function() {
	
	console.log('hi');
	
	var $annualIncome = $('#annualIncome').val();
	var $monthlyPayment = $('#monthlyPayment').val();
	var $down = $('#down').val();

	if ($annualIncome != null) {
	// if an annualIncome is provided, continue to the next condition
		continue;
	}
	else if ($annualIncome === null && $monthlyPayment === null) {
	// do not submit
		return false;
	}
	else if ($annualIncome.length && $monthlyPayment.length === 0) {
		alert("Please enter either an annual income or a monthly payment.");
		return false;
	}
	else if ($down.length === 0) {
		alert("Please enter the amount of your down payment.");
		return false;
	}
	// do not submit form
	return true;
});
