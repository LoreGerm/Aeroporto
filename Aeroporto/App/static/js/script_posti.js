

function posti(posti) {
    //volo = document.getElementById('volo').value; // ID
    //console.log(volo);
    document.getElementById('tabella_posti').classList.remove('d-none');
    let n = posti;
    for (let i = 1; i <= n; i++) {
        document.getElementById('posti').append(fila(i));
    }
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

function ottieni_posti(){
    console.log('ciao');
    document.getElementById('id_volo').value = document.getElementById('volo').value;
}
