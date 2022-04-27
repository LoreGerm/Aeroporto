


function I_tuoi_voli(){
    let codice = document.getElementById('cerca').value;
    document.getElementById('prenotazioni').innerHTML = '<div id="modal"></div>';
    const API_PREN = 'http://localhost:8000/apiprenotazione/';

    fetch(API_PREN)
    .then(response => response.json())
    .then(data => {
        let cont = 0;
        for (let i=0; i<data.length; i++) {
            // Cerca e genera le prenotazioni
            if (data[i].codice == codice) {
                if (cont == 0){
                    document.getElementById('prenotazioni').append(Genera_card_prenotazioni(data[i], 'Andata'));
                    cont++;
                }
                else{
                    document.getElementById('prenotazioni').append(Genera_card_prenotazioni(data[i], 'Ritorno'));                    
                }
            }
        }

        /* Stampa gli errori se non ci sono voli
        if(document.getElementById('voli_andata').innerHTML == ''){
            document.getElementById('error').innerHTML = 'Voli non disponibili';
            document.getElementById('error').classList.remove('d-none'); 
            document.getElementById('voli_andata').classList.add('d-none');
            document.getElementById('div_voli').classList.add('d-none');
        }
        if(data_ritorno != '' && document.getElementById('voli_ritorno').innerHTML == ''){
            document.getElementById('error').innerHTML = 'Voli non disponibili';
            document.getElementById('error').classList.remove('d-none');
            document.getElementById('voli_ritorno').classList.add('d-none');
            document.getElementById('div_voli').classList.add('d-none');
        }*/
    
    
    })
    .catch(err => console.log(err));
}


function Genera_card_prenotazioni(pren, check){
    const node = document.createElement('div');
    node.classList.add('col');
    let card = '<div class="card mt-3 text-dark">'
                +'<h2 class="card-header"> Prenotazione '+check+' </h2>'
                +'<div class="card-body">'
                    +'<div class="mb-3">'
                        +'<h5 class="card-title">'+pren.utente.nome+' '+pren.utente.cognome+'</h5>'
                        +'<h5 class="card-text">'+pren.utente.email+'</h5>'
                        +'<h5 class="card-text">'+pren.utente.telefono+'</h5>'
                    +'</div>'
                    +'<div class="mb-3">'
                        +'<h5 class="card-text">'+pren.volo.aeroporto_di_partenza.nome+' --> '+pren.volo.aeroporto_di_arrivo.nome+' </h5>'
                        +'<h5 class="card-text">'+pren.volo.data_di_partenza+'  --> '+pren.volo.data_di_arrivo+' </h5>'
                        +'<h5 class="card-text">'+pren.volo.ora_di_partenza+'  --> '+pren.volo.ora_di_arrivo+'</h5>'
                        +'<h5 class="card-text">'+pren.posti_prenotati+' --> '+pren.prezzo_totale+' €</h5>'
                    +'</div>'
                    +'<div class="mt-4">'
                        +'<button data-bs-toggle="modal" data-bs-target="#modalElimina" class="btn btn-danger">Cancella</button>'
                    +'</div>'
                +'</div></div>';

    let modal = '<div class="modal fade" id="modalElimina" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">'
                +'<div class="modal-dialog">'
                +'<div class="modal-content">'
                    +'<div class="modal-header">'
                    +'<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>'
                    +'</div>'
                    +'<div class="modal-body">'
                    +'<h3 class="text-dark">Sei sicuro di voler eliminare la prenotazione?</h3>'
                    +'</div>'
                    +'<div class="modal-footer">'
                    +'<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Chiudi</button>'
                    +'<a href="i_tuoi_voli/'+pren.id+'" type="button" class="btn btn-danger">Elimina</a>'
                    +'</div>'
                +'</div>'
                +'</div>'
            +'</div>';
    node.innerHTML = card;
    document.getElementById('modal').innerHTML += modal;
    return node
}