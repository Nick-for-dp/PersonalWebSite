import 'ol/ol.css';
import Map from 'ol/Map';
import View from 'ol/View';
import VectorTileLayer from 'ol/layer/VectorTile';
import { applyStyle } from 'ol-mapbox-style';
import { transform } from 'ol/proj';
import { Vector } from 'ol/layer';
import GeoJSON from 'ol/format/GeoJSON'
import { Vector as Vec} from 'ol/source';
import { Style, Icon } from 'ol/style';
// import MapboxLanguage from '@mapbox/mapbox-gl-language';

const baseLayer = new VectorTileLayer({declutter: true});
applyStyle(
    baseLayer, 
    'mapbox://styles/mapbox/outdoors-v12', 
    {accessToken: 'pk.eyJ1IjoibXVzaGVyIiwiYSI6ImNsa3JvcHc5ZjF6eXYzZW12ajMzMXd0enQifQ.dZ2685AuaU8GY6wDr11Ipw'}
);

// 通过geojson添加两人的足迹信息
var nickFootprintLayer = new Vector({
    source: new Vec({
        projection: 'EPSG:3857',
        url: './data/nick.geojson',
        format: new GeoJSON()
    })
});
let nickIcon = require("./bob_no_bg.png");
const nickStyle = new Style({
    image: new Icon({
        src: nickIcon,
        anchor: [1, 1],
        scale:0.05
    })
});
nickFootprintLayer.setStyle(nickStyle);

var stefanaFootprintLayer = new Vector({
    source: new Vec({
        projection: 'EPSG:3857',
        url: './data/stefana.geojson',
        format: new GeoJSON()
    })
});
let stefanaIcon = require("./pi_star_no_bg.png");
const stefanaStyle = new Style({
    image: new Icon({
        src: stefanaIcon,
        anchor: [1, 1],
        scale:0.05
    })
});
stefanaFootprintLayer.setStyle(stefanaStyle);

var publicFootprintLayer = new Vector({
    source: new Vec({
        projection: 'EPSG:3857',
        url: './data/public.geojson',
        format: new GeoJSON()
    })
});
let publicIcon = require("./woo_no_bg.png");
const publicStyle = new Style({
    image: new Icon({
        src: publicIcon,
        anchor: [1, 1],
        scale:0.05
    })
});
publicFootprintLayer.setStyle(publicStyle);

const map = new Map({
    target: 'footprintMap',
    layers: [
        baseLayer,
        nickFootprintLayer,
        stefanaFootprintLayer,
        publicFootprintLayer
    ],
    view: new View({
        center: transform([120.14, 30.30], 'EPSG:4326', 'EPSG:3857'),
        // center: [13367207.410800237, 3574715.006520772],
        zoom: 15,
        projection: "EPSG:3857"
    })
});
// map.addLayer(nickFootprintLayer);
// const languageController = new MapboxLanguage({defaultLanguage: 'zh-Hans'});
// map.addControl(languageController);


