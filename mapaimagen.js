function updateAreaCoords() {
    const img = document.querySelector('.map-container img');  // Selecciona la imagen
    const map = document.querySelector('map[name="mapa_parque"]'); // Selecciona el mapa
    const areas = map.querySelectorAll('area'); // Selecciona todas las áreas dentro del mapa

    const imgWidth = img.clientWidth; // Obtiene el ancho de la imagen
    const imgHeight = img.clientHeight; // Obtiene la altura de la imagen

    areas.forEach(area => {
        const coords = area.getAttribute('coords').split(','); // Obtiene las coordenadas de cada área

        const newCoords = coords.map((coord, index) => {
            return (index % 2 === 0) // Si es coordenada X
                ? Math.round(coord * (imgWidth / img.naturalWidth)) // Ajusta coordenada X
                : Math.round(coord * (imgHeight / img.naturalHeight)); // Ajusta coordenada Y
        });

        // Actualiza las coordenadas del área
        area.setAttribute('coords', newCoords.join(','));
    });
}

window.addEventListener('resize', updateAreaCoords);
window.addEventListener('load', updateAreaCoords);

window.addEventListener("resize", ajustarMapa);

function ajustarMapa() {
    var img = document.querySelector("img[usemap='#mapa_parque']");
    var areas = document.querySelectorAll("map[name='mapa_parque'] area");

    // Obtener las dimensiones de la imagen
    var imgWidth = img.offsetWidth;
    var imgHeight = img.offsetHeight;

    // Recorrer todas las áreas del mapa y ajustar sus coordenadas
    areas.forEach(function(area) {
        var coords = area.dataset.coords.split(",");
        var newCoords = coords.map(function(coord, index) {
            // Ajusta las coordenadas basadas en el tamaño de la imagen
            if (coord.includes("%")) {
                return Math.round((parseFloat(coord) * (index % 2 === 0 ? imgWidth : imgHeight)) / 100);
            }
            return coord;
        });

        area.coords = newCoords.join(",");
    });
}

// Ejecutar la función una vez al cargar la página
ajustarMapa();

