

function genera_posti(id_volo='') {
    const API_VOLI = 'http://localhost:8000/apivolo/';
    const API_AEREI = 'http://localhost:8000/apiaereo/';
    fetch(API_VOLI+id_volo)
        .then(response => response.json())
        .then(data => {
            if(id_volo == ''){
                id_volo = parseInt(document.getElementById('volo').value);
            }
            else{
                id_volo = parseInt(id_volo);
            }


            content = {
                'prezzo_prima_classe': data[0].prezzo_unitario_prima_classe,
                'prezzo_seconda_classe': data[0].prezzo_unitario_seconda_classe,
                'prezzo_terza_classe': data[0].prezzo_unitario_terza_classe,
    
                'posti_prima_classe': data[0].aereo.posti_prima_classe,
                'posti_seconda_classe': data[0].aereo.posti_seconda_classe,
                'posti_terza_classe': data[0].aereo.posti_terza_classe,
                'posti': (data[0].aereo.posti_prima_classe + data[0].aereo.posti_seconda_classe + data[0].aereo.posti_terza_classe)/6,
            }

            document.getElementById('tabella_posti').classList.remove('d-none');
            for (let i = 1; i <= content.posti; i++){
                document.getElementById('posti').append(fila(i,content));
            }
        })
        .catch(err => console.log(err));
}


function prezzo_totale(){
    
}


function Resto(posti, i, classe, content){
    const node = document.createElement('tr');     
    let td = '<th scope="row">' + i + '</th>';
    let lettere = ['A', 'B', 'C', 'D', 'E', 'F'];
    let resto = posti%6;
    if(resto!=0){
        if (classe == 'prima'){
            for(let j=0 ; j<resto; j++){
                td += '<td><button type="button" id="'+ lettere[j] + i.toString() + '" class="btn btn-danger" onclick="scelta(this.id,'+content.prezzo_prima_classe+')"><img src="/static/img/poltrona.png" height=30 width=30></button></td>';
            }
        }
        else if (classe == 'seconda'){
            for(let j=0 ; j<resto; j++){
                td += '<td><button type="button" id="'+ lettere[j] + i.toString() + '" class="btn btn-primary" onclick="scelta(this.id,'+content.prezzo_prima_classe+')"><img src="/static/img/poltrona.png" height=30 width=30></button></td>';
            }            
        }
        else{
            for(let j=0 ; j<resto; j++){
                td += '<td><button type="button" id="'+ lettere[j] + i.toString() + '" class="btn btn-light" onclick="scelta(this.id,'+content.prezzo_prima_classe+')"><img src="/static/img/poltrona.png" height=30 width=30></button></td>';
            }   

        }
    }
    node.innerHTML = td;
    return node;
}


function fila(i,content) {
    const node = document.createElement('tr');
    let td = '<th scope="row">' + i + '</th>';
    let lettere = ['A', 'B', 'C', 'D', 'E', 'F'];
    for (let j = 0; j < 6; j++) {
        if (i <= content.posti_prima_classe/6){
            td += '<td><button type="button" id="'+ lettere[j] + i.toString() + '" class="btn btn-danger" onclick="scelta(this.id,'+content.prezzo_prima_classe+')"><img src="/static/img/poltrona.png" height=30 width=30></button></td>';
            Resto(content.posti_prima_classe, i,  'prima', content)
        }
        else if(i <= content.posti_seconda_classe/6){
            td += '<td><button type="button" id="'+ lettere[j] + i.toString() + '" class="btn btn-primary" onclick="scelta(this.id,'+content.prezzo_prima_classe+')"><img src="/static/img/poltrona.png" height=30 width=30></button></td>';
            Resto(content.posti_seconda_classe, i, 'seconda', content)
        }
        else{
            td += '<td><button type="button" id="'+ lettere[j] + i.toString() + '" class="btn btn-light" onclick="scelta(this.id,'+content.prezzo_prima_classe+')"><img src="/static/img/poltrona.png" height=30 width=30></button></td>';
            Resto(content.posti_terza_classe, i, 'terza', content)
        }
    }
    node.innerHTML = td;
    return node;
}

let posti_scelti = [];
function scelta(id, prezzo) {
    if (document.getElementById(id).classList == 'btn btn-light') {
        posti_scelti.push(id);
        document.getElementById('posti_prenotati').value = posti_scelti;
        let input_prezzo = document.getElementById('id_prezzo_totale').valueAsNumber;
        document.getElementById('id_prezzo_totale').value = input_prezzo + prezzo;
        document.getElementById(id).classList.remove('btn-light');
        document.getElementById(id).classList.add('btn-success');
    }
    else {
        posti_scelti.pop(id);
        document.getElementById('posti_prenotati').value = posti_scelti;
        let input_prezzo = document.getElementById('id_prezzo_totale').valueAsNumber;
        document.getElementById('id_prezzo_totale').value = input_prezzo - prezzo;
        document.getElementById(id).classList.remove('btn-success');
        document.getElementById(id).classList.add('btn-light');
    }
}

/*
function ottieni_posti(){
    const API_VOLI = 'http://localhost:8000/apivolo/';

    fetch(API_VOLI)
        .then(response => response.json())
        .then(data => {
            id_volo = parseInt(document.getElementById('volo').value)
            aereo = '';
            for(let i=0; i<data.length; i++){
                if(data[i].id == id_volo){
                    aereo=data[i].aereo;
                    break
                }
            }
            fetch(aereo)
                .then(response => response.json())
                .then(data => {
                    prima
                })
                .catch(err => console.log(err));
        })
        .catch(err => console.log(err));
}
*/