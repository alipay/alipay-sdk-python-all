#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechMorseMarketingSrtaNanonymousCallbackResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingSrtaNanonymousCallbackResponse, self).__init__()
        self._biz_no = None
        self._callback_result = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def callback_result(self):
        return self._callback_result

    @callback_result.setter
    def callback_result(self, value):
        self._callback_result = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingSrtaNanonymousCallbackResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'callback_result' in response:
            self.callback_result = response['callback_result']
