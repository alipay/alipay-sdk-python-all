#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHdfLiveCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfLiveCloseResponse, self).__init__()
        self._biz_trace_id = None

    @property
    def biz_trace_id(self):
        return self._biz_trace_id

    @biz_trace_id.setter
    def biz_trace_id(self, value):
        self._biz_trace_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfLiveCloseResponse, self).parse_response_content(response_content)
        if 'biz_trace_id' in response:
            self.biz_trace_id = response['biz_trace_id']
