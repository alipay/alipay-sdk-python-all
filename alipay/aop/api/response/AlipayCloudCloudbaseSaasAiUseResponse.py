#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseSaasAiUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseSaasAiUseResponse, self).__init__()
        self._result_str = None

    @property
    def result_str(self):
        return self._result_str

    @result_str.setter
    def result_str(self, value):
        self._result_str = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseSaasAiUseResponse, self).parse_response_content(response_content)
        if 'result_str' in response:
            self.result_str = response['result_str']
