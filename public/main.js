var originalDocumentation = null;
var tokens = null;
var tokensJSON = null;

function getInput(){
    var code = document.getElementById("inputCode").value;
    code = code.replace(/[\r\n]+/g, ' ');
    sendCode(code);
}

function sendCode(code) {
    if(originalDocumentation == null){
        originalDocumentation = document.querySelector(".results-content").textContent;
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
            tokensJSON = JSON.stringify(data);
            tokens = JSON.parse(tokensJSON);
            console.log(tokens);
            showTokens(tokens);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocurrió un error al procesar el código');
    });
}

function showTokens(tokensJSON){
    var json = JSON.parse(JSON.stringify(tokensJSON));
    var tableResults = null;

    tableResults = 'Valor\tToken\n';
    Object.keys(json).forEach(index => {
        if(json[index].token == undefined){
            tableResults = `Hay un error en el código.\nDetalles: ${json[index].error} ${json[index].details}\n`
        }else{
            let token = json[index].token;
            let value = json[index].value;
    
            // Agregar cada token al string de la tabla
            tableResults += `${value}\t\t${token}\n`;
        }
    });

    // Mostrar el string de la tabla en el textarea
    var resultsTextarea = document.getElementById("documentation");
    resultsTextarea.value = tableResults;
}


function back(){
    document.querySelector(".results-content").value = originalDocumentation;
}