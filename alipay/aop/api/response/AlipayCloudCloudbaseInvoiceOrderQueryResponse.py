#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ConsumeOrder import ConsumeOrder


class AlipayCloudCloudbaseInvoiceOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseInvoiceOrderQueryResponse, self).__init__()
        self._consume_orders = None
        self._message = None
        self._page_num = None
        self._page_size = None
        self._total = None
        self._total_page = None

    @property
    def consume_orders(self):
        return self._consume_orders

    @consume_orders.setter
    def consume_orders(self, value):
        if isinstance(value, list):
            self._consume_orders = list()
            for i in value:
                if isinstance(i, ConsumeOrder):
                    self._consume_orders.append(i)
                else:
                    self._consume_orders.append(ConsumeOrder.from_alipay_dict(i))
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
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
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseInvoiceOrderQueryResponse, self).parse_response_content(response_content)
        if 'consume_orders' in response:
            self.consume_orders = response['consume_orders']
        if 'message' in response:
            self.message = response['message']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
        if 'total_page' in response:
            self.total_page = response['total_page']
