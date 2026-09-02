#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VehOpenSeriesDTO import VehOpenSeriesDTO


class AlipayEcoMycarVehlibSeriesQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarVehlibSeriesQueryResponse, self).__init__()
        self._list = None
        self._page_num = None
        self._page_size = None
        self._total_page = None
        self._total_size = None

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, list):
            self._list = list()
            for i in value:
                if isinstance(i, VehOpenSeriesDTO):
                    self._list.append(i)
                else:
                    self._list.append(VehOpenSeriesDTO.from_alipay_dict(i))
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
        response = super(AlipayEcoMycarVehlibSeriesQueryResponse, self).parse_response_content(response_content)
        if 'list' in response:
            self.list = response['list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_page' in response:
            self.total_page = response['total_page']
        if 'total_size' in response:
            self.total_size = response['total_size']
