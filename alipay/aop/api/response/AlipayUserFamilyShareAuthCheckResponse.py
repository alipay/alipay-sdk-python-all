#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserFamilyShareAuthCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserFamilyShareAuthCheckResponse, self).__init__()
        self._has_sharing_auth = None

    @property
    def has_sharing_auth(self):
        return self._has_sharing_auth

    @has_sharing_auth.setter
    def has_sharing_auth(self, value):
        self._has_sharing_auth = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserFamilyShareAuthCheckResponse, self).parse_response_content(response_content)
        if 'has_sharing_auth' in response:
            self.has_sharing_auth = response['has_sharing_auth']
