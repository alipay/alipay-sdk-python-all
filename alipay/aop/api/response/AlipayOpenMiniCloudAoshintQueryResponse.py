#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AosHintItem import AosHintItem


class AlipayOpenMiniCloudAoshintQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniCloudAoshintQueryResponse, self).__init__()
        self._item_total_count = None
        self._result = None
        self._trace_id = None

    @property
    def item_total_count(self):
        return self._item_total_count

    @item_total_count.setter
    def item_total_count(self, value):
        self._item_total_count = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, list):
            self._result = list()
            for i in value:
                if isinstance(i, AosHintItem):
                    self._result.append(i)
                else:
                    self._result.append(AosHintItem.from_alipay_dict(i))
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniCloudAoshintQueryResponse, self).parse_response_content(response_content)
        if 'item_total_count' in response:
            self.item_total_count = response['item_total_count']
        if 'result' in response:
            self.result = response['result']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
