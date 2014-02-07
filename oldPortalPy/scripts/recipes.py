import csv
import logging
import portalpy.stats
import sys
from datetime import datetime, timedelta
from operator import itemgetter
from portalpy import Portal, unpack, parse_hostname, portal_time,\
                     WEBMAP_ITEM_FILTER, normalize_url
from portalpy.provision import copy_items, copy_user_contents, copy_groups,\
                               save_items, load_items
from portalpy.config import feature_items_query
from pprint import pprint

# Setup logging (optional)
logging.basicConfig(level=logging.WARN)

def main(argv=None):
    portal_info()
    #portal_info_plus()
    #daily_item_stats()
    #most_active_publishers()
    #most_viewed_publishers()
    #most_reviewed_publishers()
    #most_rated_publishers()
    #highest_rated_publishers()
    #count_item_types()
    #count_tags()
    #calc_group_stats()
    #count_user_roles()
    #average_coverage_by_item_type()
    #print_user_contents()
    #list_group_ids()
    #create_user_group_item_reports()
    #make_publisher()
    #hide_user()
    #delete_non_admin_users()
    #copy_items_query()
    #copy_items_with_related()
    #copy_users()
    #copy_groups_sample()
    #copy_group_with_shared_content()
    #add_update_metadata()
    #signup_user()
    #invite_org_user()
    #populate_gallery()
    #create_demographics_group()
    #update_item_thumbnail()
    #update_group_thumbnail()
    #print_webmap()
    #count_webmap_url_references()
    #count_webmap_item_references()
    #find_hostname_references()
    #update_hostname_references()
    #feature_groups()
    #export_import_content()
    #find_public_content_with_weak_descriptions()
    #set_home_page_banner()
    #proxy_through_fiddler()

def portal_info():
    portal = Portal('http://portaldev.esri.com')
    print portal.info()

def portal_info_plus():
    portal = Portal('http://portaldev.esri.com')
    print portal.info()
    pprint(portal.properties())
    pprint(portal.languages())
    pprint(portal.regions())
    pprint(portal.basemaps(['title']))
    pprint(portal.color_sets(['title']))
    pprint(portal.featured_items(['title']))
    pprint(portal.featured_items_homepage(['title']))
    pprint(portal.feature_collection_templates(['title']))
    pprint(portal.symbol_sets(['title']))
    pprint(portal.gallery_templates(['title']))
    pprint(portal.webmap_templates(['title']))

def daily_item_stats():
    portal = Portal('http://www.arcgis.com')
    today = datetime.utcnow()
    weekago = today - timedelta(days=1)
    q = 'modified:[' + portal_time(weekago) + ' TO ' + portal_time(today) + ']'
    results = portal.search(['type', 'count(type)'], q, group_fields=['type'], num=5000)
    pprint(results, indent=2)

def most_active_publishers():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    results = portal.search(['owner','count(owner)'], group_fields=['owner'], scope='org')
    pprint(results, indent=2)

def most_viewed_publishers():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    results = portal.search(['owner','sum(numViews)'], group_fields=['owner'])
    pprint(results, indent=2)

def most_reviewed_publishers():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    results = portal.search(['owner','sum(numComments)'], group_fields=['owner'])
    pprint(results, indent=2)

def most_rated_publishers():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    results = portal.search(['owner','sum(numRatings)'], group_fields=['owner'])
    pprint(results, indent=2)

def highest_rated_publishers():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    results = portal.search(['owner','count(avgRating)','avg(avgRating)'], \
                             'numratings:{0 TO 99999}',\
                             group_fields=['owner'])
    pprint(results, indent=2)

def count_item_types():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    counts = portal.search(properties=['type', 'count(type)'],
                           group_fields=['type'],\
                           sort_field='count(type)',\
                           sort_order='desc')
    pprint(counts, indent=2)

