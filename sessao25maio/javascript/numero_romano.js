
function converteRomano (val){
    if (val < 0){
        return 'Nao existe numero negativo em romano';
    }
    var decomposicao = decompoeNumero(val);
    var result;
    
    result = tranformaUnidadeRomano(decomposicao[3]);
    
    if (decomposicao[2] == 1){
        result = 'X';
    }
    if(decomposicao[2] == 4) {
        result = 'XL' + result;
    }
    return result;
};

function transformaUnidadeRomano(unidade) {
    switch(decomposicao[3]){
        case 1:
            result = 'I';
            break;
        case 3:
            result = 'III';
            break;
        case 5:
            result = 'V';
            break;
        case 7:
            result = 'VII';
            break;
        case 9:
            result = 'IX';
            break;    
            
    };
}

function decompoeNumero(numero){
    var milhar = Math.floor(numero / 1000);
    numero = numero-milhar*1000;
    
    var centena = Math.floor(numero / 100);
    numero = numero - centena * 100;
    
    var dezena = Math.floor(numero / 10);
    numero = numero - dezena *10;
    
    var unidade = Math.floor(numero)
    return [milhar, centena, dezena, numero];
}

