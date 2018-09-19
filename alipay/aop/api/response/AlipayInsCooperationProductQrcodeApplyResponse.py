#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsCooperationProductQrcodeApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsCooperationProductQrcodeApplyResponse, self).__init__()
        self._code_url = None

    @property
    def code_url(self):
        return self._code_url

    @code_url.setter
    def code_url(self, value):
        self._code_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsCooperationProductQrcodeApplyResponse, self).parse_response_content(response_content)
        if 'code_url' in response:
            self.code_url = response['code_url']