def count_tags():
    portal = Portal('http://www.geoplatform.gov')
    results = portal.search(['tags'])
    tags = unpack(results, flatten=True)
    counts = dict((tag, tags.count(tag)) for tag in tags)
    sorted_counts = sorted(counts.iteritems(), key=itemgetter(1), reverse=True)
    pprint(sorted_counts, indent=2)

def calc_group_stats():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')

    items_min, items_mean, items_max, items_stdv = \
            portalpy.stats.group_item_stats(portal)
    print 'Item Count (Min): ' + str(items_min)
    print 'Item Count (Mean): ' + str(items_mean)
    print 'Item Count (Min): ' + str(items_max)
    print 'Item Count (StdDev): ' + str(items_stdv)

    members_min, members_mean, members_max, members_stdv = \
            portalpy.stats.group_member_stats(portal)
    print 'Member Count (Min): ' + str(members_min)
    print 'Member Count (Mean): ' + str(members_mean)
    print 'Member Count (Min): ' + str(members_max)
    print 'Member Count (StdDev): ' + str(members_stdv)

def count_user_roles():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    results = portal.org_users(['role', 'count(role)'], group_fields=['role'])
    pprint(results, indent=2)

def average_coverage_by_item_type():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    def avg_area(extents):
        extents = filter(None, extents)
        if extents:
            areas = []
            for e in extents:
                if e: areas.append((e[1][0] - e[0][0]) * (e[1][1] - e[0][1]))
            return sum(area for area in areas) / len(areas)
        return 0
    portal.aggregate_functions['avg_area'] = avg_area
    results = portal.search(['type', 'avg_area(extent)'], group_fields=['type'])
    pprint(results, indent=2)

def print_user_contents():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    root_items, folder_items = portal.user_contents('admin')
    pprint(root_items, indent=2)
    pprint(folder_items, indent=2)

def list_group_ids():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    groups = portal.groups(['title', 'id'])
    pprint(groups, indent=2, width=120)

def create_user_group_item_reports():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')

    item_fields = ['id', 'title', 'owner', 'numViews']
    items = portal.search(item_fields, sort_field='numViews', sort_order='desc')
    csvfile = csv.writer(open('items-report.csv', 'wb'))
    csvfile.writerow(item_fields)
    for item in items:
        row = [item[field] for field in item_fields]
        csvfile.writerow(row)

    groups_fields = ['id', 'title', 'owner']
    groups = portal.groups(groups_fields)
    csvfile = csv.writer(open('groups-report.csv', 'wb'))
    csvfile.writerow(groups_fields)
    for group in groups:
        row = [group[field] for field in groups_fields]
        csvfile.writerow(row)

    user_fields = ['username', 'fullName', 'email', 'role']
    users = portal.org_users(user_fields)
    csvfile = csv.writer(open('users-report.csv', 'wb'))
    csvfile.writerow(user_fields)
    for user in users:
        row = [user[field] for field in user_fields]
        csvfile.writerow(row)

def make_publisher():
    portal = Portal('http://portaldev.arcgis.com', 'admin', 'esri.agp')
    portal.update_user_role('wmathot', 'org_publisher')

def hide_user():
    portal = Portal('http://portaldev.arcgis.com', 'admin', 'esri.agp')
    user_to_hide = 'wmathot'
    portal.update_user(user_to_hide, {'access': 'private'})
    groups = portal.groups(['id'], 'owner:' + user_to_hide)
    for group in groups:
        portal.update_group(group['id'], {'access': 'private'})
    items = portal.search(['id'], 'owner:' + user_to_hide)
    portal.share_items(user_to_hide, items, None, False, False)

def delete_non_admin_users():
    portal = Portal('http://wittm.esri.com', 'admin', 'esri.agp')
    users = portal.org_users(['username', 'role'])
    for user in users:
        if user['role'] != 'org_admin':
            portal.delete_user(user['username'], cascade=True)

