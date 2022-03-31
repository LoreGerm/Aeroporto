let n = 10;
for (let i = 1; i <= n; i++) {
    document.getElementById('posti').append(fila(i));
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

let posti = [];
function scelta(id) {
    if (document.getElementById(id).classList == 'btn') {
        posti.push(id);
        //document.getElementById('posti_prenotati').value = id;
        document.getElementById(id).classList.add('btn-success');
    }
    else {
        posti.pop(id);
        document.getElementById(id).classList.remove('btn-success');
    }
}