#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseObglobalPermissionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObglobalPermissionQueryResponse, self).__init__()
        self._auth_flag = None

    @property
    def auth_flag(self):
        return self._auth_flag

    @auth_flag.setter
    def auth_flag(self, value):
        self._auth_flag = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObglobalPermissionQueryResponse, self).parse_response_content(response_content)
        if 'auth_flag' in response:
            self.auth_flag = response['auth_flag']
