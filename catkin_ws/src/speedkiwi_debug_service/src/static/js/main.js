$(document).ready(function() {
  $('#robots-btn').on('click', function() {
    $('#bins-btn').addClass('unselected')
    updateFunction = updateRobots;
    $('#robots-btn').removeClass('unselected')
  });

  $('#bins-btn').on('click', function() {
    $('#robots-btn').addClass('unselected')
    updateFunction = updateBins;
    $('#bins-btn').removeClass('unselected')
  });

  updateFunction = updateRobots;

  setInterval(function () {
    updateFunction();
  }, 100);
});

function updateRobots() {
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

function updateBins() {
  $.ajax('http://127.0.0.1:1337/bins', {
    success: function(data, textStatus, xhr) {
      $('#robots').empty()
      $.each(data, function(key, val) {
        $('#robots').append('<div class="robot" id="' + key + '"></div>')
        $('#' + key).append('<h2>' + key + ' - Bin' + '</h2>')
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
