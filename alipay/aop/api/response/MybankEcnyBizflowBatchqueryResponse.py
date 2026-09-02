#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BizFlowInfo import BizFlowInfo


class MybankEcnyBizflowBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankEcnyBizflowBatchqueryResponse, self).__init__()
        self._data_list = None
        self._next_cursor = None
        self._page_size = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, BizFlowInfo):
                    self._data_list.append(i)
                else:
                    self._data_list.append(BizFlowInfo.from_alipay_dict(i))
    @property
    def next_cursor(self):
        return self._next_cursor

    @next_cursor.setter
    def next_cursor(self, value):
        self._next_cursor = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value

    def parse_response_content(self, response_content):
        response = super(MybankEcnyBizflowBatchqueryResponse, self).parse_response_content(response_content)
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'next_cursor' in response:
            self.next_cursor = response['next_cursor']
        if 'page_size' in response:
            self.page_size = response['page_size']
