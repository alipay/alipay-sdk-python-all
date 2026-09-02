#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SolWifiShopInfo import SolWifiShopInfo


class AlipayCommerceCityfacilitatorWifiShopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCityfacilitatorWifiShopQueryResponse, self).__init__()
        self._data = None
        self._page_number = None
        self._page_size = None
        self._total = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, SolWifiShopInfo):
                    self._data.append(i)
                else:
                    self._data.append(SolWifiShopInfo.from_alipay_dict(i))
    @property
    def page_number(self):
        return self._page_number

    @page_number.setter
    def page_number(self, value):
        self._page_number = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCityfacilitatorWifiShopQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'page_number' in response:
            self.page_number = response['page_number']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
