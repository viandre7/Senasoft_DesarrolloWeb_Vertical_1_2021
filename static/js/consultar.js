/**Declarar variables */
var primeraCard;
var primeraFila;

$(function(){    
    /**Datatable para la tabla consultar historia */
    $('#tblConsulta').DataTable( {
            dom: 'Bfrtip',
            buttons: [
                'copy', 'csv', 'excel', 'print'
            ]
        } );

        primeraCard=$("#cardPrimera");
        primeraFila=$("#fila");
   
});

