var config = {
    host: 'machine-ip-address',
    port: 5200,
    mode: 'http',
    load_xml: function(xml_location, params, succeed, failed){
        $.ajax({
            url : "/xml/"+xml_location,
            type: 'GET',
            success: function(result,status,xhr) {
                succeed(xhr, params);
            },
            error: function(xhr,status,error) {
                failed();
            }
        });
    },
    error_modal: function (title, details){
      $('#error-display-modal').openModal();
      var error_title = document.getElementById("error-title");
      var error_details = document.getElementById("error-details");

      error_title.value = title;
      error_details.value = details;
    },
    account_moderation: 'True',
    content_moderation: 'False'
}
