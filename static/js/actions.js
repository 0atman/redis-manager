$( document ).ready(function() {

  // move queue items
  $('.btn').click(function() {
    var move_messages_to = $('input[type=text]').val();
    var messages_to_move = get_messages_to_move();
    var action = $(this).text();
    console.log(messages_to_move)
    $.ajax({
      type: 'POST',
      url: 'action_messages',
      data: JSON.stringify({
        action: action,
        move_messages_to: move_messages_to,
        messages_to_move: messages_to_move,
      }),
      contentType: 'application/json; charset=utf-8',
      dataType: 'json'
    });
    location.reload();
  });

  // get queues with messages we want to move
  function get_messages_to_move(){
    var messages_to_move = []
    $('.panel').each(function() {
      queue_name = $(this).find('.panel-title span').text();

      messages_in_queue = [];
      messages = $(this).find('input:checked').siblings();
      messages.each(function() {
        message = $(this).find('.original-message').text();
        messages_in_queue.push(message);
      });

      messages_to_move.push({name: queue_name, messages:messages_in_queue});
    });
    return messages_to_move;
  }


});
