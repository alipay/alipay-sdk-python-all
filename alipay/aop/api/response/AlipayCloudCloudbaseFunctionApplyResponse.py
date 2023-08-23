#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseFunctionApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseFunctionApplyResponse, self).__init__()
        self._biz_trace_id = None
        self._cost = None
        self._data = None

    @property
    def biz_trace_id(self):
        return self._biz_trace_id

    @biz_trace_id.setter
    def biz_trace_id(self, value):
        self._biz_trace_id = value
    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseFunctionApplyResponse, self).parse_response_content(response_content)
        if 'biz_trace_id' in response:
            self.biz_trace_id = response['biz_trace_id']
        if 'cost' in response:
            self.cost = response['cost']
        if 'data' in response:
            self.data = response['data']
