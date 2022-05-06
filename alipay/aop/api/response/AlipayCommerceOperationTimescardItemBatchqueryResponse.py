#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TimeCardItemInfo import TimeCardItemInfo


class AlipayCommerceOperationTimescardItemBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationTimescardItemBatchqueryResponse, self).__init__()
        self._datas = None
        self._page_num = None
        self._page_size = None
        self._total_size = None

    @property
    def datas(self):
        return self._datas

    @datas.setter
    def datas(self, value):
        if isinstance(value, TimeCardItemInfo):
            self._datas = value
        else:
            self._datas = TimeCardItemInfo.from_alipay_dict(value)
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
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationTimescardItemBatchqueryResponse, self).parse_response_content(response_content)
        if 'datas' in response:
            self.datas = response['datas']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
