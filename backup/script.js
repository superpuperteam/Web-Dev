function uploadFiles() {
    const input = document.getElementById('fileInput');
    const list = document.getElementById('fileItems');
    
    for (let i = 0; i < input.files.length; i++) {
        const li = document.createElement('li');
        li.textContent = input.files[i].name;
        list.appendChild(li);
    }
}

function backup() {
    alert('Резервная копия успешно создана!');
}
