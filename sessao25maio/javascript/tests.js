module('Numeros romanos');

test('Retorna milha de numero', function() {
   equals(decompoeNumero(2456)[0], 2);
   equals(decompoeNumero(898)[0], 0);
});

test('Retorna a centena de numero', function() {
   equals(decompoeNumero(2456)[1], 4);
   equals(decompoeNumero(898)[1], 8);
});

test('Retorna a dezena de numero', function() {
   equals(decompoeNumero(2456)[2], 5);
   equals(decompoeNumero(898)[2], 9);
});

test('Retorna a unidade de numero', function() {
   equals(decompoeNumero(2456)[3], 6);
   equals(decompoeNumero(898)[3], 8);
});

test('Convertendo 1 em romano', function(){
    
    var numeroRomano = converteRomano(1);
    equals(numeroRomano, 'I');
});

test('Convertendo 3 em romano', function(){
    
    var numeroRomano = converteRomano(3);
    equals(numeroRomano, 'III');
});

test('Convertendo 5 em romano', function(){
    
    var numeroRomano = converteRomano(5);
    equals(numeroRomano, 'V');
});

test('Convertendo 10 em romano', function(){
    
    var numeroRomano = converteRomano(10);
    equals(numeroRomano, 'X');
});

test('Convertendo 7 em romano', function(){
    var numeroRomano = converteRomano(7);
    equals(numeroRomano, 'VII');
});

test('Convertendo 49 em romano', function(){
    var numeroRomano = converteRomano(49);
    equals(numeroRomano, 'XLIX');
});

test('Erro ao converter um numero negativo', function(){
    var erro = converteRomano(-10);
    equals(erro, 'Nao existe numero negativo em romano');
});
