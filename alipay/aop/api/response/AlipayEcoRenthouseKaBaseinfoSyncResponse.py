#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoRenthouseKaBaseinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoRenthouseKaBaseinfoSyncResponse, self).__init__()
        self._ka_code = None

    @property
    def ka_code(self):
        return self._ka_code

    @ka_code.setter
    def ka_code(self, value):
        self._ka_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoRenthouseKaBaseinfoSyncResponse, self).parse_response_content(response_content)
        if 'ka_code' in response:
            self.ka_code = response['ka_code']
