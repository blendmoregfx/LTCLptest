$(document).ready( function(){

  $('input:radio[class="form-check-input"]').on("click", function(){

      var getradioValue = $(this).val();
      alert(getradioValue);

  });

});
