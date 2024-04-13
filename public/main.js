var originalDocumentation = null;

function getInput(){
    var code = document.getElementById("inputCode").value;
    sendCode(code);
}

function sendCode(code) {
    if(originalDocumentation == null){
        originalDocumentation = document.querySelector(".results-content").textContent;
        console.log(originalDocumentation);
    }
    fetch('http://127.0.0.1:5000/analyzeCode', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://127.0.0.1:5000',
            'Access-Control-Credentials' : 'true'
        },
        body: JSON.stringify({ codeInput: code })
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
            var textarea = document.getElementById("documentation");
            textarea.value = data.result;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocurrió un error al procesar el código');
    });
}

function back(){
    document.querySelector(".results-content").value = originalDocumentation;
}