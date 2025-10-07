function mostrarTareas(mes) {

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
    tareas[mes].forEach(tarea => {
        const li = document.createElement('li');
        li.innerHTML = `<a href = "${tarea.url}" target = "_blank">${tarea.texto}</a>`;
        lista.appendChild(li)
        
    });
    lista.classList.remove('oculto');
}

function mostrarMensaje() {
    const comentario =
    document.getElementById('comentario').value;
    if (comentario.trim() ==="") {
        alert('Por favor, escribe un comentario antes de enviar');
    }
    else {
        alert('Gracias por tu retroalimentacion');
        document.getElementById('comentario').value="";
    }
}

function ocultarLista() {
    const lista = document.getElementById('lista-tareas');
    lista.classList.add('oculto');
    lista.innerHTML = '';
}