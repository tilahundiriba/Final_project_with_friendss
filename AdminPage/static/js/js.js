document.getElementById('lab_test_type').addEventListener('change', function() {
    var selectedOption = this.options[this.selectedIndex];
    var labFee = selectedOption.getAttribute('data-fee');
    document.getElementById('payment_amount').value = labFee;
});