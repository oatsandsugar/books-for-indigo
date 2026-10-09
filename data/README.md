# World map

`world-map.json` contains country outlines derived from [Natural Earth 1:110m countries](https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_110m_admin_0_countries.geojson), downloaded 9 October 2026. Natural Earth data is public domain.

Coordinates use a simple equirectangular projection, rounded to one decimal SVG unit. Antarctica is omitted. The map groups books by their existing `data-country` value; missing origins are reported separately.

To rebuild after downloading the source GeoJSON:

```sh
python3 scripts/build-world-map.py /path/to/ne_110m_admin_0_countries.geojson
```

## Edition evidence

`edition-publishers.json` documents evidence for each `data-edition-publisher` in `index.html`. Photo references identify the user-provided cover images; the photographs themselves are not published here. Preserve original publisher metadata. Add edition records only when evidence identifies the copy read, not merely another available edition.
