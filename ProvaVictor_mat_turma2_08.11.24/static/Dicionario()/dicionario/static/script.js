 // Função para buscar palavras por letra inicial
 function handleAlphabetSearch(letter) {
    const searchResults = document.getElementById('searchResults');

    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: letter })
    })
    .then(response => response.json())
    .then(data => {
        searchResults.innerHTML = '';
        if (data.results.length > 0) {
            data.results.forEach(result => {
                const div = document.createElement('div');
                div.className = 'result-item';
                div.innerHTML = `<h3>${result.word}</h3><p>${result.description}</p>`;
                searchResults.appendChild(div);
            });
        } else {
            searchResults.innerHTML = '<p>Nenhum resultado encontrado.</p>';
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function handleAlphabetSearch(value) {
    document.getElementById('searchResults').value += value;
}
function clearResult() {
    document.getElementById('searchResults').value = '';
}