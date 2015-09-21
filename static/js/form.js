

function validateForm() {
console.log('hi')
	// var annualincome = document.forms["myForm"]["annualincome"].value;
	var annualIncome = $("#annualIncome").val();
	var monthlyPayment = $("#monthlyPayment").val();
	console.log(monthlyPayment);
	console.log(annualIncome);
	if annualIncome || monthlyPayment {
		return true
	}
	return false
}