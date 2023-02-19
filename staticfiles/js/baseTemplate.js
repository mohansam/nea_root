$(document).ready(function() {
    $('.nav-link').click(function() {
      // Remove active class from all nav links
      $('.nav-link').removeClass('top-navbar-active');
  
      // Add active class to clicked nav link
      $(this).addClass('top-navbar-active');
  
      // Store active state in a cookie
      Cookies.set('activeNav', $(this).text());
    });
  
    // Retrieve active state from cookie and apply it on page load
    var activeNav = Cookies.get('activeNav');
    if (activeNav) {
      $('.nav-link').removeClass('top-navbar-active');
      $('.nav-link:contains(' + activeNav + ')').addClass('top-navbar-active');
    }
  });
  
  