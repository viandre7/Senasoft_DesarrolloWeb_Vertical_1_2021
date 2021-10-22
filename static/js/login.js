$(function(){
  $("#btnIniciarSesion").click(function(){
    alert("hola mundo")
    });



  function login() {
  $.ajax({
    url: "/agregarRespuesta",
    data: formQueja,
    type: "post",
    dataType: "json",
    cache: false,
    contentType: false,
    processData: false,
    success: function (resultado) {
      console.log(resultado);
      if (resultado.estado) {
        $("#modalRespuestaSol").modal("hide");
      }
    },
    error: function (resultado) {
      console.log(resultado);
    },
  });
}

})
