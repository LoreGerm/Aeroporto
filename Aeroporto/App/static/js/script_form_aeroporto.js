

function Form_indirizzo_appari(){
    document.getElementById('id_indirizzo').removeAttribute('required'); 
    document.getElementById('id_via').setAttribute('required', ''); 
    document.getElementById('id_numero').setAttribute('required', ''); 
    document.getElementById('id_citta').setAttribute('required', ''); 
    document.getElementById('id_provincia').setAttribute('required', ''); 
    document.getElementById('id_stato').setAttribute('required', ''); 
    document.getElementById('indirizzo').classList.add('d-none');
    document.getElementById('form-indirizzo').classList.remove('d-none');

}

function Form_indirizzo_scompari(){
    document.getElementById('id_indirizzo').setAttribute('required', '');
    document.getElementById('id_via').removeAttribute('required', ''); 
    document.getElementById('id_numero').removeAttribute('required', ''); 
    document.getElementById('id_citta').removeAttribute('required', ''); 
    document.getElementById('id_provincia').removeAttribute('required', ''); 
    document.getElementById('id_stato').removeAttribute('required', ''); 
    document.getElementById('indirizzo').classList.remove('d-none');
    document.getElementById('form-indirizzo').classList.add('d-none');
}