document.getElementById('importButton').addEventListener('click', function() {
    var input = document.createElement('input');
    input.type = 'file';
    input.webkitdirectory = true;
    input.onchange = function(event) {
        var folderPath = event.target.files[0].path;
        moveFilesToMedia(folderPath);
    };
    input.click();
});

function moveFilesToMedia(folderPath) {
    if (typeof folderPath !== 'undefined') {
        var formData = new FormData();
        formData.append('folder_path', folderPath);
        formData.append('csrfmiddlewaretoken', getCookie('csrftoken'));  // Include CSRF token
        fetch('/move_files/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Files moved to media successfully.');
            } else {
                alert('Failed to move files to media.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    } else {
        alert('Please select a folder.');
    }
}

// Function to retrieve CSRF token from cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
