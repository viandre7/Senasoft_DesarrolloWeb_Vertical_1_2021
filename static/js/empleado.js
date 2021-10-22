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
    $.ajax({
        url: "/agregarEmpleado",
        data: $("#frmRegistro").serialize(),
        type: "post",
        dataType: "json",
        cache: false,
        success: function(resultado){
            console.log(resultado);
            if(resultado.estado){                
                $("#txtCorreo").val("");
                $("#txtCedula").val("");                
                $("#txtNombre").val("");
                $("#txtApellido").val("");
                $("#txtCelular").val("");
                $("#txtCargo").val("");
                $("#txtPassword").val("");

                swal("¡Correcto!!", resultado.mensaje + 
                " ", "info"); 
                window.location="/mostrarIniciarSesion"
            }else{
                $("#txtCorreo").val("");
                $("#txtCedula").val('');                
                $("#txtNombre").val("");
                $("#txtApellido").val("");
                $("#txtCelular").val("");
                $("#txtCargo").val("");
                $("#txtPassword").val("");

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

