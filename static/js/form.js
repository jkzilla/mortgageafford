
<script type="text/javascript">
	
	function validateForm() {
		var annualincome = document.forms["myForm"]["annualincome"].value;
		var monthlypayment = document.forms["myForm"]["monthlypayment"].value;
		var down = document.forms["myForm"]["down"].value;
		var monthlydebts = document.forms["myForm"]["monthlydebts"].value;
		var rate = document.forms["myForm"]["rate"].value;
		var schedule = document.forms["myForm"]["schedule"].value;
		var term = document.forms["myForm"]["term"].value;		
		var debttoincome = document.forms["myForm"]["debttoincome"].value;
		var incometax = document.forms["myForm"]["incometax"].value;
		var estimateyes = document.forms["myForm"]["estimateyes"].value;
		var estimateno = document.forms["myForm"]["estimateno"].value;
		var propertytax = document.forms["myForm"]["propertytax"].value;
		var hazardinsurance = document.forms["myForm"]["hazardinsurance"].value;
		var privatemortgage = document.forms["myForm"]["privatemortgage"].value;

		if (annualincome, monthlypayment, down, monthlydebts, rate, debttoincome % 1 === 0){
			alert("Please enter an integer value.")
			return false;
		}
		else {
			return true;
		}
	}	
	}
	}
		if monthlypayment == "" && annualincome == "" {
			//annualincome must have value
		alert("Please enter EITHER an annual income OR monthly payment value above.")
		return false;

		}
		if debttoincome == "" {
			debttoincome == 35;
			return true;
			//default is 35%
		}

</script>