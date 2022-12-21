#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DataItem import DataItem


class AlipayOpenMiniCloudAositemQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniCloudAositemQueryResponse, self).__init__()
        self._aggregation_result = None
        self._item_total_count = None
        self._result = None
        self._trace_id = None

    @property
    def aggregation_result(self):
        return self._aggregation_result

    @aggregation_result.setter
    def aggregation_result(self, value):
        self._aggregation_result = value
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
                if isinstance(i, DataItem):
                    self._result.append(i)
                else:
                    self._result.append(DataItem.from_alipay_dict(i))
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniCloudAositemQueryResponse, self).parse_response_content(response_content)
        if 'aggregation_result' in response:
            self.aggregation_result = response['aggregation_result']
        if 'item_total_count' in response:
            self.item_total_count = response['item_total_count']
        if 'result' in response:
            self.result = response['result']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
