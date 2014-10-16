from urllib2 import urlopen
import json

ROOT_URL = "https://www.govtrack.us/api/v2/"


def get(url):
    response = urlopen(url).read()
    return json.loads(response)


class Legislators(object):

    def current_congress(self, limit=3):
        url = ROOT_URL + "role?current=true&limit=%d" % limit
        return get(url)

    def committees(self, pks):
        pk_params = "%d" % pks[0]
        for pk in pks[1:]:
            pk_params += "|%d" % pk

        url = ROOT_URL + "committee_member?person__in=%s" % pk_params
        committees_list = get(url)
        membership = {}
        for x in committees_list['objects']:
            pid = x['person']['id']
            mems = membership.get(pid, [])
            mems.append(x['committee']['name'])
            membership[pid] = mems
        return membership


class Bills(object):
    URL = ROOT_URL + "bill"
