// Obtén todos los botones "Leer más"
var readMoreButtons = document.querySelectorAll('.read-more-button');

// Agrega un evento click a cada botón
readMoreButtons.forEach(function(button) {
  button.addEventListener('click', function() {
    // Encuentra el elemento .post padre del botón
    var post = button.closest('.post');
    
    // Agrega o quita la clase .expanded para mostrar u ocultar el contenido completo
    post.classList.toggle('expanded');
  });
});

