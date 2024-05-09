#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAcommunicationCrowdMatchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationCrowdMatchResponse, self).__init__()
        self._match = None

    @property
    def match(self):
        return self._match

    @match.setter
    def match(self, value):
        if isinstance(value, list):
            self._match = list()
            for i in value:
                self._match.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationCrowdMatchResponse, self).parse_response_content(response_content)
        if 'match' in response:
            self.match = response['match']
