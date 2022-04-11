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
    document.getElementById('div_voli').classList.remove('d-none');
    aeroporto_andata = document.getElementById('aeroporto_di_partenza').value;
    aeroporto_ritorno = document.getElementById('aeroporto_di_arrivo').value;
    data_andata = document.getElementById('data_andata').value;
    data_ritorno = document.getElementById('data_ritorno').value;
    n_posti = document.getElementById('n_posti').value;

    const API_VOLI = 'http://localhost:8000/apivolo/';
    fetch(API_VOLI)
    .then(response => response.json())
    .then(data => {
        let voli_andata = [];
        let voli_ritorno = [];
        for (let i=0; i<data.length; i++) {
            if (data[i].aeroporto_di_partenza.id == aeroporto_andata && data[i].aeroporto_di_arrivo.id == aeroporto_ritorno && data[i].data_di_partenza == data_andata && data[i].posti_totali >= n_posti) {
                voli_andata.push(data[i]);
            }
            else if (data[i].aeroporto_di_partenza.id == aeroporto_ritorno && data[i].aeroporto_di_arrivo.id == aeroporto_andata && data[i].data_di_partenza == data_ritorno && data[i].posti_totali >= n_posti){
                voli_ritorno.push(data[i]);
            }
        }
        
        for(let i=0; i<voli_andata.length; i++){
            document.getElementById('voli_andata').append(Genera_card(voli_andata[i]));
        }
        for(let i=0; i<voli_ritorno.length; i++){
            document.getElementById('voli_ritorno').append(Genera_card(voli_ritorno[i]));
        }
    
    })
    .catch(err => console.log(err));
}


function Genera_card(volo){
    const node = document.createElement('div');
    let card = '<div class="card mt-3 text-dark">'
                +'<div class="card-body">'
                +'<h5 class="card-subtitle mb-3">'+volo.aeroporto_di_partenza.nome+' --> '+volo.aeroporto_di_arrivo.nome+'</h5>'
                +'<h5 class="card-subtitle mb-3">'+volo.data_di_partenza+' --> '+volo.data_di_arrivo+'</h5>'
                +'<h5 class="card-subtitle mb-3">'+volo.ora_di_partenza+' --> '+volo.ora_di_arrivo+'</h5>'
                +'<h6 class="card-subtitle mb-3">Prima classe: '+volo.prezzo_unitario_prima_classe+' €</h6>'
                +'<h6 class="card-subtitle mb-3">Seconda classe: '+volo.prezzo_unitario_seconda_classe+' €</h6>'
                +'<h6 class="card-subtitle mb-3">Terza classe: '+volo.prezzo_unitario_terza_classe+' €</h6>'
                +'<div> <input type="checkbox" class="btn-check" name="andata" id="andata" autocomplete="off" value="{{v.id}}"><label class="btn btn-outline-success" for="andata">Seleziona</label></div>'
                +'</div></div>';
    node.innerHTML = card;
    return node
}
