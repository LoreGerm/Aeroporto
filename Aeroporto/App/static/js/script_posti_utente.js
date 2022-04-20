


let posti_scelti = [];
function Posti(id_volo='', id_div_posti='', volo_ritorno='', posti=''){
    
    document.getElementById('btn-avanti').disabled = true;
    document.getElementById('btn-avanti').classList.add('opacity-25');

    if(id_div_posti == ''){
        document.getElementById('tabella_posti').classList.remove('d-none');
    }
    else if(id_div_posti == 'andata' && volo_ritorno!=''){
        document.getElementById('btn-ritorno').classList.remove('d-none');
        document.getElementById('btn-andata').classList.add('d-none');

        document.getElementById('ritorno').classList.add('d-none');
        document.getElementById('andata').classList.remove('d-none');
    }
    else if(id_div_posti == 'ritorno' && volo_ritorno!=''){
        document.getElementById('form').classList.remove('d-none');

        document.getElementById('btn-ritorno').classList.add('d-none');

        document.getElementById('andata').classList.add('d-none');
        document.getElementById('ritorno').classList.remove('d-none');
    }
    else{
        document.getElementById('btn-andata').classList.add('d-none');
        document.getElementById('form').classList.remove('d-none');

        document.getElementById('ritorno').classList.add('d-none');
        document.getElementById('andata').classList.remove('d-none');        
    }

    posti_scelti = [];
    if(id_volo == ''){
        id_volo = parseInt(document.getElementById('volo').value);
    }
    else{
        id_volo = parseInt(id_volo);
    }
    const API_PREN = 'http://localhost:8000/apiprenotazione/';
    fetch(API_PREN)
        .then(response => response.json())
        .then(data => {

            let posti_prenotati = '';
            for(let i=0; i<data.length; i++){
                if(data[i].volo.id == id_volo){
                    posti_prenotati += data[i].posti_prenotati+',';
                }
            }

            posti_prenotati = posti_prenotati.split(',');
            Genera_posti(id_volo, posti_prenotati, id_div_posti, posti)
        })
        .catch(err => console.log(err));
    
}


function Genera_posti(id_volo, posti_prenotati, id_div_posti, posti) {
    document.getElementById('prezzo_totale_'+id_div_posti).value = 0;
    document.getElementById('posti_'+id_div_posti).innerHTML = '';
    const API_VOLI = 'http://localhost:8000/apivolo/';
    fetch(API_VOLI+id_volo)
        .then(response => response.json())
        .then(data => {
            content = {
                'prezzo_prima_classe': data.prezzo_unitario_prima_classe,
                'prezzo_seconda_classe': data.prezzo_unitario_seconda_classe,
                'prezzo_terza_classe': data.prezzo_unitario_terza_classe,
    
                'posti_prima_classe': data.aereo.posti_prima_classe,
                'posti_seconda_classe': data.aereo.posti_seconda_classe,
                'posti_terza_classe': data.aereo.posti_terza_classe,
                'posti': (data.aereo.posti_prima_classe + data.aereo.posti_seconda_classe + data.aereo.posti_terza_classe)/6,
            }

            document.getElementById(id_div_posti).classList.remove('d-none');
            document.getElementById('tabella_posti').classList.remove('d-none');

            for (let i = 1; i <= content.posti; i++){
                document.getElementById('posti_'+id_div_posti).append(Fila(i,content, posti_prenotati, id_div_posti, posti));
            }
        })
        .catch(err => console.log(err));
}



