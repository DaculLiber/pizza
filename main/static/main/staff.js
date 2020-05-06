

// Whenever the delete button is pressed the delete_func is called
// and makes an ajax call to our api to delete certain item (requires a staff user to access link)
function delete_func(id, pizza_name)
{
    const url = `/api/delete/${id}`;
    const req = new XMLHttpRequest();
    req.open('DELETE', url);
    
    req.setRequestHeader('X-CSRFToken', csrftoken);
    // req.setRequestHeader('content-type', 'application/json');


    req.onreadystatechange = function() { // Call a function when the state changes.
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            // Request finished. Do processing here.
        }
    }
    
    
    req.send();
    location.reload();
    $('#body_content').html(pizza_name);
    $('#alert').show();
    setTimeout(function() { 
        $('#alert').hide(); 
    }, 2000);

    
}


function delete_order(id)
{
    const url = `/api/done/${id}`;
    const req = new XMLHttpRequest();
    req.open('DELETE', url);
    req.setRequestHeader('X-CSRFToken', csrftoken);
    // req.setRequestHeader('content-type', 'application/json');

    req.onreadystatechange = function() { // Call a function when the state changes.
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            // Request finished. Do processing here.
        }
    }
    
    req.send();
    location.reload();
    $('#body_content').html("Order done!");
    $('#alert').show();
    setTimeout(function() { 
        $('#alert').hide(); 
    }, 2000);

    
}

