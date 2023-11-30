#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PointInfo import PointInfo


class AlipayCommerceIotPointQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotPointQueryResponse, self).__init__()
        self._cur_page = None
        self._data = None
        self._total = None

    @property
    def cur_page(self):
        return self._cur_page

    @cur_page.setter
    def cur_page(self, value):
        self._cur_page = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, PointInfo):
                    self._data.append(i)
                else:
                    self._data.append(PointInfo.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotPointQueryResponse, self).parse_response_content(response_content)
        if 'cur_page' in response:
            self.cur_page = response['cur_page']
        if 'data' in response:
            self.data = response['data']
        if 'total' in response:
            self.total = response['total']
