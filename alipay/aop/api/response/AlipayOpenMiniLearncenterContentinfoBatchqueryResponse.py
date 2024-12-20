#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LearnCenterContentInfo import LearnCenterContentInfo


class AlipayOpenMiniLearncenterContentinfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniLearncenterContentinfoBatchqueryResponse, self).__init__()
        self._data_list = None
        self._page_num = None
        self._page_size = None
        self._total = None
        self._total_pages = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, LearnCenterContentInfo):
            self._data_list = value
        else:
            self._data_list = LearnCenterContentInfo.from_alipay_dict(value)
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
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniLearncenterContentinfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
