#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OutputInvoiceReceiptOpenApiResponse import OutputInvoiceReceiptOpenApiResponse


class AlipayBossFncOutputinvoiceRcptQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncOutputinvoiceRcptQueryResponse, self).__init__()
        self._current_page = None
        self._items_page = None
        self._result_set = None
        self._total_items = None
        self._total_pages = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def items_page(self):
        return self._items_page

    @items_page.setter
    def items_page(self, value):
        self._items_page = value
    @property
    def result_set(self):
        return self._result_set

    @result_set.setter
    def result_set(self, value):
        if isinstance(value, list):
            self._result_set = list()
            for i in value:
                if isinstance(i, OutputInvoiceReceiptOpenApiResponse):
                    self._result_set.append(i)
                else:
                    self._result_set.append(OutputInvoiceReceiptOpenApiResponse.from_alipay_dict(i))
    @property
    def total_items(self):
        return self._total_items

    @total_items.setter
    def total_items(self, value):
        self._total_items = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncOutputinvoiceRcptQueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'items_page' in response:
            self.items_page = response['items_page']
        if 'result_set' in response:
            self.result_set = response['result_set']
        if 'total_items' in response:
            self.total_items = response['total_items']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
