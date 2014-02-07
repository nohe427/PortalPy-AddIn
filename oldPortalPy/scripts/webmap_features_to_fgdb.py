import arcpy
import logging
import os
import sys
from portalpy import Portal

logging.basicConfig(level=logging.WARN)

GEOM_TYPE_MAP = {'esriGeometryPoint': 'POINT',
                 'esriGeometryMultipoint': 'MULTIPOINT',
                 'esriGeometryPolyline': 'POLYLINE',
                 'esriGeometryPolygon': 'POLYGON'}

FIELD_TYPE_MAP = {'esriFieldTypeString': 'TEXT',
                  'esriFieldTypeInteger': 'LONG',
                  'esriFieldTypeDouble': 'DOUBLE',
                  'esriFieldTypeDate': 'DATE'}

def main(argv=None):
    portal = Portal('http://portaldev.esri.com')
    template_name = 'Map Notes'
    file_gdb_path = 'C:/Temp/MapNotes.gdb'

    # Retrieve the layer definitions (schemas) for the specified
    # feature collection template
    template_id = portal.feature_collection_templates(q=template_name)[0]['id']
    template = portal.item_data(template_id, return_json=True)
    template_schemas = [layer['layerDefinition'] for layer in template['layers']]

    # Create the file GDB with feature classes for each schema
    create_file_gdb(file_gdb_path, template_schemas)

    # Get all webmaps, pull out features that match the template schemas, and
    # then load them into the corresponding feature classes in the file GDB
    for webmap in portal.webmaps():
        for template_schema in template_schemas:
            features = webmap.features([template_schema])
            if features:
                load_features(file_gdb_path, template_schema['name'], features)

def create_file_gdb(file_gdb_path, schemas):
    arcpy.CreateFileGDB_management(os.path.dirname(file_gdb_path), \
                                   os.path.basename(file_gdb_path))
    arcpy.env.workspace = file_gdb_path
    for schema in schemas:
        fc_name = schema['name']
        geom_type = GEOM_TYPE_MAP[schema['geometryType']]
        arcpy.CreateFeatureclass_management(file_gdb_path, fc_name, geom_type)
        for field in schema['fields']:
            if field['type'] in FIELD_TYPE_MAP:
                field_type = FIELD_TYPE_MAP[field['type']]
                arcpy.AddField_management(fc_name, field['name'], field_type)

def load_features(file_gdb_path, fc_name, features):
    fc = file_gdb_path + '/' + fc_name
    try:
        rows = arcpy.InsertCursor(fc)
        fields = {field.name: field for field in arcpy.ListFields(fc)}
        for feature in features:
            row = rows.newRow()
            row.setValue('SHAPE', arcpy.AsShape(feature['geometry'], True))
            for name, value in feature['attributes'].iteritems():
                field = fields.get(name)
                if field and field.editable:
                    row.setValue(name, value)
            rows.insertRow(row)
    finally:
        if row: del row
        if rows: del rows

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
