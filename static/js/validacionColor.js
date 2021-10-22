$(function () {
    $("#btnEnviar").click(function () {
        subirArchivo();
    });

    var num_doc;
    var fecha;

    function subirArchivo(){
        const convPNG = new FormData($("#frmCargarHistoria")[0]);
        $.ajax({
            url: "/subirArchivo",
            data: convPNG,
            type: "post",
            dataType: "json",
            cache: false,
            contentType: false,
            processData: false,
            success: function (resultado) {
                console.log(resultado);
                if(resultado.estado){
                    num_doc = (resultado.datos[0]).toString();
                    fecha = (resultado.datos[1]);
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
            numeroDocumento: num_doc,
            fechaConsulta: fecha
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
            numeroDocumento: num_doc,
            fechaConsulta: fecha
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
            numeroDocumento: num_doc,
            fechaConsulta: fecha
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