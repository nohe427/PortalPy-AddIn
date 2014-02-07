import logging
from portalpy import Portal, ArcGISConnection

logging.basicConfig(level=logging.WARN)

TAGS = 'GIS, Service'
TYPE_MAP = {
    'featureserver': {'type':'Feature Service', 'typeKeywords': 'Data, Service, Feature Service, ArcGIS Server, Feature Access'},
    'mapserver': {'type':'Map Service','typeKeywords': 'Data, Service, Map Service, ArcGIS Server'},
    'geocodeserver': {'type':'Geocoding Service','typeKeywords': 'Tool, Service, Geocoding Service, Locator Service, ArcGIS Server'},
    'naserver': {'type':'Network Analysis Service','typeKeywords': 'Tool, Service, Network Analysis Service, ArcGIS Server'},
    'globeserver': {'type':'Globe Service','typeKeywords': 'Data, Service, Globe Service, ArcGIS Server'},
    'gpserver': {'type':'Geoprocessing Service','typeKeywords': 'Tool, Service, Geoprocessing Service, ArcGIS Server'},
    'geodataserver': {'type':'Geodata Service','typeKeywords': 'Data, Service, Geodata Service, ArcGIS Server'},
    'imageserver': {'type':'Image Service','typeKeywords': 'Data, Service, Image Service, ArcGIS Server'},
    'geometryserver': {'type':'Geometry Service','typeKeywords': 'Tool, Service, Geometry Service, ArcGIS Server'}
}

def main():
    portal = Portal('http://wittm.esri.com', 'admin', 'esri.agp')
    server = ArcGISConnection('http://sampleserver4.arcgisonline.com/ArcGIS/rest/services')
    root = server.post('/', {'f': 'json'})
    register_services(portal, server, root['services'])
    for folder_name in root['folders']:
        folder = server.post('/' + folder_name, {'f': 'json'})
        register_services(portal, server, folder['services'])

def register_services(portal, server, services):
    for service in services:
        type = service['type']
        if type.lower() in TYPE_MAP:
            path = '/' + service['name'] + '/' + type
            service_info = server.post(path, {'f': 'json'})
            doc_info = service_info.get('documentInfo') or {};
            item = {
                'url': server.baseurl + path,
                'title': service['name'].split('/')[-1],
                'description': service_info.get('serviceDescription') or \
                               service_info.get('description') or \
                               doc_info.get('Comments') or '',
                'snippet': doc_info.get('Subject') or '',
                'tags': TAGS,
                'accessInformation': service_info.get('copyrightText') or \
                                     doc_info.get('Credits') or '',
                'spatialReference' : get_spatial_reference(type, service_info),
            }
            item.update(TYPE_MAP[type.lower()])
            id = portal.add_item(item)
            if id:
                print 'Registered service \'' + item['title'] + '\' with id=' + id

def get_spatial_reference(service_type, service_info):
    spatial_ref = service_info.get('spatialReference')
    if service_type == 'ImageServer' and 'extent' in service_info:
        spatial_ref = service_info['extent'].get('spatialReference')
    if not spatial_ref:
        return None
    elif 'wkid' in spatial_ref:
        return spatial_ref['wkid'];
    # TODO Handle wkt
    return None

if __name__ == "__main__":
    main()
