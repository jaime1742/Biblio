function mostrarFotos(id) {
    let marcas = document.querySelectorAll(id)
    let imagenes = document.querySelectorAll(".coche")

    imagenes.forEach((imagen) => {
        imagen.classList.add("ocultar")
        
    })

    marcas.forEach((marca) => {
        marca.classList.remove("ocultar")
    })
}

function todos() {
    let figures = document.querySelectorAll("figure")
    figures.forEach((figure) => {
        figure.classList.remove("ocultar")
    })
}


