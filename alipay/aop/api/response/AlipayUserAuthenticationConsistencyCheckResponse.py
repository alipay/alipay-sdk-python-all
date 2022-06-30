#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAuthenticationConsistencyCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAuthenticationConsistencyCheckResponse, self).__init__()
        self._match = None

    @property
    def match(self):
        return self._match

    @match.setter
    def match(self, value):
        self._match = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAuthenticationConsistencyCheckResponse, self).parse_response_content(response_content)
        if 'match' in response:
            self.match = response['match']
