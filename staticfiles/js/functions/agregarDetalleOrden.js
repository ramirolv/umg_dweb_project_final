
function agregarDetalle(){
    fila = document.createElement('tr');
    tdAcciones = document.createElement('td');
    tdCantidad = document.createElement('td');
    tdDescripcion = document.createElement('td');
    tdPrecio = document.createElement('td');

    tdCantidad.appenChild(document.createTextNode('4'));
    tdDescripcion.appenChild(document.createTextNode('Pizza'));
    tdPrecio.appenChild(document.createTextNode('50.00'));
    
    fila.appenChild(tdAcciones);
    fila.appenChild(tdCantidad);
    fila.appenChild(tdDescripcion);
    fila.appenChild(tdPrecio);

    tabla = document.getElementById('body_table_orden');
    tabla.appenChild(fila);
}