

$(document).ready(function validateForm() {
	console.log('hi')
	
	var $annualIncome = $("#annualIncome").val();
	var $monthlyPayment = $("#monthlyPayment").val();
	console.log(monthlyPayment);
	console.log(annualIncome);
	if $annualIncome.length != 0 {
		return true;
	}
	else if $annualIncome.length === 0 && $monthlyPayment.length != 0 {
		// submit form
		return true;
	}
	else if $annualIncome.length && $monthlyPayment.length === 0 {
		alert("Please enter either an annual income or a monthly payment.")
		return false;
	}
	// do not submit form
	alert("Please fill out values correctly");
	return false;
}
)