#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NDeviceMetricsListForDayResponse import NDeviceMetricsListForDayResponse
from alipay.aop.api.domain.NDeviceMetricsListForDayResponse import NDeviceMetricsListForDayResponse


class AlipayCommerceOperationNdeviceMetricsfordayBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationNdeviceMetricsfordayBatchqueryResponse, self).__init__()
        self._count = None
        self._data = None
        self._list = None
        self._page_num = None
        self._page_size = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, NDeviceMetricsListForDayResponse):
                    self._data.append(i)
                else:
                    self._data.append(NDeviceMetricsListForDayResponse.from_alipay_dict(i))
    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, NDeviceMetricsListForDayResponse):
            self._list = value
        else:
            self._list = NDeviceMetricsListForDayResponse.from_alipay_dict(value)
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationNdeviceMetricsfordayBatchqueryResponse, self).parse_response_content(response_content)
        if 'count' in response:
            self.count = response['count']
        if 'data' in response:
            self.data = response['data']
        if 'list' in response:
            self.list = response['list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
