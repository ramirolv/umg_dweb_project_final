$(document).on('ready', iniciar);

//campos para rellenar
var linkImg;
var selectTipo;
var inputSabor;
var inputPrecio;

function iniciar(){
    //boton de agregar
    $btnAgregar = $('#btnAgregar');
    $btnAgregar.on('click', agregar);
}

function agregar(){
    //campos para rellenar
    linkImg = document.getElementById('inputLinkImg').value;
    selectTipo = document.getElementById('selectTipo').value;
    inputSabor = document.getElementById('inputSabor').value;
    inputPrecio = document.getElementById('inputPrecio').value;

    if(validarCamposFormulario()){
        if (selectTipo === 'Pizza') {
            $contenedorProductos = $('#contenedorProductos1');
        }else if(selectTipo === 'Otros'){
            $contenedorProductos = $('#contenedorProductos2');
        }
        else if(selectTipo === 'Bebidas'){
            $contenedorProductos = $('#contenedorProductos3');
        }
        $contenedorProductos.append(insertarProducto(linkImg, inputSabor, inputPrecio));
        alert('Agregado con éxito');
    }
}

function validarCamposFormulario(){
    alert('Entra a la función validar');
    alert(linkImg+inputSabor+inputPrecio);
    if (linkImg === '' || inputSabor === '' || inputPrecio === '') {
        alert('No se han llenado todos los campos');
        return false;
    }else{
        return true;
    }
}

function insertarProducto(img, sabor, precio){
    var cadena = '<div class="col-lg-3 col-md-8 "> <div class="product-item d-flex flex-column bg-white rounded overflow-hidden h-100"> <div class="position-relative mt-auto">            <img class="img-fluid" src="'+img+'" alt="">        </div>        <div class="text-center p-2">                                <h4 class="mb-3">'+sabor+'</h4>            <span>Venta por Unidad</span>            <hr><div class="d-inline-block border border-primary rounded-pill px-2 mb-2">Q '+precio+'</div>        </div>                     </div></div>';
    return cadena;
}