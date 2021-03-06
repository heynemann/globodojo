(function() {
    
    var extensions = {

        assert: function assert(a, msg) {
            ok(a, msg);
        },
        assertEquals: function assertEquals(actual, expected, message) {
            equals(actual, expected, message);
        },
        assertNotEquals: function assertNotEquals(actual, expected, message) {
        	ok(actual != expected,message);
        },
        fail: function fail(msg) {
            ok(false, msg);
        }

    };
    
    for(var fn in extensions) {
        this[fn] = this[fn] || extensions[fn];// this === global scope
    }
        
})();