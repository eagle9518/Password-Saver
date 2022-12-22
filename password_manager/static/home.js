const csrftoken = getCookie('csrftoken');

const allRemoveCategoryButtons = document.getElementsByClassName("btn btn-danger")
for (let category of allRemoveCategoryButtons){
    category.addEventListener("click", function(){ deleteCategory(category.id)})
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

function deleteCategory(category_name){
    if (window.confirm("Are you sure you want to delete?")) {
        fetch(`${window.location.href}`, {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpResponse',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({'category_to_delete': category_name})
        }).then(response => {
            return response.json()
        }).then(data => {
            alert(data["Delete Message"])
            let deleted_category = document.getElementById(category_name)
            deleted_category.remove()
        })
    }
}





