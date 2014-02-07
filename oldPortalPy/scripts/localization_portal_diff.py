import logging
import sys
from portalpy import Portal

logging.basicConfig(level=logging.WARN)

def main(argv=None):
    portal1 = Portal('http://portaldev.esri.com')
    portal2 = Portal('http://dev.arcgis.com')
    portal1_items_by_key = get_items_by_key(portal1)
    portal2_items_by_key = get_items_by_key(portal2)
    print_left_only(portal1.hostname, portal1_items_by_key, portal2_items_by_key)
    print_left_only(portal2.hostname, portal2_items_by_key, portal1_items_by_key)

def get_items_by_key(portal):
    items_by_key = dict()
    for lang in portal.languages():
        user = 'esri_' + lang['culture'][:2]
        items = portal.search(['id','owner','type','name', 'title'],\
                              'owner:' + user, scope='public')
        for item in items:
            items_by_key[item['owner'] + ':' + str(item['name'])] = item
    return items_by_key

def print_left_only(left_name, left_items_by_key, right_items_by_key):
    left_only_keys = set(left_items_by_key.keys()) - set(right_items_by_key.keys())
    left_only = [left_items_by_key[key] for key in left_only_keys]
    left_only = sorted(left_only, key=lambda k: k['owner'])
    print left_name + ' only (total: ' + str(len(left_only)) + ')'
    for item in left_only:
        print str(item)
    print

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
