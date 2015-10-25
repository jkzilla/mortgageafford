var main = function() {

	var form = $('#myForm');
	
	form.validate();
	
	$('#Submit').click(function() {
	
	console.log('hi')
	
	var $annualIncome = $('#annualIncome').val();
	var $monthlyPayment = $('#monthlyPayment').val();
	var $down = $('#down').val();

	if ($annualIncome != null) {
		return true;
	}
	else if ($annualIncome.length === 0 && $monthlyPayment.length != 0) {
		// submit form
		return true;
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
}
);

$(document).ready(main);