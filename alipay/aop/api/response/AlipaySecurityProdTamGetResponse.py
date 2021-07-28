#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdTamGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTamGetResponse, self).__init__()
        self._encrypted_ta_bin = None
        self._encrypted_ta_data = None
        self._ext_info = None
        self._return_code = None
        self._return_desc = None
        self._ta_hash = None
        self._ta_info = None

    @property
    def encrypted_ta_bin(self):
        return self._encrypted_ta_bin

    @encrypted_ta_bin.setter
    def encrypted_ta_bin(self, value):
        self._encrypted_ta_bin = value
    @property
    def encrypted_ta_data(self):
        return self._encrypted_ta_data

    @encrypted_ta_data.setter
    def encrypted_ta_data(self, value):
        self._encrypted_ta_data = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def return_code(self):
        return self._return_code

    @return_code.setter
    def return_code(self, value):
        self._return_code = value
    @property
    def return_desc(self):
        return self._return_desc

    @return_desc.setter
    def return_desc(self, value):
        self._return_desc = value
    @property
    def ta_hash(self):
        return self._ta_hash

    @ta_hash.setter
    def ta_hash(self, value):
        self._ta_hash = value
    @property
    def ta_info(self):
        return self._ta_info

    @ta_info.setter
    def ta_info(self, value):
        self._ta_info = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTamGetResponse, self).parse_response_content(response_content)
        if 'encrypted_ta_bin' in response:
            self.encrypted_ta_bin = response['encrypted_ta_bin']
        if 'encrypted_ta_data' in response:
            self.encrypted_ta_data = response['encrypted_ta_data']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_desc' in response:
            self.return_desc = response['return_desc']
        if 'ta_hash' in response:
            self.ta_hash = response['ta_hash']
        if 'ta_info' in response:
            self.ta_info = response['ta_info']
