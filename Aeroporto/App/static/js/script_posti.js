

function posti(posti) {
    document.getElementById('tabella_posti').classList.remove('d-none');
    let n = posti;
    console.log(n);
    for (let i = 1; i <= n; i++) {
        document.getElementById('posti').append(fila(i));
    }
}

function fila(i) {
    const node = document.createElement('tr');
    let td = '<th scope="row">' + i + '</th>'
    let lettere = ['A', 'B', 'C', 'D', 'E', 'F'];
    for (let j = 0; j < 6; j++) {
        td += '<td><button type="button" id="' + i.toString() + lettere[j] + '" class="btn" onclick="scelta(this.id)"><img src="" height=30 width=30></button></td>';
    }
    node.innerHTML = td;
    return node;
}

let posti_scelti = [];
function scelta(id) {
    if (document.getElementById(id).classList == 'btn') {
        posti_scelti.push(id);
        document.getElementById('posti_prenotati').value = posti_scelti;
        document.getElementById(id).classList.add('btn-success');
    }
    else {
        posti_scelti.pop(id);
        document.getElementById('posti_prenotati').value = posti_scelti;
        document.getElementById(id).classList.remove('btn-success');
    }
}