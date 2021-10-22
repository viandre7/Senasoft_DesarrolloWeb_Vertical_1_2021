


/** Acción del evento click del btnCrear */
$(function(){
    $("#btncrear").click(function(){
        if(($("#txtCorreo").val()!="") 
                && ($("#txtCedula").val()!="") && ($("#txtNombre").val()!="") && ($("#txtApellido").val()!="")
                && ($("#txtCelular").val()!="")&& ($("#txtPassword").val()!="")&& ($("#txtCargo").val()!="")){
                    agregarEmpleado();
        }else{
            swal("Por favor llene todos los campos!!"); 
        }
            
     });
});



/**
 * Metodo que mediante ajax hace una petición al servidor 
 * para agregar un empleado a la db @returns true o false
 */
function agregarEmpleado(){
    const formAgregar = new FormData($("#frmRegistro")[0]);

    $.ajax({
        url: "/agregarEmpleado",
        data: formAgregar,
        type: "post",
        dataType: "json",
        cache: false,
        contentType: false,
        processData: false,
        success: function(resultado){
            console.log(resultado);
            if(resultado.estado){      
                swal("Exito!!", resultado.mensaje + 
                " ", "danger");          
             
                limpiarFrm();

                window.location="/mostrarIniciarSesion"
            }else{
                limpiarFrm();

                swal("Error!!", resultado.mensaje + 
                " ", "danger"); 
                window.location="/registrarse"
            }
        },
        error: function(resultado){
            console.log(resultado);
        }

    });
}


/**
 * Función que permite limpiar los campos del formulario agregar
 * Empleado
 */
function limpiarFrm() {
    $("#txtCorreo").val("");
    $("#txtCedula").val('');                
    $("#txtNombre").val("");
    $("#txtApellido").val("");
    $("#txtCelular").val("");
    $("#txtCargo").val("");
    $("#txtPassword").val("");
    $("#txtImagen").val("");
}

