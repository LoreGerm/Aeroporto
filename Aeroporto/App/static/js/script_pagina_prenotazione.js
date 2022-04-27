let API_URL = '192.168.1.254:8000';


function Aumenta(){     // Al click del + aumenta il numero dei posti
    posti =parseInt(document.getElementById('n_posti').value);
    if(posti < 15){     // Massimo 15 posti
        posti =parseInt(document.getElementById('n_posti').value);
        document.getElementById('n_posti').value = posti+1;
    }   
}

function Diminuisci(){     // Al click del - diminuisce il numero dei posti
    posti =parseInt(document.getElementById('n_posti').value);
    if(posti != 1){     // Minimo 1 posto
        document.getElementById('n_posti').value = posti-1;
    }
}


function radio_btn(id){
    // Azzera e nasconde i div dove vengono mostrati i voli
    document.getElementById('voli_andata').innerHTML = '<h1>Andata</h1>';
    document.getElementById('voli_ritorno').innerHTML = '<h1>Ritorno</h1>';
    document.getElementById('div_voli').classList.add('d-none');

    if(id=='andata-ritorno'){   // Se l'utente seleziona 'andata e ritorno'
        document.getElementById('div-data-ritorno').classList.remove('d-none'); // Mostra la data di ritorno
    }
    else{
        document.getElementById('div-data-ritorno').classList.add('d-none');  // Nasconde la data di ritorno
        document.getElementById('voli_ritorno').classList.add('d-none');  // Nasconde il div dei voli di ritorno
        document.getElementById('data_ritorno').value = '';  // Azzera la data di ritorno
    }
}


let andata = false
let ritorno = false
function btn_avanti(check){  // Abilita il bottone per andare avanti al click del volo
    let nome=''
    try {
        nome = check[0].name
    } catch {
        nome = check.name
    }

    if (nome=='andata'){
        andata = true
    }
    else{
        ritorno = true
    }
    if(document.getElementById('andata-ritorno').checked){  // Se l'utente ha selezionato andata e ritrono

        if(andata && ritorno){    // Se l'utente ha selezionato i voli
            // Abilita il bottone per andare avanti
            document.getElementById('avanti').classList.remove('opacity-50');
            document.getElementById('avanti').disabled = false;
        }
    }
    else{ // Se l'utente ha selezionato solo andata
        // Abilita il bottone per andare avanti
        document.getElementById('avanti').classList.remove('opacity-50');
        document.getElementById('avanti').disabled = false;        
    }

}



function Voli() {
    document.getElementById('voli_andata').innerHTML = '<h1>Andata</h1>';
    document.getElementById('voli_ritorno').innerHTML = '<h1>Ritorno</h1>';

    document.getElementById('avanti').classList.add('opacity-50');
    document.getElementById('avanti').disabled = true;

    aeroporto_andata = document.getElementById('aeroporto_di_partenza').value;
    aeroporto_ritorno = document.getElementById('aeroporto_di_arrivo').value;
    data_andata = document.getElementById('data_andata').value;
    data_ritorno = document.getElementById('data_ritorno').value;
    n_posti = document.getElementById('n_posti').value;

    if (n_posti <= 0 || n_posti > 15){     // Se il numero di posti selezionati è minore o ugale a 0 o maggiore di 15
        // Stampa l'errore
        document.getElementById('div_voli').classList.add('d-none');
        document.getElementById('error').innerHTML = 'Numero di posti non valido';
        document.getElementById('error').classList.remove('d-none');
    }
    else if(aeroporto_andata == '' || aeroporto_ritorno == ''){     // Se non vengono selezionati gli aeroporti
        // Stampa l'errore
        document.getElementById('div_voli').classList.add('d-none');
        document.getElementById('error').innerHTML = 'Selezionare gli aeroporti';
        document.getElementById('error').classList.remove('d-none');    
    }
    else if(data_andata == ''){     // Se non viene selezionata la data di andata
        // Stampa l'errore
        document.getElementById('div_voli').classList.add('d-none');
        document.getElementById('error').innerHTML = 'Selezionare la data di partenza';
        document.getElementById('error').classList.remove('d-none');   
    }
    else if(data_ritorno == '' && document.getElementById('andata-ritorno').checked){   // Se l'utente ha selezionato 'andata e ritorno' e non viene selezionata la data di ritorno
        // Stampa l'errore
        document.getElementById('div_voli').classList.add('d-none');
        document.getElementById('error').innerHTML = 'Selezionare la data di ritorno';
        document.getElementById('error').classList.remove('d-none');   
    }
    else{
        document.getElementById('error').innerHTML = '';
        document.getElementById('error').classList.add('d-none');

        if(data_ritorno != ''){
            document.getElementById('voli_ritorno').classList.remove('d-none');
        }
        document.getElementById('voli_andata').classList.remove('d-none');

        document.getElementById('div_voli').classList.remove('d-none');

        document.getElementById('posti').value = n_posti;

        const API_VOLI = 'http://'+API_URL+'/apivolo/';
        fetch(API_VOLI)
        .then(response => response.json())
        .then(data => {

            for (let i=0; i<data.length; i++) {
                // Cerca e genera i voli di andata
                if (data[i].aeroporto_di_partenza.id == aeroporto_andata && data[i].aeroporto_di_arrivo.id == aeroporto_ritorno && data[i].data_di_partenza == data_andata && data[i].posti_totali >= n_posti) {
                    document.getElementById('voli_andata').append(Genera_card(data[i], 'andata'));
                }
                // Cerca e genera i voli di ritorno
                else if (data_ritorno != '' && data[i].aeroporto_di_partenza.id == aeroporto_ritorno && data[i].aeroporto_di_arrivo.id == aeroporto_andata && data[i].data_di_partenza == data_ritorno && data[i].posti_totali >= n_posti){
                    document.getElementById('voli_ritorno').append(Genera_card(data[i], 'ritorno'));
                }
            }

            // Stampa gli errori se non ci sono voli
            if(document.getElementById('voli_andata').innerHTML == '<h1>Andata</h1>'){
                document.getElementById('error').innerHTML = 'Voli non disponibili';
                document.getElementById('error').classList.remove('d-none'); 
                document.getElementById('voli_andata').classList.add('d-none');
                document.getElementById('div_voli').classList.add('d-none');
            }
            if(data_ritorno != '' && document.getElementById('voli_ritorno').innerHTML == '<h1>Ritorno</h1>'){
                document.getElementById('error').innerHTML = 'Voli non disponibili';
                document.getElementById('error').classList.remove('d-none');
                document.getElementById('voli_ritorno').classList.add('d-none');
                document.getElementById('div_voli').classList.add('d-none');
            }
        
        
        })
        .catch(err => console.log(err));
    }
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
                +'<div class="form-check"> <input type="radio" class="form-check-input" onclick="btn_avanti('+check+')" name="'+check+'" id="'+check+volo.id+'" autocomplete="off" value="'+volo.codice+'"><label class="form-check-label" for="'+check+volo.id+'">Seleziona</label></div>'
                +'</div></div>';
    node.innerHTML = card;
    return node
}




