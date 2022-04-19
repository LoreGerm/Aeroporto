function Aumenta(){
    posti =parseInt(document.getElementById('n_posti').value);
    document.getElementById('n_posti').value = posti+1;
}

function Diminuisci(){
    posti =parseInt(document.getElementById('n_posti').value);
    if(posti != 1){
        document.getElementById('n_posti').value = posti-1;
    }
}


function radio_btn(id){
    if(id=='andata-ritorno'){
        document.getElementById('div-data-ritorno').classList.remove('d-none');
        document.getElementById('voli_andata').innerHTML = '';
        document.getElementById('voli_ritorno').innerHTML = '';
        document.getElementById('div_voli').classList.add('d-none');
    }
    else{
        document.getElementById('div-data-ritorno').classList.add('d-none');    
        document.getElementById('voli_andata').innerHTML = '';
        document.getElementById('voli_ritorno').innerHTML = '';
        document.getElementById('voli_ritorno').classList.add('d-none');
        document.getElementById('div_voli').classList.add('d-none');
        document.getElementById('data_ritorno').value = '';
    }
}



function Voli() {    
    document.getElementById('voli_andata').innerHTML = '';
    document.getElementById('voli_ritorno').innerHTML = '';

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
            document.getElementById('voli_andata').append(Genera_card(voli_andata[i], 'andata'));
        }
        if(data_ritorno != ''){
            document.getElementById('voli_ritorno').classList.remove('d-none');
            for(let i=0; i<voli_ritorno.length; i++){
                document.getElementById('voli_ritorno').append(Genera_card(voli_ritorno[i], 'ritorno'));
            }
        }
    
    })
    .catch(err => console.log(err));
}


function Genera_card(volo, check){
    const node = document.createElement('div');
    let data_p = volo.data_di_partenza.slice(8,10)+'/'+volo.data_di_partenza.slice(5,7)+'/'+volo.data_di_partenza.slice(0,4)
    let data_a = volo.data_di_arrivo.slice(8,10)+'/'+volo.data_di_arrivo.slice(5,7)+'/'+volo.data_di_arrivo.slice(0,4)
    let card = '<div class="card mt-3 text-dark">'
                +'<div class="card-body">'
                +'<h5 class="card-subtitle mb-3">'+volo.aeroporto_di_partenza.nome+' --> '+volo.aeroporto_di_arrivo.nome+'</h5>'
                +'<h5 class="card-subtitle mb-3">'+data_p+' --> '+data_a+'</h5>'
                +'<h5 class="card-subtitle mb-3">'+volo.ora_di_partenza.slice(0, 5)+' --> '+volo.ora_di_arrivo.slice(0, 5)+'</h5>'
                +'<h6 class="card-subtitle mb-3">Prima classe: '+volo.prezzo_unitario_prima_classe+' €</h6>'
                +'<h6 class="card-subtitle mb-3">Seconda classe: '+volo.prezzo_unitario_seconda_classe+' €</h6>'
                +'<h6 class="card-subtitle mb-3">Terza classe: '+volo.prezzo_unitario_terza_classe+' €</h6>'
                +'<div> <input type="radio" class="btn-check" name="'+check+'" id="'+check+'" autocomplete="off" value="'+volo.codice+'"><label class="btn btn-outline-success" for="'+check+'">Seleziona</label></div>'
                +'</div></div>';
    node.innerHTML = card;
    return node
}
