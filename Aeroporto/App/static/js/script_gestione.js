

function Genera_gestione_cerca(obj){

    let API = '';

    if(obj == 'voli'){
        API = 'http://localhost:8000/apivolo/';
    }
    else if(obj == 'pren'){
        API = 'http://localhost:8000/apiprenotazione/';
    }
    else if(obj == 'aeroporti'){
        API = 'http://localhost:8000/apiaeroporto/';
    }
    else if(obj == 'aerei'){
        API = 'http://localhost:8000/apiaereo/';
    }

    
    document.getElementById('thead').innerHTML = Genera_thead(obj);
    document.getElementById('tbody').innerHTML = '<div id="modal"> </div>';

    fetch(API)
    .then(response => response.json())
    .then(data => {

        for (let i = 0; i < data.length; i++) {
            if(data[i].codice.includes(document.getElementById('cerca').value)){
                document.getElementById('tbody').append(Genera_tbody(data[i], obj));
            }
        }

    })
    .catch(err => console.log(err));
}




function Genera_thead(obj){
    let thead = '';
    if(obj == 'voli'){
        thead = '<th>Codice</th>'
                    +'<th>Partenza</th>'
                    +'<th>Arrivo</th>'
                    +'<th>Prezzo 1° classe</th>'
                    +'<th>Prezzo 2° classe</th>'
                    +'<th>Prezzo 3° classe</th>'
                    +'<th>Posti totali</th>'
                    +'<th>Ora di partenza</th>'
                    +'<th>Ora di arrivo</th>'
                    +'<th>Data di partenza</th>'
                    +'<th>Data di arrivo</th>'
                    +'<th>Km</th>'
                    +'<th>Aereo</th>';
    }
    else if(obj == 'pren'){
        thead = '<th>Codice</th>'
                    +'<th>Nome utente</th>'
                    +'<th>Cognome utente</th>'
                    +'<th>email utente</th>'
                    +'<th>Telefono utente</th>'
                    +'<th>Codice volo</th>'
                    +'<th>Posti prenotati</th>'
                    +'<th>Prezzo totale</th>';
    }
    else if(obj == 'aeroporti'){
        thead = '<th>Codice</th>'
                    +'<th>Nome</th>'
                    +'<th>Descrizione</th>'
                    +'<th>Via</th>'
                    +'<th>Numero civico</th>'
                    +'<th>Stato</th>'
                    +'<th>Citta</th>'
                    +'<th>Provincia</th>';
    }
    else if(obj == 'aerei'){
        thead = '<th>Codice</th>'
                    +'<th>Modello</th>'
                    +'<th>Stato</th>'
                    +'<th>Km totali</th>'
                    +'<th>Km ultima manutenzione</th>'
                    +'<th>Data ultima manutenzione</th>'
                    +'<th>Posti 1° classe</th>'
                    +'<th>Posti 2° classe</th>'
                    +'<th>Posti 3° classe</th>';
    }
    return thead;
}



