function iniciarMap() {
    var coordenadas = [
        { lat: -33.517695, lng: -70.595752 },
        { lat: -33.5126159, lng: -70.588873 },
        { lat: -33.5104165, lng: -70.6070532 },
        // Agrega más coordenadas aquí según sea necesario
    ];
  
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: coordenadas[0] // Centra el mapa en la primera coordenada
    });
  
    // Itera sobre el array de coordenadas y coloca un marcador en cada una
    coordenadas.forEach(function(coordenada) {
        var marker = new google.maps.Marker({
            position: coordenada,
            map: map
        });
    });
  }