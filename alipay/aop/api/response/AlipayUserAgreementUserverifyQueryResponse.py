#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementUserverifyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementUserverifyQueryResponse, self).__init__()
        self._user_match = None

    @property
    def user_match(self):
        return self._user_match

    @user_match.setter
    def user_match(self, value):
        self._user_match = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementUserverifyQueryResponse, self).parse_response_content(response_content)
        if 'user_match' in response:
            self.user_match = response['user_match']