function Genera_tbody(data, obj){
    const tr = document.createElement('tr');
    let modal = '';
    let td = '';
    if(obj == 'voli'){
        let data_p = data.data_di_partenza.slice(8,10)+'/'+data.data_di_partenza.slice(5,7)+'/'+data.data_di_partenza.slice(0,4)
        let data_a = data.data_di_arrivo.slice(8,10)+'/'+data.data_di_arrivo.slice(5,7)+'/'+data.data_di_arrivo.slice(0,4)
        td = '<td>'+data.codice+'</td>'
                +'<td>'+data.aeroporto_di_partenza.nome+'</td>'
                +'<td>'+data.aeroporto_di_arrivo.nome+'</td>'
                +'<td>'+data.prezzo_unitario_prima_classe+' €</td>'
                +'<td>'+data.prezzo_unitario_seconda_classe+' €</td>'
                +'<td>'+data.prezzo_unitario_terza_classe+' €</td>'
                +'<td>'+data.posti_totali+'</td>'
                +'<td>'+data.ora_di_partenza.slice(0, 5)+'</td>'
                +'<td>'+data.ora_di_arrivo.slice(0, 5)+'</td>'
                +'<td>'+data_p+'</td>'
                +'<td>'+data_a+'</td>'
                +'<td>'+data.km+'</td>'
                +'<td>'+data.aereo.codice+'</td>'
                +'<td class="row">'
                +'<a href="voli/modifica/'+data.id+'" class="btn btn-success col">Modifica</a>'
                +'<button class="btn btn-danger col" data-bs-toggle="modal" data-bs-target="#'+data.codice+'">Elimina</button>'
                +'</td>';

        modal = '<div class="modal fade" id="'+data.codice+'" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">'
                    +'<div class="modal-dialog">'
                    +'<div class="modal-content">'
                        +'<div class="modal-header">'
                        +'<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>'
                        +'</div>'
                        +'<div class="modal-body">'
                        +'<h3 class="text-dark">Sei sicuro di voler eliminare il volo '+data.codice+'?</h3>'
                        +'</div>'
                        +'<div class="modal-footer">'
                        +'<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Chiudi</button>'
                        +'<a href="voli/'+data.id+'" type="button" class="btn btn-danger">Elimina</a>'
                        +'</div>'
                    +'</div>'
                    +'</div>'
                +'</div>';
    }
    else if(obj == 'pren'){
        td = '<td>'+data.codice+'</td>'
                +'<td>'+data.utente.nome+'</td>'
                +'<td>'+data.utente.cognome+'</td>'
                +'<td>'+data.utente.email+'</td>'
                +'<td>'+data.utente.telefono+'</td>'
                +'<td>'+data.volo.codice+'</td>'
                +'<td>'+data.posti_prenotati+'</td>'
                +'<td>'+data.prezzo_totale+'</td>'
                +'<td class="row">'
                +'<a href="prenotazioni/modifica/'+data.id+'" class="btn btn-success col">Modifica</a>'
                +'<button class="btn btn-danger col" data-bs-toggle="modal" data-bs-target="#'+data.codice+'">Elimina</button>'
                +'</td>';

        modal = '<div class="modal fade" id="'+data.codice+'" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">'
                    +'<div class="modal-dialog">'
                    +'<div class="modal-content">'
                        +'<div class="modal-header">'
                        +'<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>'
                        +'</div>'
                        +'<div class="modal-body">'
                        +'<h3 class="text-dark">Sei sicuro di voler eliminare la prenotazione '+data.codice+'?</h3>'
                        +'</div>'
                        +'<div class="modal-footer">'
                        +'<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Chiudi</button>'
                        +'<a href="prenotazioni/'+data.id+'" type="button" class="btn btn-danger">Elimina</a>'
                        +'</div>'
                    +'</div>'
                    +'</div>'
                +'</div>';
    }
    else if(obj == 'aeroporti'){
        td = '<td>'+data.codice+'</td>'
                +'<td>'+data.nome+'</td>'
                +'<td>'+data.descrizione+'</td>'
                +'<td>'+data.indirizzo.via+'</td>'
                +'<td>'+data.indirizzo.numero+'</td>'
                +'<td>'+data.indirizzo.stato+'</td>'
                +'<td>'+data.indirizzo.citta+'</td>'
                +'<td>'+data.indirizzo.provincia+'</td>'
                +'<td class="row">'
                +'<a href="aeroporti/modifica/'+data.id+'" class="btn btn-success col">Modifica</a>'
                +'<button class="btn btn-danger col" data-bs-toggle="modal" data-bs-target="#'+data.codice+'">Elimina</button>'
                +'</td>';
        
        modal = '<div class="modal fade" id="'+data.codice+'" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">'
                    +'<div class="modal-dialog">'
                    +'<div class="modal-content">'
                        +'<div class="modal-header">'
                        +'<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>'
                        +'</div>'
                        +'<div class="modal-body">'
                        +"<h3 class='text-dark'>Sei sicuro di voler eliminare l'aeroporto "+data.nome+"?</h3>"
                        +'</div>'
                        +'<div class="modal-footer">'
                        +'<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Chiudi</button>'
                        +'<a href="aeroporti/'+data.id+'" type="button" class="btn btn-danger">Elimina</a>'
                        +'</div>'
                    +'</div>'
                    +'</div>'
                +'</div>';
    }
    else if(obj == 'aerei'){
        let data_m = data.data_ultima_manutenzione.slice(8,10)+'/'+data.data_ultima_manutenzione.slice(5,7)+'/'+data.data_ultima_manutenzione.slice(0,4)
        td = '<td>'+data.codice+'</td>'
                +'<td>'+data.modello+'</td>'
                +'<td>'+data.stato+'</td>'
                +'<td>'+data.km_totali+'</td>'
                +'<td>'+data.km_da_ultima_manutenzione+'</td>'
                +'<td>'+data_m+'</td>'
                +'<td>'+data.posti_prima_classe+'</td>'
                +'<td>'+data.posti_seconda_classe+'</td>'
                +'<td>'+data.posti_terza_classe+'</td>'
                +'<td class="row">'
                +'<a href="aerei/modifica/'+data.id+'" class="btn btn-success col">Modifica</a>'
                +'<button class="btn btn-danger col" data-bs-toggle="modal" data-bs-target="#'+data.codice+'">Elimina</button>'
                +'</td>';

        modal = '<div class="modal fade" id="'+data.codice+'" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">'
                    +'<div class="modal-dialog">'
                    +'<div class="modal-content">'
                        +'<div class="modal-header">'
                        +'<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>'
                        +'</div>'
                        +'<div class="modal-body">'
                        +"<h3 class='text-dark'>Sei sicuro di voler eliminare l'aereo "+data.codice+"?</h3>"
                        +'</div>'
                        +'<div class="modal-footer">'
                        +'<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Chiudi</button>'
                        +'<a href="aereo/'+data.id+'" type="button" class="btn btn-danger">Elimina</a>'
                        +'</div>'
                    +'</div>'
                    +'</div>'
                +'</div>';
    }
    tr.innerHTML = td;
    document.getElementById('modal').innerHTML += modal;

    return tr
}