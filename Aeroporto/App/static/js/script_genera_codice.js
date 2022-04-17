function Genera_codice(){
    lettere = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',' Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'z']

    for(let i=0; i<document.getElementsByName('codice').length; i++){
        n_lettera = lettere[ Math.floor(Math.random() * 42)];
        document.getElementsByName('codice')[i].value =n_lettera + Math.floor((1 + Math.random()) * 0x10000).toString(16).substring(1);
    }
}