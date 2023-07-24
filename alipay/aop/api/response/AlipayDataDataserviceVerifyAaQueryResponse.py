#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceVerifyAaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceVerifyAaQueryResponse, self).__init__()
        self._ces = None

    @property
    def ces(self):
        return self._ces

    @ces.setter
    def ces(self, value):
        self._ces = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceVerifyAaQueryResponse, self).parse_response_content(response_content)
        if 'ces' in response:
            self.ces = response['ces']
