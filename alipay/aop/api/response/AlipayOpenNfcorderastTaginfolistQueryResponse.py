#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NOrderTagDetailDTO import NOrderTagDetailDTO


class AlipayOpenNfcorderastTaginfolistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenNfcorderastTaginfolistQueryResponse, self).__init__()
        self._data = None
        self._has_next = None
        self._page_num = None
        self._page_size = None
        self._pages = None
        self._total = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, NOrderTagDetailDTO):
            self._data = value
        else:
            self._data = NOrderTagDetailDTO.from_alipay_dict(value)
    @property
    def has_next(self):
        return self._has_next

    @has_next.setter
    def has_next(self, value):
        self._has_next = value
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
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        self._pages = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenNfcorderastTaginfolistQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'has_next' in response:
            self.has_next = response['has_next']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'pages' in response:
            self.pages = response['pages']
        if 'total' in response:
            self.total = response['total']
