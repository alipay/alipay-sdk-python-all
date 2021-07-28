#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayAppPocketmoneyAuthQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppPocketmoneyAuthQueryResponse, self).__init__()
        self._auth_result = None
        self._change_code_id = None
        self._vendor_parent_id = None

    @property
    def auth_result(self):
        return self._auth_result

    @auth_result.setter
    def auth_result(self, value):
        self._auth_result = value
    @property
    def change_code_id(self):
        return self._change_code_id

    @change_code_id.setter
    def change_code_id(self, value):
        self._change_code_id = value
    @property
    def vendor_parent_id(self):
        return self._vendor_parent_id

    @vendor_parent_id.setter
    def vendor_parent_id(self, value):
        self._vendor_parent_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppPocketmoneyAuthQueryResponse, self).parse_response_content(response_content)
        if 'auth_result' in response:
            self.auth_result = response['auth_result']
        if 'change_code_id' in response:
            self.change_code_id = response['change_code_id']
        if 'vendor_parent_id' in response:
            self.vendor_parent_id = response['vendor_parent_id']
