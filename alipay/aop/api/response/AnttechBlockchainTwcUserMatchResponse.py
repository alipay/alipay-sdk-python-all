#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainTwcUserMatchResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainTwcUserMatchResponse, self).__init__()
        self._desc = None
        self._match_success = None

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
        response = super(AnttechBlockchainTwcUserMatchResponse, self).parse_response_content(response_content)
        if 'desc' in response:
            self.desc = response['desc']
        if 'match_success' in response:
            self.match_success = response['match_success']
