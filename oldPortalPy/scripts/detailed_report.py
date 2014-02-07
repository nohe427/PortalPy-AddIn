import logging
import sys
from portalpy import Portal
from portalpy.stats import group_item_stats, group_member_stats
from pprint import pprint

logging.basicConfig(level=logging.WARN)


def main(argv=None):
    portal = Portal('http://wittm.esri.com/maps', 'admin', 'esri.agp')
    print_summary(portal)
    print_user_info(portal)
    print_group_info(portal)
    print_item_info(portal)
    print_system_content(portal)


def print_summary(portal):
    print '---------------------------'
    print 'GENERAL'
    print '---------------------------'
    print portal.info()
    print '---------------------------'
    print 'Language count: ' + str(len(portal.languages()))
    print 'Region count: ' + str(len(portal.regions()))
    print


def print_user_info(portal):
    print '---------------------------'
    print 'USERS'
    print '---------------------------'
    print 'User Count (org): ' + str(len(portal.org_users(num=10000)))
    print 'Users by Role:'
    results = portal.org_users(['role', 'count(role)'], group_fields=['role'])
    pprint(results, indent=4)
    print


def print_group_info(portal):
    print '---------------------------'
    print 'GROUPS'
    print '---------------------------'
    print 'Group Count (org): ' + str(len(portal.groups(scope='org', num=10000)))
    items_min, items_mean, items_max, items_stdv = group_item_stats(portal)
    print 'Item Count (Min): ' + str(items_min)
    print 'Item Count (Mean): ' + str(items_mean)
    print 'Item Count (Min): ' + str(items_max)
    print 'Item Count (StdDev): ' + str(items_stdv)
    members_min, members_mean, members_max, members_stdv = group_member_stats(portal)
    print 'Member Count (Min): ' + str(members_min)
    print 'Member Count (Mean): ' + str(members_mean)
    print 'Member Count (Min): ' + str(members_max)
    print 'Member Count (StdDev): ' + str(members_stdv)
    print


def print_item_info(portal):
    print '---------------------------'
    print 'CONTENT'
    print '---------------------------'
    print 'Item Count (org): ' + str(len(portal.search(scope='org', num=10000)))
    print 'Items by Type:'
    results = portal.search(properties=['type', 'count(type)'],
                            group_fields=['type'], \
                            sort_field='count(type)', \
                            sort_order='desc')
    pprint(results, indent=4)
    print


def print_system_content(portal):

    print '---------------------------'
    print 'BASEMAPS'
    print '---------------------------'
    print_info(portal, portal.basemaps(['id', 'title']), \
               'basemapGalleryGroupQuery')
    print

    print '---------------------------'
    print 'COLOR SETS'
    print '---------------------------'
    print_info(portal, portal.color_sets(['id', 'title']), \
               'colorSetsGroupQuery')
    print

    print '---------------------------'
    print 'FEATURED ITEMS'
    print '---------------------------'
    print_info(portal, portal.featured_items(['id', 'title']), \
               'featuredItemsGroupQuery')
    print

    print '---------------------------'
    print 'FEATURED ITEMS (HOME PAGE)'
    print '---------------------------'
    print_info(portal, portal.featured_items_homepage(['id', 'title']), \
               'homePageFeaturedContent')
    print

    print '---------------------------'
    print 'FEATURE COLLECTION TEMPLATES'
    print '---------------------------'
    print_info(portal, portal.feature_collection_templates(['id', 'title']), \
               'layerTemplatesGroupQuery')
    print

    print '---------------------------'
    print 'SYMBOL SETS'
    print '---------------------------'
    print_info(portal, portal.symbol_sets(['id', 'title']), \
               'symbolSetsGroupQuery')
    print

    print '---------------------------'
    print 'WEB MAPPING TEMPLATES'
    print '---------------------------'
    print_info(portal, portal.webmap_templates(['id', 'title']), \
               'templatesGroupQuery')
    print

    if not portal._is_pre_21:
        print '---------------------------'
        print 'GALLERY TEMPLATES'
        print '---------------------------'
        print_info(portal, portal.gallery_templates(['id', 'title']), \
                   'galleryTemplatesGroupQuery')


def print_info(portal, system_items, query):
    print 'Group: ' + portal.properties().get(query)
    if system_items:
        print 'Count: ' + str(len(system_items))
        print 'Details:'
        for item in system_items:
            print ' - ' + str(item)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
