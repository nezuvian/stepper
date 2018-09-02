$(function() {
  console.log( "ready!" );

  $('#button').click(function() {
    $.get('/jquery', function(data) {
      $('#text').val(data.text);
    })
  });
});