function Fila(i,content, posti_prenotati, id_div_posti, posti) {
    const node = document.createElement('tr');
    let td = '<th scope="row">' + i + '</th>';
    let lettere = ['A', 'B', 'C', 'D', 'E', 'F'];
    for (let j = 0; j < 6; j++) {

        if(!posti_prenotati.includes(lettere[j] + i.toString())){
            if (content.posti_prima_classe!=0){
                td += '<td><button type="button" id="'+ lettere[j] + i.toString() + '" value="'+ lettere[j] + i.toString() + '" class="btn btn-warning" onclick="Scelta(this.id,'+content.prezzo_prima_classe+', '+id_div_posti+', '+posti+')"><img src="/static/img/poltrona.png" height=30 width=30></button></td>';
                content.posti_prima_classe--;
            }
            else if(content.posti_seconda_classe!=0){
                td += '<td><button type="button" id="'+ lettere[j] + i.toString() + '" value="'+ lettere[j] + i.toString() + '" class="btn btn-primary" onclick="Scelta(this.id,'+content.prezzo_seconda_classe+', '+id_div_posti+', '+posti+')"><img src="/static/img/poltrona.png" height=30 width=30></button></td>';
                content.posti_seconda_classe--;
            }
            else{
                td += '<td><button type="button" id="'+ lettere[j] + i.toString() + '" value="'+ lettere[j] + i.toString() + '" class="btn btn-light" onclick="Scelta(this.id,'+content.prezzo_terza_classe+', '+id_div_posti+', '+posti+')"><img src="/static/img/poltrona.png" height=30 width=30></button></td>';
            }
        }
        else{
            if (content.posti_prima_classe!=0){
                td += '<td><button type="button" id="'+ lettere[j] + i.toString() + '" value="'+ lettere[j] + i.toString() + '" class="btn btn-warning opacity-50" disabled"><img src="/static/img/poltrona_disable.png" height=30 width=30></button></td>';
                content.posti_prima_classe--;
            }
            else if(content.posti_seconda_classe!=0){
                td += '<td><button type="button" id="'+ lettere[j] + i.toString() + '" value="'+ lettere[j] + i.toString() + '" class="btn btn-primary opacity-50" disabled"><img src="/static/img/poltrona_disable.png" height=30 width=30></button></td>';
                content.posti_seconda_classe--;
            }
            else{
                td += '<td><button type="button" id="'+ lettere[j] + i.toString() + '" value="'+ lettere[j] + i.toString() + '" class="btn btn-light opacity-50" disabled"><img src="/static/img/poltrona_disable.png" height=30 width=30></button></td>';
            }
        }
    }
    node.innerHTML = td;
    return node;
}



function Scelta(id, prezzo, id_div_posti, posti) {
        if (!posti_scelti.includes(id)) {
            posti_scelti.push(id);
            document.getElementById('posti_prenotati_'+id_div_posti.id).value = posti_scelti;
            let input_prezzo = document.getElementById('prezzo_totale_'+id_div_posti.id).valueAsNumber;
            document.getElementById('prezzo_totale_'+id_div_posti.id).value = input_prezzo + prezzo;
            document.getElementById('posti_'+id_div_posti.id).querySelector('#'+id).classList.add('btn-lg');
            document.getElementById('posti_'+id_div_posti.id).querySelector('#'+id).classList.add('border');
            document.getElementById('posti_'+id_div_posti.id).querySelector('#'+id).classList.add('border-success');
            document.getElementById('posti_'+id_div_posti.id).querySelector('#'+id).classList.add('border-5');
        }
        else {
            posti_scelti.pop(id);
            document.getElementById('posti_prenotati_'+id_div_posti.id).value = posti_scelti;
            let input_prezzo = document.getElementById('prezzo_totale_'+id_div_posti.id).valueAsNumber;
            document.getElementById('prezzo_totale_'+id_div_posti.id).value = input_prezzo - prezzo;
            document.getElementById('posti_'+id_div_posti.id).querySelector('#'+id).classList.remove('btn-lg');
            document.getElementById('posti_'+id_div_posti.id).querySelector('#'+id).classList.remove('border');
            document.getElementById('posti_'+id_div_posti.id).querySelector('#'+id).classList.remove('border-success');
            document.getElementById('posti_'+id_div_posti.id).querySelector('#'+id).classList.remove('border-5');
        }
        
    if(posti_scelti.length == posti){
        document.getElementById('btn-avanti').disabled = false;
        document.getElementById('btn-avanti').classList.remove('opacity-25');
    }
    else{
        document.getElementById('btn-avanti').disabled = true;
        document.getElementById('btn-avanti').classList.add('opacity-25');        
    }
}


