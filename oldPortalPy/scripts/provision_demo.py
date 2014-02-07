import logging, random
from portalpy import Portal, WEB_ITEM_FILTER
from portalpy.config import configure_portal, create_basemap_gallery_group, \
                            feature_items, feature_groups
from portalpy.provision import load_groups, copy_items

logging.basicConfig(level=logging.WARN)

# Setup portal connections and file paths
portal = Portal('http://wittm.esri.com', 'admin', 'esri.agp')
arcgisonline = Portal('http://www.arcgis.com')
groups_csv = '.\\provision_groups.csv'

# Configure the portal
configure_portal(portal, 'Demo Portal', 'A portal used for demonstrations.')
create_basemap_gallery_group(portal, 'Demo Basemaps', copy_filter='-bing -osm')

# Create groups from CSV, then copy/share like-tagged items from arcgis online
items_to_feature = []
owner = portal.logged_in_user()['username']
groups = load_groups(portal, groups_csv, 'csv')[0]
for group in groups:
    tags = group['tags'].split(',')
    tags_expr = ' OR '.join('tags:"%s"' % tag.strip() for tag in tags)
    item_query = WEB_ITEM_FILTER + ' AND (' + tags_expr + ')'
    items = arcgisonline.search(q=item_query, num=5)
    item_id_map = copy_items(items, arcgisonline, portal, owner)
    portal.share_items(owner, item_id_map.values(), [group['id']], True, True)
    items_to_feature.append(item_id_map[items[0]['id']])

# Feature items and groups (clear_existing=True)
feature_items(portal, items_to_feature, True)
feature_groups(portal, random.sample(groups, 5), True)
