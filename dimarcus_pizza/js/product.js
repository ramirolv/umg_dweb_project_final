$(document).on('ready', iniciar);

function iniciar(){
    $varBotonAgregar = $('#botonNuevo');
    $varBotonAgregar.on('click', abrirFormulario);
    
    $varBotonSalirFromulario = $('#cerrarFormulario');
    $varBotonSalirFromulario.on('click', cerrarFormulario);

    $varformulario = $('#formularioAgregar');
}

function abrirFormulario(){
    $varformulario.show();
}

function cerrarFormulario(){
    $varformulario.hide();
}