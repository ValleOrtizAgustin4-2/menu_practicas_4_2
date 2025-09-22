function mostrarTareas(mes)
{
    const tareas = {
        septiembre: [
            {texto: 'Html-Css-Js-Audio',url:'https://misitio.com/ej-1'},
            {texto: 'Html-Css-Js-Video',url:'https://misitio.com/ej-2'},
        ],
        octubre: [
            {texto: 'Html-Css-Js-Multiples Imagenes',url:'https://misitio.com/ej-3'},
            {texto: 'Html-Css-Js-Combinacion Objetos',url:'https://misitio.com/ej-4'},
        ],
        noviembre: [
            {texto: 'Html-Css-Js-Responsivos',url:'https://misitio.com/ej-5'},
            {texto: 'Html-Css-Js-Animaciones',url:'https://misitio.com/ej-6'},
        ]
    };

    const lista = document.getElementById('lista-tareas');
    lista.innerHTML="";
    lista.classList.add('oculto');
}

function ocultarLista()
{
const lista = document.getElementById('lista-tareas');
lista.classList.add('oculto');
lista.innerHTML = '';
}