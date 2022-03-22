$.validator.addMethod("terminaPor", function(value, element, parametro){
    if(value.endsWith(parametro)){
        return true;
    }
    return false;
}, "Debe terminar por {0}")
$("#formulario_contacto").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 3,
            maxlength: 30
        },
        email: {
            required: true,
            email: true,
            terminaPor: "live.cl"
            //number: true
            //min: 3
            //max: 30
        },
        tiposolicitud: {
            required: true
        },
        mensaje: {
            required: true,
            minlength: 5,
            maxlength: 200
        }
    }

})

$("#guardar").click(function(){
    if($("#formulario_cliente").valid() == false) {
        return;
    }
    let nombre = $("#nombre").val()
    let email = $("#email").val()
    let tiposolicitud = $("#tipo_solicitud").val()
    let mensaje = $("#mensaje").val()
    let avisos = $("#avisos").is(":checked")

    //construir un json
    //enviar los datos por post
})