#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VehSearchItem import VehSearchItem


class AlipayEcoMycarVehMultiterminalBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarVehMultiterminalBatchqueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._search_list = None
        self._total_page = None
        self._total_size = None

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
    def search_list(self):
        return self._search_list

    @search_list.setter
    def search_list(self, value):
        if isinstance(value, list):
            self._search_list = list()
            for i in value:
                if isinstance(i, VehSearchItem):
                    self._search_list.append(i)
                else:
                    self._search_list.append(VehSearchItem.from_alipay_dict(i))
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarVehMultiterminalBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'search_list' in response:
            self.search_list = response['search_list']
        if 'total_page' in response:
            self.total_page = response['total_page']
        if 'total_size' in response:
            self.total_size = response['total_size']