def copy_items_query():
    source = Portal('http://www.arcgis.com')
    target = Portal('http://wittm.esri.com', 'wmathot', 'wmathot')
    items = source.search(q='h1n1')
    copied_items = copy_items(items, source, target, 'wmathot', 'Copied Items (h1n1)')
    for sourceid in copied_items.keys():
        print 'Copied ' + sourceid + ' to ' + copied_items[sourceid]

def copy_items_with_related():
    source = Portal('http://dev.arcgis.com')
    target = Portal('http://wittm.esri.com', 'wmathot', 'wmathot')
    items = source.search(q='type:"Web Mapping Application"', num=5)
    copied_items = copy_items(items, source, target, 'wmathot', 'Web Apps 5',  \
                              relationships=['WMA2Code', 'MobileApp2Code'])
    for sourceid in copied_items.keys():
        print 'Copied ' + sourceid + ' to ' + copied_items[sourceid]

def copy_users():
    source = Portal('http://portaldev.arcgis.com', 'admin', 'esri.agp')
    target = Portal('http://wittm.esri.com', 'wmathot', 'wmathot')
    owners = ['admin', 'wmathot']
    target_owner = target.logged_in_user()['username']
    for owner in owners:
        groups = source.groups(q='owner:' + owner)
        copied_groups = copy_groups(groups, source, target, target_owner)
        copied_items = copy_user_contents(source, owner, target, target_owner)
        for item_id in copied_items.keys():
            sharing = source.user_item(item_id)[1]
            if sharing['access'] != 'private':
                target_item_id = copied_items[item_id]
                target_group_ids = [copied_groups[id] for id in sharing['groups']\
                                    if id in copied_groups]
                share_org = (sharing['access'] == 'org')
                share_public = (sharing['access'] == 'public')
                if not target.is_multitenant():
                    share_public = (share_public or share_org)
                target.share_items(target_owner, [target_item_id],
                                   target_group_ids,\
                                   share_org or share_public,\
                                   share_public)

def copy_groups_sample():
    source = Portal('http://portaldev.arcgis.com', 'wmathot', 'wmathot')
    target = Portal('http://wittm.esri.com', 'admin', 'esri.agp')
    groups = source.groups(q='Administration')
    copied_groups = copy_groups(groups, source, target, 'wmathot')
    for sourceid in copied_groups.keys():
        print 'Copied ' + sourceid + ' to ' + copied_groups[sourceid]

def copy_user_with_groups_and_items():
    source = Portal('http://portaldev.arcgis.com', 'wmathot', 'wmathot')
    target = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    source_owner = source.logged_in_user()['username']
    target_owner = target.logged_in_user()['username']

    # Copy the groups
    groups = source.groups(q='owner:' + source_owner)
    copied_groups = copy_groups(groups, source, target)
    print 'Copied ' + str(len(copied_groups)) + ' groups'

    # Copy the items
    copied_items = copy_user_contents(source, source_owner, target, target_owner)
    print 'Copied ' + str(len(copied_items)) + ' items'

    # Share the items in the target portal
    for item_id in copied_items.keys():
        sharing = source.user_item(item_id)[1]
        if sharing['access'] != 'private':
            target_item_id = copied_items[item_id]
            target_group_ids = [copied_groups[id] for id in sharing['groups']\
                                if id in copied_groups]
            target.share_items(target_owner, [target_item_id], target_group_ids,\
                               sharing['access'] == 'org',\
                               sharing['access'] == 'public')

