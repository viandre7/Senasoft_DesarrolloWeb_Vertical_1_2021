function mostrarPassword(){
    var cambio = document.getElementById("txtPassword");
    if(cambio.type == "password"){
        cambio.type = "text";
        $('.icons').removeClass('fa fa-eye-slash').addClass('fa fa-eye');
    }else{
        cambio.type = "password";
        $('.icons').removeClass('fa fa-eye').addClass('fa fa-eye-slash');
    }
} 

function btnDivSubir() {
    window.location="/subirHistoria"
}
function btnDivConsultar() {
    window.location="/consultarHistoria"
}
function btnDivDescargar() {
    window.location="/static/recursos/FormatoHistoriaClinica.pdf"
}
function btnDivComo() {
    window.location="#"
}


