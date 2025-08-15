#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAuthenticationConsistencyCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAuthenticationConsistencyCheckResponse, self).__init__()
        self._certify_url = None
        self._match = None
        self._not_certify_msg = None

    @property
    def certify_url(self):
        return self._certify_url

    @certify_url.setter
    def certify_url(self, value):
        self._certify_url = value
    @property
    def match(self):
        return self._match

    @match.setter
    def match(self, value):
        self._match = value
    @property
    def not_certify_msg(self):
        return self._not_certify_msg

    @not_certify_msg.setter
    def not_certify_msg(self, value):
        self._not_certify_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAuthenticationConsistencyCheckResponse, self).parse_response_content(response_content)
        if 'certify_url' in response:
            self.certify_url = response['certify_url']
        if 'match' in response:
            self.match = response['match']
        if 'not_certify_msg' in response:
            self.not_certify_msg = response['not_certify_msg']
