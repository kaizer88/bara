
$( document ).ready(function() {

    $("#stress").prop("disabled", true);
    $("#mcvar").prop("disabled", true);
    $("#headlines").prop("disabled", true);
    $("#headline_assets").prop("disabled", true);

});

$(function(){
  $('#types').change(function(e){

    $("#mcvar").prop("disabled", true);
    $("#headlines").prop("disabled", true);
    $("#headline_assets").prop("disabled", true);

      var myarray = $(e.target).val();

      if(jQuery.inArray("stress", myarray) != -1) {
        $("#stress").prop("disabled", false);
        }
      else {
          $("#stress").prop("disabled", true);
      }

      if(jQuery.inArray("mcvar", myarray) != -1) {
        $("#mcvar").prop("disabled", false);
        }
      else {
          $("#mcvar").prop("disabled", true);
      }

      if(jQuery.inArray("headlines", myarray) != -1) {
        $("#headlines").prop("disabled", false);
        }
      else {
          $("#headlines").prop("disabled", true);
      }

      if(jQuery.inArray("headline_assets", myarray) != -1) {
        $("#headline_assets").prop("disabled", false);
        }
      else {
          $("#headline_assets").prop("disabled", true);
      }


  })
})
