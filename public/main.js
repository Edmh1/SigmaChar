function getInput(){
    var code = document.getElementById("inputCode").value;
    sendCode(code);
}

function sendCode(code) {
    fetch('puerto que da el flask/analyzeCode', {
        method: 'POST',
        body: JSON.stringify({ code: code })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al enviar el código al backend');
        }
        return response.json();
    })
    .then(data => {
        console.log('Respuesta del backend:', data);
        if (data.error) {
            alert('Error en el análisis del código: ' + data.error);
        } else {
            var textarea = document.querySelector('.results-content');
            textarea.value = data.result;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocurrió un error al procesar el código');
    });
}