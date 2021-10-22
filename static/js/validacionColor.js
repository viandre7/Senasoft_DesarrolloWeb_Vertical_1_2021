$(function () {
    $("#btncrear").click(function () {
        subirArchivo();
    });

    var filename;

    function subirArchivo(){
        const convPNG = new FormData($("#frmCargarHistoria")[0]);
        $.ajax({
            url: "/subirHistoria",
            data: convPNG,
            type: "post",
            dataType: "json",
            cache: false,
            contentType: false,
            processData: false,
            success: function (resultado) {
                console.log(resultado);
                if(resultado.estado){
                    filename = (resultado.datos).toString();
                    convertirArchivo();
                }
            },
            error: function (resultado) {
                console.log(resultado);
            },
        });
    }

    function convertirArchivo(){
        var parametros = {        
            nombreArchivo: filename
        };
        $.ajax({
            url: "/convertirArchivo",
            data: parametros,
            type: "post",
            dataType: "json",
            cache: false,
            success: function (resultado) {
                console.log(resultado);
                if(resultado.estado){
                    convertirEscalaGrises();
                }
            },
            error: function (resultado) {
                console.log(resultado);
            },
        });

    }

    function convertirEscalaGrises(){
        var parametros = {        
            nombreArchivo: filename
        };
        $.ajax({
            url: "/convertirEscalaGrises",
            data: parametros,
            type: "post",
            dataType: "json",
            cache: false,
            success: function (resultado) {
                console.log(resultado);
                convertirImagen();
            },
            error: function (resultado) {
                console.log(resultado);
            },
        });
    }

    function convertirImagen(){
        var parametros = {        
            nombreArchivo: filename
        };
        $.ajax({
            url: "/convertirImagen",
            data: parametros,
            type: "post",
            dataType: "json",
            cache: false,
            success: function (resultado) {
                console.log(resultado);
            },
            error: function (resultado) {
                console.log(resultado);
            },
        });
    }
})