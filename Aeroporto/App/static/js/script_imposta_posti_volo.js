

// Nella creazione del voli alla scelta dell'aereo scrive nell'input nascosto il numero di posti totali dell'aereo scelto che per salvarli nel volo
function Imposta_posti_volo(){

    const API_PREN = 'http://localhost:8000/apiaereo/';
    fetch(API_PREN + document.getElementById('aereo').value)
        .then(response => response.json())
        .then(data => {
            
            document.getElementById('posti_totali').value = data.posti_prima_classe + data.posti_seconda_classe + data.posti_terza_classe;

        })
        .catch(err => console.log(err));
}