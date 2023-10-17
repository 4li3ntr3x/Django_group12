$(document).ready(function() {
    // Oculta los contenidos completos de las publicaciones al cargar la página
    $(".post p").hide();
  
    // Maneja el botón "Leer más" solo si el contenido supera las 30 palabras
    $(".post").each(function() {
      var content = $(this).find("p");
      var words = content.text().split(' ');
      if (words.length > 30) {
        content.slice(0, 30).show();
        $(this).append('<button class="read-more-button">Leer más</button>');
      }
    });
  
    // Maneja el botón "Leer más" cuando se hace clic
    $(".read-more-button").on("click", function() {
      var post = $(this).closest(".post");
      post.find("p").show(); // Muestra el contenido completo
      $(this).hide(); // Oculta el botón "Leer más"
    });
  });
  
