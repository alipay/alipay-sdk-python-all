#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZolozIdentificationZolozidGetResponse(AlipayResponse):

    def __init__(self):
        super(ZolozIdentificationZolozidGetResponse, self).__init__()
        self._result_info = None

    @property
    def result_info(self):
        return self._result_info

    @result_info.setter
    def result_info(self, value):
        self._result_info = value

    def parse_response_content(self, response_content):
        response = super(ZolozIdentificationZolozidGetResponse, self).parse_response_content(response_content)
        if 'result_info' in response:
            self.result_info = response['result_info']
