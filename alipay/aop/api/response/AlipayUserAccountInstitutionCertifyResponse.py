#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAccountInstitutionCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountInstitutionCertifyResponse, self).__init__()
        self._match = None
        self._user_id = None

    @property
    def match(self):
        return self._match

    @match.setter
    def match(self, value):
        self._match = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAccountInstitutionCertifyResponse, self).parse_response_content(response_content)
        if 'match' in response:
            self.match = response['match']
        if 'user_id' in response:
            self.user_id = response['user_id']
