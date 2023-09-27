#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechMorseDataDataserviceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseDataDataserviceQueryResponse, self).__init__()
        self._biz_no = None
        self._result = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseDataDataserviceQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'result' in response:
            self.result = response['result']
