// ---- navbar burger handling ---- //
document.addEventListener('DOMContentLoaded', () => {
  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {
    // Add a click event on each of them
    $navbarBurgers.forEach( el => {
      el.addEventListener('click', () => {
        // Get the target from the "data-target" attribute
        const target = el.dataset.target;
        const $target = document.getElementById(target);
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');
      });
    });
  }
});

// ----- enable website sections ----- //
function showHome(){
  var home = document.getElementById("section-home");
  var attivita = document.getElementById("section-attivita");
  var approfondimenti = document.getElementById("section-approfondimenti");
  home.classList.remove('is-hidden');
  attivita.classList.add('is-hidden');
  approfondimenti.classList.add('is-hidden');
}
function showAttivita(){
  var home = document.getElementById("section-home");
  var attivita = document.getElementById("section-attivita");
  var approfondimenti = document.getElementById("section-approfondimenti");
  home.classList.add('is-hidden');
  attivita.classList.remove('is-hidden');
  approfondimenti.classList.add('is-hidden');
}
function showApprofondimenti(){
  var home = document.getElementById("section-home");
  var attivita = document.getElementById("section-attivita");
  var approfondimenti = document.getElementById("section-approfondimenti");
  home.classList.add('is-hidden');
  attivita.classList.add('is-hidden');
  approfondimenti.classList.remove('is-hidden');
}


// ----- check hash changes in order to display correct sections ----- //
var hash = window.location.hash;
setInterval(function(){
    if (window.location.hash != hash) {
        hash = window.location.hash;
        if (hash == '#approfondimenti') {
          showApprofondimenti();
        }
        if (hash == '#attivita') {
          showAttivita();
        } else {
          showHome();
        }
    }
}, 100);