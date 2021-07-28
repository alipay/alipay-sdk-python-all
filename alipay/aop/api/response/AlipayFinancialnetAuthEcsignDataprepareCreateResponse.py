#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthEcsignDataprepareCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthEcsignDataprepareCreateResponse, self).__init__()
        self._ext_info = None
        self._jump_type = None
        self._jump_url = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def jump_type(self):
        return self._jump_type

    @jump_type.setter
    def jump_type(self, value):
        self._jump_type = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthEcsignDataprepareCreateResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'jump_type' in response:
            self.jump_type = response['jump_type']
        if 'jump_url' in response:
            self.jump_url = response['jump_url']
