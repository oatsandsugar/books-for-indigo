"""Build SVG country paths from Natural Earth's public-domain 110m GeoJSON.
Usage: python3 scripts/build-world-map.py /path/to/ne_110m_admin_0_countries.geojson
Source: https://github.com/nvkelso/natural-earth-vector/tree/master/geojson
"""
import json
import sys
from pathlib import Path

features = json.loads(Path(sys.argv[1]).read_text())['features']
countries = []
for feature in features:
    props = feature['properties']
    if props['ADM0_A3'] == 'ATA':
        continue
    geometry = feature['geometry']
    polygons = geometry['coordinates'] if geometry['type'] == 'MultiPolygon' else [geometry['coordinates']]
    paths = []
    for polygon in polygons:
        for ring in polygon:
            points = [f'{(lon + 180) * 2.5:.1f},{(85 - lat) * 2.5:.1f}' for lon, lat in ring]
            paths.append('M' + 'L'.join(points) + 'Z')
    countries.append({'code': props['ISO_A2_EH'], 'name': props['NAME_EN'], 'path': ''.join(paths)})
output = {'source': 'Natural Earth, public domain; retrieved 2026-10-09', 'viewBox': '0 0 900 365', 'countries': countries}
Path('data/world-map.json').write_text(json.dumps(output, ensure_ascii=False, separators=(',', ':')) + '\n')
print(f'{len(countries)} country outlines; {Path("data/world-map.json").stat().st_size:,} bytes')
