/* ---------- Loads modal to display information on payment ---------*/
$(window).on('load', function() {
    $('#paymentGuide').modal('show');
  });

/* ---------- Resets payment form and re-enables payment button ---------*/
$('#payment-reset').click(function() {
  $('#form-reset').trigger("reset");
  $('#submit_payment_btn').prop('disabled', false).val("Submit Payment");
});

/* ---------- changes text when payment form is submitted ---------*/
$('#payment-form').submit(function()
 {
    $("input[type='submit']", this)
      .val("Please Wait...");
    return true;
  });