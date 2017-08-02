$(function () {
  var page_title = $(document).attr("title");

  function hide_stream_update() {
    $(".stream-update").hide();
    $(".stream-update .new-posts").text("");
    $(document).attr("title", page_title);
  };

  $("body").keydown(function (evt) {
    var keyCode = evt.which?evt.which:evt.keyCode;
    if (evt.ctrlKey && keyCode == 80) {
      $(".btn-compose").click();
      return false;
    }
  });

  $("#compose-form textarea[name='post']").keydown(function (evt) {
    var keyCode = evt.which?evt.which:evt.keyCode;
    if (evt.ctrlKey && (keyCode == 10 || keyCode == 13)) {
      $(".btn-post").click();
    }
  });

  $(".btn-compose").click(function () {
    if ($(".compose").hasClass("composing")) {
      $(".compose").removeClass("composing");
      $(".compose").slideUp();
    }
    else {
      $(".compose").addClass("composing");
      // $(".compose input").val("");
      // $(".compose textarea").val("");
      $(".compose").slideDown(400, function () {
        $("#id_title").focus();
      });
    }
  });

  $(".btn-cancel-compose").click(function () {
    $(".compose").slideUp();
  });

  $(".btn-post").click(function () {
    var last_event = $(".stream li:first-child").attr("event-id");
    if (last_event == undefined) {
      last_event = "0";
    }
    $("#compose-form input[name='last_event']").val(last_event);
    $.ajax({
      url: '/events/post/',
      data: $("#compose-form").serialize(),
      type: 'post',
      cache: false,
      success: function (data) {
        $("ul.stream").prepend(data);
        $(".compose").slideUp();
        $(".compose").removeClass("composing");
        hide_stream_update();
      }
    });
  });

  $("ul.stream").on("click", ".like", function () {
    var li = $(this).closest("li");
    var event = $(li).attr("event-id");
    var csrf = $(li).attr("csrf");
    $.ajax({
      url: '/events/like/',
      data: {
        'event': event,
        'csrfmiddlewaretoken': csrf
      },
      type: 'post',
      cache: false,
      success: function (data) {
        if ($(".like", li).hasClass("unlike")) {
          $(".like", li).removeClass("unlike");
          $(".like .text", li).text("Like");
        }
        else {
          $(".like", li).addClass("unlike");
          $(".like .text", li).text("Unlike");
        }
        $(".like .like-count", li).text(data);
      }
    });
    return false;
  });

  $("ul.stream").on("click", ".comment", function () { 
    var post = $(this).closest(".post");
    if ($(".comments", post).hasClass("tracking")) {
      $(".comments", post).slideUp();
      $(".comments", post).removeClass("tracking");
    }
    else {
      $(".comments", post).show();
      $(".comments", post).addClass("tracking");
      $(".comments input[name='post']", post).focus();
      var event = $(post).closest("li").attr("event-id");
      $.ajax({
        url: '/events/comment/',
        data: { 'event': event },
        cache: false,
        beforeSend: function () {
          $("ol", post).html("<li class='loadcomment'><img src='/static/img/loading.gif'></li>");
        },
        success: function (data) {
          $("ol", post).html(data);
          $(".comment-count", post).text($("ol li", post).not(".empty").length);
        }
      });
    }
    return false;
  });

  $("ul.stream").on("keydown", ".comments input[name='post']", function (evt) {
    var keyCode = evt.which?evt.which:evt.keyCode;
    if (keyCode == 13) {
      var form = $(this).closest("form");
      var container = $(this).closest(".comments");
      var input = $(this);
      $.ajax({
        url: '/events/comment/',
        data: $(form).serialize(),
        type: 'post',
        cache: false,
        beforeSend: function () {
          $(input).val("");
        },
        success: function (data) {
          $("ol", container).html(data);
          var post_container = $(container).closest(".post");
          $(".comment-count", post_container).text($("ol li", container).length);
        }
      });
      return false;
    }
  });

  var load_events = function () {
    if (!$("#load_event").hasClass("no-more-events")) {
      var page = $("#load_event input[name='page']").val();
      var next_page = parseInt($("#load_event input[name='page']").val()) + 1;
      $("#load_event input[name='page']").val(next_page);
      $.ajax({
        url: '/events/load/',
        data: $("#load_event").serialize(),
        cache: false,
        beforeSend: function () {
          $(".load").show();
        },
        success: function (data) {
          if (data.length > 0) {
            $("ul.stream").append(data)
          }
          else {
            $("#load_event").addClass("no-more-events");
          }
        },
        complete: function () {
          $(".load").hide();
        }
      });
    }
  };

  $("#load_event").bind("enterviewport", load_events).bullseye();

  function check_new_events () {
    var last_event = $(".stream li:first-child").attr("event-id");
    var event_source = $("#event_source").val();
    if (last_event != undefined) {
      $.ajax({
        url: '/events/check/',
        data: {
          'last_event': last_event,
          'event_source': event_source
        },
        cache: false,
        success: function (data) {
          if (parseInt(data) > 0) {
            $(".stream-update .new-posts").text(data);
            $(".stream-update").show();
            $(document).attr("title", "(" + data + ") " + page_title);
          }
        },
        complete: function() {
          window.setTimeout(check_new_events, 30000);
        }
      });
    }
    else {
      window.setTimeout(check_new_events, 30000);
    }
  };
  check_new_events();

  $(".stream-update a").click(function () {
    var last_event = $(".stream li:first-child").attr("event-id");
    var event_source = $("#event_source").val();
    $.ajax({
      url: '/events/load_new/',
      data: { 
        'last_event': last_event,
        'event_source': event_source
      },
      cache: false,
      success: function (data) {
        $("ul.stream").prepend(data);
      },
      complete: function () {
        hide_stream_update();
      }
    });
    return false;
  });

  $("input,textarea").attr("autocomplete", "off");

  function update_events () {
    var first_event = $(".stream li:first-child").attr("event-id");
    var last_event = $(".stream li:last-child").attr("event-id");
    var event_source = $("#event_source").val();

    if (first_event != undefined && last_event != undefined) {
      $.ajax({
        url: '/events/update/',
        data: {
          'first_event': first_event,
          'last_event': last_event,
          'event_source': event_source
        },
        cache: false,
        success: function (data) {
          $.each(data, function(id, event) {
              var li = $("li[event-id='" + id + "']");
              $(".like-count", li).text(event.likes);
              $(".comment-count", li).text(event.comments);
          });
        },
        complete: function () {
          window.setTimeout(update_events, 30000);
        }
      });
    }
    else {
      window.setTimeout(update_events, 30000);
    }
  };
  update_events();

  function track_comments () {
    $(".tracking").each(function () {
      var container = $(this);
      var event = $(this).closest("li").attr("event-id");
      $.ajax({
        url: '/events/track_comments/',
        data: {'event': event},
        cache: false,
        success: function (data) {
          $("ol", container).html(data);
          var post_container = $(container).closest(".post");
          $(".comment-count", post_container).text($("ol li", container).length);
        }
      });
    });
    window.setTimeout(track_comments, 30000);
  };
  track_comments();

  $("ul.stream").on("click", ".remove-event", function () {
    var li = $(this).closest("li");
    var event = $(li).attr("event-id");
    var csrf = $(li).attr("csrf");
    $.ajax({
      url: '/events/remove/',
      data: {
        'event': event,
        'csrfmiddlewaretoken': csrf
      },
      type: 'post',
      cache: false,
      success: function (data) {
        $(li).fadeOut(400, function () {
          $(li).remove();
        });
      }
    });
  });

  $("#compose-form textarea[name='post']").keyup(function () {
    $(this).count(255);
  });

});