<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fun Map of GIS Club</title>

    <script src='https://api.mapbox.com/mapbox-gl-js/v2.9.1/mapbox-gl.js'></script>
    <link href='https://api.mapbox.com/mapbox-gl-js/v2.9.1/mapbox-gl.css' rel='stylesheet' />

    <style>
        .marker {
            background-image: url("UBCGISClubLOGO.png");
            background-size: cover;
            width: 70px;
            height: 70px;
            border-radius: 50%;
            cursor: pointer;
        }

        .mapboxgl-popup {
            max-width: 200px;
        }

        .mapboxgl-popup-content {
            text-align: center;
            font-family: 'Open Sans', sans-serif;
        }
    </style>


</head>


<body>
    <div>
        <h1> UBC GIS Club</h1>
    </div>


    <div id='map' style='width: 1000px; height: 800px;'></div>
    <!-- feel free to play around with the map size by changing pixels-->

    <script>
        mapboxgl.accessToken = 'pk.eyJ1Ijoibm9ydG9uMjciLCJhIjoiY2xoam9hNHI5MGpuMjNscWtlcTF2dTN3dyJ9.xx0qCx-woV7mYFkrMNQmiA';
        const map = new mapboxgl.Map({
            container: 'map',
            style: 'mapbox://styles/norton27/clnl3x5ph00lu01q1emfi4hjx', //insert style here, here are some pre-set options https://docs.mapbox.com/api/maps/styles/
            center: [-123.21224931916706, 49.26029799208978,], //insert coordinates here
            zoom: 12 // insert zoom level here e.g. 15
        });


        map.addControl(new mapboxgl.NavigationControl());


        const geojson = {
            type: 'FeatureCollection',
            features: [
                {
                    type: 'Feature',
                    geometry: {
                        type: 'Point',
                        coordinates: [-123.20837651469633, 49.26388219880599] //insert coordinates here
                    },
                    properties: {
                        title: 'Bombay Masala', // what's your marker title? e.g. University Golf Course
                        description: 'Point Grey' // where is your marker? e.g. Point Grey
                    }
                },
                {
                    type: 'Feature',
                    geometry: {
                        type: 'Point',
                        coordinates: [-123.25600176717671, 49.265920324279676] //coordinates
                    },
                    properties: {
                        title: 'UBC GIS Club', // whats your marker title?
                        description: 'the best club ever' // where is it?
                    }
                }
            ]
        };

        // add markers to map
        for (const feature of geojson.features) {
            // create a HTML element for each feavture
            const el = document.createElement('div');
            el.className = 'marker';


            // make a marker for each feature and add to the map
            new mapboxgl.Marker(el)
                .setLngLat(feature.geometry.coordinates)
                .setPopup(
                    new mapboxgl.Popup({ offset: 25 }) // add popups
                        .setHTML(
                            `<h3>${feature.properties.title}</h3>
<p>${feature.properties.description}</p>`
                        )
                )
                .addTo(map)
        }
        // Add a scale control to the map
        map.addControl(new mapboxgl.ScaleControl());

    </script>
</body>

</html>