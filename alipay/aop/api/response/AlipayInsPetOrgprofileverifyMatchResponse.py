#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MatchPetList import MatchPetList


class AlipayInsPetOrgprofileverifyMatchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsPetOrgprofileverifyMatchResponse, self).__init__()
        self._match_pet_list = None

    @property
    def match_pet_list(self):
        return self._match_pet_list

    @match_pet_list.setter
    def match_pet_list(self, value):
        if isinstance(value, MatchPetList):
            self._match_pet_list = value
        else:
            self._match_pet_list = MatchPetList.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsPetOrgprofileverifyMatchResponse, self).parse_response_content(response_content)
        if 'match_pet_list' in response:
            self.match_pet_list = response['match_pet_list']
