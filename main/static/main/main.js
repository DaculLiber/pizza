

console.log("Meow");


// document.addEventListener('DOMContentLoaded', () => {

// });


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

console.log(csrftoken);


function add_to_basket(id) {


    const pizza_name = document.getElementById(id).innerHTML;

    $('#body_content').html(pizza_name); 
    $('.toast').toast('show');

    console.log(pizza_name);



    const req = new XMLHttpRequest();
    req.open('POST', '/add-to-basket/');
    
    req.setRequestHeader('X-CSRFToken', csrftoken);
    req.setRequestHeader('content-type', 'application/json');



    req.onreadystatechange = function() { // Call a function when the state changes.
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            // Request finished. Do processing here.
        }
    }
    
    const pizza = {"pizza_name":`${pizza_name}`};
    console.log(typeof pizza);


    // req.send(`{"pizza_name":"${pizza_name}"}`);
    req.send(pizza);





    console.log('JSON SENT!');



} 