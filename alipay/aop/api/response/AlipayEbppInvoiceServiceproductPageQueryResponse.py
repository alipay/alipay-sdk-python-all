#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceProductInfo import ServiceProductInfo


class AlipayEbppInvoiceServiceproductPageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceServiceproductPageQueryResponse, self).__init__()
        self._items = None
        self._page_no = None
        self._page_size = None
        self._total_num = None
        self._total_size = None

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, ServiceProductInfo):
                    self._items.append(i)
                else:
                    self._items.append(ServiceProductInfo.from_alipay_dict(i))
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceServiceproductPageQueryResponse, self).parse_response_content(response_content)
        if 'items' in response:
            self.items = response['items']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_num' in response:
            self.total_num = response['total_num']
        if 'total_size' in response:
            self.total_size = response['total_size']
