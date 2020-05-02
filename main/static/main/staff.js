

// Whenever the delete button is pressed the delete_func is called
// and makes an ajax call to our api to delete certain item (requires a staff user to access link)
function delete_func(id)
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
    
    location.reload();
    req.send();
}

