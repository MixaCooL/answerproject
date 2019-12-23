$(document).ready(function() {
    $("#top_country").on("submit", function(event) {
      event.preventDefault();
      $.ajax({
        type: "POST",
        url: "",
        headers: { action: "top_country" },
        data: {
          count: $("#count").val(),
          csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(response) {
          console.log(response)
          $('.table-content').empty();
          $(".table-content").prepend(`
          <table class="table">
          <thead>
          <tr>
            <th>Country Name</th>
            <th>Count users</th>
          </tr>
        </thead>
        </table>
            `);
          $.each(response,function(index,value) {
            $(".table").append(`
            <tr>
            <td>${index}</td>
            <td>${value}</td>
            </tr>
            `)
            });
        }
      });
    });
    $("#category_country").on("submit", function(event) {
        event.preventDefault();
        $.ajax({
          type: "POST",
          url: "",
          headers: { action: "category_country" },
          data: {
            category: $("#category").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
          },
          success: function(response) {
            console.log(response)
            $('.table-content').empty();
          $(".table-content").prepend(`
          <table class="table">
          <thead>
          <tr>
            <th>Country Name</th>
            <th>Count users</th>
          </tr>
        </thead>
        </table>
            `);
            $(".table").append(`
            <tr>
            <td>${response['Country']}</td>
            <td>${response['Count']}</td>
            </tr>
            `);
          }
        });
      });
      $("#times_of_day").on("submit", function(event) {
        event.preventDefault();
        var category = $("#times_of_day").find("#category").val();
        $.ajax({
          type: "POST",
          url: "",
          headers: { action: "times_of_day" },
          data: {
            category: $("#times_of_day").find("#category").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
          },
          success: function(response) {
            console.log(response)
            $('.table-content').empty();
          $(".table-content").prepend(`
          <div class="information">
          <div class="history-input-item-description history-input-item-description-select">
          Категорию ${response['category']} чаще всего просмтаривают ${response['times_of_day']}.</div>
          </div>
          `);
          }
        });
      });
  });
  