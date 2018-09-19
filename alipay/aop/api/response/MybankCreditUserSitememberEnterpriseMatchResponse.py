#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditUserSitememberEnterpriseMatchResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditUserSitememberEnterpriseMatchResponse, self).__init__()
        self._match = None
        self._not_match_code = None

    @property
    def match(self):
        return self._match

    @match.setter
    def match(self, value):
        self._match = value
    @property
    def not_match_code(self):
        return self._not_match_code

    @not_match_code.setter
    def not_match_code(self, value):
        self._not_match_code = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditUserSitememberEnterpriseMatchResponse, self).parse_response_content(response_content)
        if 'match' in response:
            self.match = response['match']
        if 'not_match_code' in response:
            self.not_match_code = response['not_match_code']
