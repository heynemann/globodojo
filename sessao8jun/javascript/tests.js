

module('Minesweep');

test('Verifica que um grid possui 4x4 de tamanho', function(){
   var minesweep = new Minesweep(4, 4);
   equals(minesweep.width, 4, 'Largura deveria ser quatro'); 
   equals(minesweep.height, 4, 'Altura deveria ser quatro'); 
});



test('Dado um array de strings, eh dada uma matriz como saida.', function() {
    var minesweep = new Minesweep(4, 4, ['....', '....', '....', '....']);
    
    equals(minesweep.result()[0][0], '.');
});
