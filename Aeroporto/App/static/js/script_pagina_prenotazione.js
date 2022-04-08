function Aumenta(){
    posti =parseInt(document.getElementById('n_posti').value);
    document.getElementById('n_posti').value = posti+1;
}

function Diminuisci(){
    posti =parseInt(document.getElementById('n_posti').value);
    if(posti != 0){
        document.getElementById('n_posti').value = posti-1;
    }
}