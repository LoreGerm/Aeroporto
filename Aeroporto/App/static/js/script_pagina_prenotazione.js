function Aumenta(){
    posti =parseInt(document.getElementById('n_posti').value);
    document.getElementById('n_posti').value = posti+1;
}

function Diminuisci(){
    posti =parseInt(document.getElementById('n_posti').value);
    if(posti != 0){
        document.getElementById('n_posti').value = posti-1;
    }
}



function Voli() {
    aeroporto_andata = document.getElementById('aeroporto_di_partenza').value;
    aeroporto_ritorno = document.getElementById('aeroporto_di_arrivo').value;
    data_andata = document.getElementById('data_andata').value;
    data_ritorno = document.getElementById('data_ritorno').value;
    n_posti = document.getElementById('n_posti').value;

    console.log(aeroporto_andata, aeroporto_ritorno, data_andata, data_ritorno, n_posti);

    const API_VOLI = 'http://localhost:8000/apivolo/';
    fetch(API_VOLI)
      .then(response => response.json())
      .then(data => {
        let voli = [];
        for (let i = 0; i < data.lenght; i++) {
          if (data[i].aeroporto_di_partenza.id == aeroporto_andata & data[i].aeroporto_di_arrivo.id == aeroporto_ritorno & data[i].data_di_partenza == data_andata & data[i].data_di_arrivo == data_ritorno & data[i].posti_totali >= n_posti) {
            console.log('mammita')
            voli.push(data);
          }
        }
        console.log(voli);
      })
      .catch(err => console.log(err));
}
