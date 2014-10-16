import pytest
from django.test import TestCase
from govtrack.wrapper import Legislators

class LegislatorTests(TestCase):
	def test_people_list(self):
		ppl =  Legislators()
		resp = ppl.current_congress()
		assert type(resp) is dict

		pks = [x['person']['id'] for x in resp['objects']]
		pytest.set_trace()
		resp = ppl.committees(pks)