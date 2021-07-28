#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainTwcPreauthinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainTwcPreauthinfoQueryResponse, self).__init__()
        self._desc = None
        self._match = None
        self._status = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def match(self):
        return self._match

    @match.setter
    def match(self, value):
        self._match = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainTwcPreauthinfoQueryResponse, self).parse_response_content(response_content)
        if 'desc' in response:
            self.desc = response['desc']
        if 'match' in response:
            self.match = response['match']
        if 'status' in response:
            self.status = response['status']
