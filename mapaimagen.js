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

