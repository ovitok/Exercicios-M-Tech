function appendToResult(value) {
    document.getElementById('result').value += value;
}
function clearResult() {
    document.getElementById('result').value = '';
}
function deleteLast() {
    const resultField = document.getElementById('result');
    resultField.value = resultField.value.slice(0, -1); // Remove o ultimo caractere
}
function calculateResult() {
    const resultField = document.getElementById('result');
    try {
        const result = eval(resultField.value.replace('%','/100'));
        resultField.value = result;
} catch (error) {
    resultField.value = 'Erro'; //exibe 'erro' em caso erro de calculo
}
}
