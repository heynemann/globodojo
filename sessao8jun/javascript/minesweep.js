var Minesweep = function(w, h, coord){
    
    return {
        width : w,
        height: h,
        campoMinado: [],
        result: function() {
            
            for(var i=0; i<coord.length; i++) {
                this.campoMinado.push(coord[i].split(''));
            }    
            
            console.log(this.campoMinado);
            return this.campoMinado;
        }
    };
}