

function genera_posti(id_volo='') {
    console.log(id_volo);
    const API_VOLI = 'http://localhost:8000/apivolo/';
    fetch(API_VOLI)
        .then(response => response.json())
        .then(data => {
            if(id_volo == ''){
                id_volo = parseInt(document.getElementById('volo').value);
            }
            console.log(id_volo)
            let aereo = '';
            for(let i=0; i<data.length; i++){
                if(data[i].id == ''){
                    aereo=data[i].aereo;
                    break
                }
            }
            fetch(aereo)
                .then(response => response.json())
                .then(data => {
                    posti = parseInt(data.posti_prima_classe) + parseInt(data.posti_seconda_classe) + parseInt(data.posti_terza_classe);
                    document.getElementById('tabella_posti').classList.remove('d-none');
                    for (let i = 1; i <= posti; i++) {
                        document.getElementById('posti').append(fila(i));
                    }
                })
                .catch(err =>{
                    console.log(err) 
                    document.getElementById('posti').innerHTML = ''
                });
        })
        .catch(err => console.log(err));
    
    //volo = document.getElementById('volo').value; // ID
    //console.log(volo);
}

function fila(i) {
    const node = document.createElement('tr');
    let td = '<th scope="row">' + i + '</th>'
    let lettere = ['A', 'B', 'C', 'D', 'E', 'F'];
    for (let j = 0; j < 6; j++) {
        td += '<td><button type="button" id="'+ lettere[j] + i.toString() + '" class="btn btn-light" onclick="scelta(this.id)"><img src="/static/img/poltrona.png" height=30 width=30></button></td>';
    }
    node.innerHTML = td;
    return node;
}

let posti_scelti = [];
function scelta(id) {
    if (document.getElementById(id).classList == 'btn btn-light') {
        posti_scelti.push(id);
        document.getElementById('posti_prenotati').value = posti_scelti;
        document.getElementById(id).classList.remove('btn-light');
        document.getElementById(id).classList.add('btn-success');
    }
    else {
        posti_scelti.pop(id);
        document.getElementById('posti_prenotati').value = posti_scelti;
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