def copy_group_with_shared_content():
    source = Portal('http://www.arcgis.com')
    target = Portal('http://wittm.esri.com', 'admin', 'esri.agp')
    target_owner = target.logged_in_user()['username']
    group_id = '2394b887a80347fb8544610cfa30489c'

    # Copy the groups
    groups = source.groups(q='id:' + group_id)
    copied_groups = copy_groups(groups, source, target)
    print 'Copied ' + str(len(copied_groups)) + ' groups'

    # Copy the items
    items = source.search(q='group:' + group_id)
    copied_items = copy_items(items, source, target, target_owner,
                              'Copied Items (' + group_id + ')')
    print 'Copied ' + str(len(copied_items)) + ' items'

    # Share the items in the target portal
    for item_id in copied_items.keys():
        sharing = source.user_item(item_id)[1]

        # If we have access to the full sharing properties of the source
        # item, then copy all of them, otherwise just share with the group
        if sharing and sharing['access'] != 'private':
            target_item_id = copied_items[item_id]
            target_group_ids = [copied_groups[id] for id in sharing['groups'] \
                                if id in copied_groups]
            share_org = (sharing['access'] == 'org')
            share_public = (sharing['access'] == 'public')
            if not target.is_multitenant():
                share_public = (share_public or share_org)
            target.share_items(target_owner, [target_item_id],
                               target_group_ids, \
                               share_org or share_public, \
                               share_public)
        else:
            target_item_id = copied_items[item_id]
            target_group_id = copied_groups[group_id]
            target.share_items(target_owner, [target_item_id], \
                               [target_group_id])

def add_update_metadata():
    portal = Portal('http://portaldev.arcgis.com', 'admin', 'esri.agp')
    portal.update_item('02ec2b569a38467dbb78a52ec7eb060e', \
                       metadata='C:\Projects\DOI\RFI\World.mxd.xml')

def signup_user():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    portal.signup('test_user', 'test_user', 'Test User', 'tests@tests.com')

def invite_org_user():
    portal = Portal('http://wittakermathot.maps.arcgis.com', 'wmathot', '***')

    # Prepare the invitations
    invitations = [
            {'fullname': 'James Bond', 'username': 'jbond_wittakermathot',
             'email': 'wmathot@gmail.com', 'role': 'account_user'}]

    # Invite users. Log those who werent invited
    not_invited = portal.invite(invitations, 'test1', 'test2')
    if not_invited:
        print 'Not invited: ' + str(not_invited)

    # Accept the invitations and set the user's password to their username
    accepted_count = 0
    for invitation in invitations:
        username = invitation['username']
        for pending_invitation in portal.invitations(['id', 'username']):
            if username == pending_invitation['username']:
                invitation_id = pending_invitation['id']
                new_password = username
                is_reset = portal.reset_user(username, invitation_id, new_password)
                if is_reset:
                    portal_as_user = Portal('http://www.arcgis.com', username, new_password)
                    is_accepted = portal_as_user.accept(invitation_id)
                    if is_accepted:
                        accepted_count += 1

    print 'Invited ' + str(len(invitations)) + ', Accepted ' + str(accepted_count)

def populate_gallery():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    feature_items_query(portal, 'imagery type:"Web Map"')

def create_demographics_group():
    arcgisonline = Portal('http://www.arcgis.com')
    portal = Portal('http://wittm.esri.com', 'admin', 'esri.agp')
    owner = portal.logged_in_user()['username']
    items = arcgisonline.search(q='demographics owner:esri ' + WEBMAP_ITEM_FILTER)
    copied_items = copy_items(items, arcgisonline, portal, owner)
    group_id = portal.create_group({'title': 'Demographics', 'access': 'public',
                                    'tags': 'demographics'},
                                   thumbnail='http://bit.ly/WEaIh5')
    for item_id in copied_items.values():
        portal.share_items(owner, [item_id], [group_id], True, True)

def update_item_thumbnail():
    portal = Portal('http://wittm.esri.com', 'admin', 'esri.agp')
    portal.update_item('726323baf8f44d6a8c55a77111db9b2c',
                       thumbnail='http://bit.ly/13RRmr0')

def update_group_thumbnail():
    portal = Portal('http://wittm.esri.com', 'admin', 'esri.agp')
    portal.update_group('c0187b0429fa450ab62f4b33dd028f8c',
                        thumbnail='http://bit.ly/13RRmr0')

def print_webmap():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    try:
        webmap = portal.webmap('cb769438c687478e9ccdb8377116ed02')
        pprint(webmap.json(), indent=2, width=120)
    except Exception as e:
        logging.error(e)

