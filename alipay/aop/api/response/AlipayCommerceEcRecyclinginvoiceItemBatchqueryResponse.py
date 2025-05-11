#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemQueryOpenResult import ItemQueryOpenResult


class AlipayCommerceEcRecyclinginvoiceItemBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceItemBatchqueryResponse, self).__init__()
        self._curr_page_size = None
        self._data_list = None
        self._page_num = None
        self._page_size = None
        self._total_size = None

    @property
    def curr_page_size(self):
        return self._curr_page_size

    @curr_page_size.setter
    def curr_page_size(self, value):
        self._curr_page_size = value
    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, ItemQueryOpenResult):
                    self._data_list.append(i)
                else:
                    self._data_list.append(ItemQueryOpenResult.from_alipay_dict(i))
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
        response = super(AlipayCommerceEcRecyclinginvoiceItemBatchqueryResponse, self).parse_response_content(response_content)
        if 'curr_page_size' in response:
            self.curr_page_size = response['curr_page_size']
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
