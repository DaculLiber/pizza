// document.addEventListener('DOMContentLoaded', () => {

// });

// Variables
var content_array = [];
var retrievedData = localStorage.getItem("basket_content");
// console.log(JSON.parse(retrievedData));

$("document").ready(function(){

    const height_window = $(window).height();
    const height_body = $("body").height();

    if(height_body <= height_window)
    {
        $("#sticky-footer").addClass("py-4 text-white-50 fixed-bottom");
    }
    else
    {
        $("#sticky-footer").removeClass("fixed-bottom");
    }

});


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

// console.log(csrftoken);


function add_to_basket(id) {


    const pizza_name = $(`#${id}`).html();
    const pizza_price = $(`#price_${id}`).html();

    const obj = new Object();
    obj.name = pizza_name;
    obj.price = pizza_price;

    console.log(obj);

    content_array.push(obj);

    // JSON.stringify(content_array);
    localStorage.setItem("basket_content", JSON.stringify(content_array));

    console.log("content", content_array);


    $('#body_content').html(`${pizza_name} added to the basket!`);
    $('#alert').show();
    setTimeout(function() { 
        $('#alert').hide(); 
    }, 2000);


} 



/*

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


*/