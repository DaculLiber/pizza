function update_func(id)
{
    console.log(id);
}


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

