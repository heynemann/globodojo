module('Geracao de template');

test('Funcao retorna string sem valores', function() {
    var template = new Template('Aqui deve entrar $algumaCoisa$');
    var retorno = template.aplica({});
    equals(retorno, 'Aqui deve entrar $algumaCoisa$', 'Sem dicionário deve retornar string passada.');
});

test('Funcao que dispara erro quando a string de template nao e informada', function() {
    expect(1);
    
    try {
        var template = new Template();
    } catch(erro) {
        equals(erro, 'É necessário passar um template');
    }
});


test('Funcao que aplica variaveis ao template ', function() {
    expect(1);
    
    var template = new Template("Hi $foo$");
    var retorno = template.aplica({"foo": "bar"});
    equals(retorno, "Hi bar", 'As variaveis devem ser aplicadas a string');

});

test('Verifica que se variaveis nao forem passada retorna seu valor original ', function() {
    expect(1);
    
    var template = new Template("Hi $foo$ como esta $foo2$");
    var retorno = template.aplica({"foo": "bar"});
    equals(retorno, "Hi bar como esta $foo2$", 'As variaveis devem ser aplicadas a string');

});

test('Retorna lista de chaves no template', function() {
    expect(1);
    
    var template = new Template("Hi $foo$ como esta $foo$");
    var chaves = template.obtemChaves();
    equals(chaves, ['$foo$', '$foo$'], 'As variaveis devem ser aplicadas a string');

});

// test('Verifica que se a mesma variavel eh substituida mais de uma vez no mesmo template', function() {
//     expect(1);
//     
//     var template = new Template("Hi $foo$ como esta $foo$");
//     var retorno = template.aplica({"foo": "bar"})
//     equals(retorno, "Hi bar como esta bar", 'As variaveis devem ser aplicadas a string');
// 
// });

