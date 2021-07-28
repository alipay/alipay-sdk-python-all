#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainTwcUserinfoMatchResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainTwcUserinfoMatchResponse, self).__init__()
        self._cousumer_id_hash = None
        self._desc = None
        self._match_success = None

    @property
    def cousumer_id_hash(self):
        return self._cousumer_id_hash

    @cousumer_id_hash.setter
    def cousumer_id_hash(self, value):
        self._cousumer_id_hash = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def match_success(self):
        return self._match_success

    @match_success.setter
    def match_success(self, value):
        self._match_success = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainTwcUserinfoMatchResponse, self).parse_response_content(response_content)
        if 'cousumer_id_hash' in response:
            self.cousumer_id_hash = response['cousumer_id_hash']
        if 'desc' in response:
            self.desc = response['desc']
        if 'match_success' in response:
            self.match_success = response['match_success']
