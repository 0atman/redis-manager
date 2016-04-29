$( document ).ready(function() {


  // highlight all list-items if heading it checked
  $('.panel-title :checkbox').change(function() {
    checked = $(this).is(':checked');
    $(this).closest('.panel').find('.list-group-item').each(function() {
      if (checked) {
        $(this).find('input').prop('checked', true);
        $(this).addClass('list-group-item-success');
      }else{
        $(this).find('input').prop('checked', false);
        $(this).removeClass('list-group-item-success');
      }
    });
  });

  // highlight list-item when checkbox is checked
  $('.list-group-item :checkbox').change(function() {
    checked = $(this).is(':checked');
    if (checked == false) {
      $(this).closest(".panel").find(".panel-heading input").prop('checked', false);
    }
    $(this).closest(".list-group-item").toggleClass('list-group-item-success');
  });

  // search
  $('#derp').on('input',function(){
    search_text = $(this).val();
    console.log(search_text.length);
    $('.list-group-item').each(function() {
      message = $(this).text();
      if (search_text.length == 0){
        // reset highlighting
        original_message = $(this).find('.original-message').html();
        $(this).find('.displayed-message').html(original_message);
        $(this).show();
      }else if (message.indexOf(search_text) >= 0){
        // highlight search_text of message
        html = $(this).find('.original-message').html();
        html = html.replace(search_text, '<mark>' + search_text + '</mark>');
        $(this).find('.displayed-message').html(html);
        $(this).show();
      }else{
        // hide item
        $(this).hide();
      }
    });
  });


});
