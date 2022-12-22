const csrftoken = getCookie('csrftoken');

const allRemovePasswordButtons = document.getElementsByClassName("btn btn-danger")
for (let password of allRemovePasswordButtons){
    password.addEventListener("click", function(){ deletePassword(password.id)})
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function deletePassword(password_site) {
    if (window.confirm("Are you sure you want to delete")) {
        fetch(`${window.location.href}`, {
            method:'POST',
            credentials: "same-origin",
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpResponse',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({'password_to_delete': password_site})
        }).then(response =>{
            return response.json()
        }).then(data => {
            alert(data['Delete Message'])
            let deleted_password = document.getElementById(password_site)
            deleted_password.remove()
        })
    }
}