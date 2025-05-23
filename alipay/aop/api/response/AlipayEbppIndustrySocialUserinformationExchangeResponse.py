#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySocialUserinformationExchangeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySocialUserinformationExchangeResponse, self).__init__()
        self._encrypt_id = None
        self._sm_4_iv = None

    @property
    def encrypt_id(self):
        return self._encrypt_id

    @encrypt_id.setter
    def encrypt_id(self, value):
        self._encrypt_id = value
    @property
    def sm_4_iv(self):
        return self._sm_4_iv

    @sm_4_iv.setter
    def sm_4_iv(self, value):
        self._sm_4_iv = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySocialUserinformationExchangeResponse, self).parse_response_content(response_content)
        if 'encrypt_id' in response:
            self.encrypt_id = response['encrypt_id']
        if 'sm_4_iv' in response:
            self.sm_4_iv = response['sm_4_iv']
