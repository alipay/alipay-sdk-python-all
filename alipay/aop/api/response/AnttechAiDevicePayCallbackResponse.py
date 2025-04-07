#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechAiDevicePayCallbackResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiDevicePayCallbackResponse, self).__init__()
        self._biz_receiet = None
        self._request_id = None

    @property
    def biz_receiet(self):
        return self._biz_receiet

    @biz_receiet.setter
    def biz_receiet(self, value):
        self._biz_receiet = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechAiDevicePayCallbackResponse, self).parse_response_content(response_content)
        if 'biz_receiet' in response:
            self.biz_receiet = response['biz_receiet']
        if 'request_id' in response:
            self.request_id = response['request_id']
