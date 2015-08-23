$(document).ready(function() {
  setInterval(function () {
    update();
  }, 100);
});

function update() {
  $.ajax('http://127.0.0.1:1337/robots', {
    success: function(data, textStatus, xhr) {
      $('#robots').empty()
      $.each(data, function(key, val) {
        $('#robots').append('<div class="robot" id="' + key + '"></div>')
        $('#' + key).append('<h2>' + key + ' - ' + val.type + '</h2>')
        $.each(val, function(innerKey, innerVal) {
          if (innerKey === 'type') {}
          else {
            $('#' + key).append('<span class="key">' + innerKey + ': </span>')
            $('#' + key).append('<span class="val">' + innerVal + '</span></br>')
          }
        });
      });
    },
    crossDomain: true
  });
}
