var Template  = function(template) {
    if (template === undefined) {
        throw "É necessário passar um template"
    }
    this.template = template;
        
    this.aplica = function(dicionario){
        var template = this.template;

        for(item in dicionario){
            template = template.replace("$"+item+"$", dicionario[item]);
        }
            
        return template;
    }
}

