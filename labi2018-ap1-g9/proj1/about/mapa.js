var map = new L.Map("oMeuMapa", {center: [40.633258,-8.659097],zoom: 15});
var osmUrl="http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
var osmAttrib="Map data OpenStreetMap contributors";
var osm = new L.TileLayer(osmUrl, {attribution: osmAttrib});
map.addLayer(osm);
function mostraCoordenadas(e){
    var s = document.getElementById("coordenadas");
    s.innerHTML = "Latitude, Longitude = "+e.latlng.lat+", "+e.latlng.lng;
    }
var pontos = [
    L.marker([40.633258, -8.659097]).bindPopup("@DETI"),
    ];
    for(i in pontos) {
    pontos[i].addTo(map);
    }