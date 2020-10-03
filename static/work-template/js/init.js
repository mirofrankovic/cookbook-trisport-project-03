(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space



const name = document.getElementById("name")
const email = document.getElementById("email")
const message = document.getElementById("message")
const form = document.getElementById("form")


form.addEventListener('submit', (e) => {
    e.preventDefault()
})



 $( "#form" ).submit(function( event ) {
                    alert( "Thank you for your email" ); 
                    event.preventDefault();
                  }); 
