"use strict";

const csrftoken = getCookie("csrftoken");

$("#signup_form").on("submit", function(event) {
    event.preventDefault();
    register_subscriber();
});

function register_subscriber() {
    $.ajax({
        url: "/register_subscriber/", // the endpoint
        type: "POST", // http method
        data: {
            username: $("#id_username").val()
        },

        success: function() {
            alert("WELCOME ABOARD: " + $("#id_username").val() + "!");
            $("#id_username").val(""); // remove the value from the input
        },

        error: function() {
            alert("INVALID USERNAME: " + $("#id_username").val() + "!");
            $("#id_username").val(""); // remove the value from the input
        }
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
