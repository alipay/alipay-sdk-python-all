#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNordermaterialsapplyMaterialsCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordermaterialsapplyMaterialsCreateResponse, self).__init__()
        self._qr_code_url_list = None

    @property
    def qr_code_url_list(self):
        return self._qr_code_url_list

    @qr_code_url_list.setter
    def qr_code_url_list(self, value):
        if isinstance(value, list):
            self._qr_code_url_list = list()
            for i in value:
                self._qr_code_url_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordermaterialsapplyMaterialsCreateResponse, self).parse_response_content(response_content)
        if 'qr_code_url_list' in response:
            self.qr_code_url_list = response['qr_code_url_list']
