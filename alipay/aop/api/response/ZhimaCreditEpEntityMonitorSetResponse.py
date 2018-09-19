#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpEntityMonitorSetResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpEntityMonitorSetResponse, self).__init__()
        self._biz_success = None

    @property
    def biz_success(self):
        return self._biz_success

    @biz_success.setter
    def biz_success(self, value):
        self._biz_success = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpEntityMonitorSetResponse, self).parse_response_content(response_content)
        if 'biz_success' in response:
            self.biz_success = response['biz_success']