def count_webmap_url_references():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    urls = []
    for webmap in portal.webmaps():
        urls.extend(webmap.urls(normalize=True))
    url_counts = dict((url, urls.count(url)) for url in urls)
    pprint(url_counts, indent=2)

def count_webmap_item_references():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    item_ids = []
    for webmap in portal.webmaps():
        item_ids.extend(webmap.item_ids())
    item_id_counts = dict((id, item_ids.count(id)) for id in item_ids)
    pprint(item_id_counts, indent=2)

def find_hostname_references():
    hostname = 'wh94.fltplan.com'
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    hostname_references = []
    url_items = portal.search(['id','type','url'], portalpy.URL_ITEM_FILTER)
    for item in url_items:
        if parse_hostname(item['url']) == hostname:
            hostname_references.append((item['id'], item['type'], item['url']))
    webmaps = portal.webmaps()
    for webmap in webmaps:
        urls = webmap.urls(normalize=True)
        for url in urls:
            if parse_hostname(url) == hostname:
                hostname_references.append((webmap.id, 'Web Map', url))
    pprint(hostname_references, indent=2)

def update_hostname_references():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    hostname_map = {'wh94.fltplan.com:8080': 'wh94.fltplan.com'}
    url_items = portal.search(['id','type','url'], portalpy.URL_ITEM_FILTER)
    for item in url_items:
        url = item.get('url')
        if url:
            url = normalize_url(url)
            host = parse_hostname(url, include_port=True)
            if host in hostname_map:
                url = url.replace(host, hostname_map[host])
                portal.update_item(item['id'], {'url': url})
    webmaps = portal.webmaps()
    for webmap in webmaps:
        is_update = False
        for url in webmap.urls():
            normalized_url = normalize_url(url)
            host = parse_hostname(normalized_url, include_port=True)
            if host in hostname_map:
                new_url = normalized_url.replace(host, hostname_map[host])
                webmap.data = webmap.data.replace(url, new_url)
                is_update = True
        if is_update:
            portal.update_webmap(webmap)

def feature_groups():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    portalpy.config.feature_groups_query(portal, 'Administration', True)

def export_import_content():
    source = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    target = Portal('http://wittm.esri.com', 'admin', 'esri.agp')
    file_path = 'C:\\temp\\export'
    web_content = source.search(q=portalpy.WEB_ITEM_FILTER)
    save_items(source, web_content, file_path, indent=4)
    load_items(target, file_path)

def find_public_content_with_weak_descriptions():
    portal = Portal('http://portaldev.esri.com', 'admin', 'esri.agp')
    public_items = portal.search(q='access:public')
    weak_items = []
    for item in public_items:
        snippet = item.get('snippet')
        description = item.get('description')
        thumbnail = item.get('thumbnail')
        if not snippet or not description or not thumbnail or len(snippet) < 20 \
                       or len(description) < 50:
            weak_items.append(item)
    for weak_item in weak_items:
        owner = weak_item['owner']
        email = portal.user(owner)['email']
        print owner + ', ' + email + ', ' + weak_item['id']


def set_home_page_banner():
    portal = Portal('http://wittm.esri.com', 'admin', 'esri.agp')
    portal.add_resource('custom-banner.jpg',\
                        data='http://www.myterradesic.com/images/header-globe.jpg')
    portal.update_property('rotatorPanels', \
        [{"id":"banner-custom", "innerHTML": "<img src='http://" + portal.hostname +\
        "/sharing/accounts/self/resources/custom-banner.jpg?token=SECURITY_TOKEN' " +\
        "style='-webkit-border-radius:0 0 10px 10px; -moz-border-radius:0 0 10px 10px; " +\
        "-o-border-radius:0 0 10px 10px; border-radius:0 0 10px 10px; margin-top:0; " +\
        "width:960px; height:180px;'/>"}])

def proxy_through_fiddler():
    portal = Portal('http://www.arcgis.com', proxy_host='localhost', proxy_port=8888)
    print portal.info()

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
