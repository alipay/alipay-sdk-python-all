#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskBackgroundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskBackgroundQueryResponse, self).__init__()
        self._detail_info = None

    @property
    def detail_info(self):
        return self._detail_info

    @detail_info.setter
    def detail_info(self, value):
        self._detail_info = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskBackgroundQueryResponse, self).parse_response_content(response_content)
        if 'detail_info' in response:
            self.detail_info = response['detail_info']
