function Genera(){
    lettere = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',' Z']
    n_lettera = lettere[ Math.floor(Math.random() * 21)];

    for(let i=0; i<document.getElementsByName('codice').length; i++){
        document.getElementsByName('codice')[i].value =n_lettera + Math.floor((1 + Math.random()) * 0x10000).toString(16).substring(1);
    }
}