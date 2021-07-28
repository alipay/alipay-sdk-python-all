#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniEntityBindVO import MiniEntityBindVO


class AlipayOpenMiniShopRelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniShopRelationQueryResponse, self).__init__()
        self._current_page_num = None
        self._data_list = None
        self._per_page_count = None
        self._total_count = None

    @property
    def current_page_num(self):
        return self._current_page_num

    @current_page_num.setter
    def current_page_num(self, value):
        self._current_page_num = value
    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, MiniEntityBindVO):
                    self._data_list.append(i)
                else:
                    self._data_list.append(MiniEntityBindVO.from_alipay_dict(i))
    @property
    def per_page_count(self):
        return self._per_page_count

    @per_page_count.setter
    def per_page_count(self, value):
        self._per_page_count = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniShopRelationQueryResponse, self).parse_response_content(response_content)
        if 'current_page_num' in response:
            self.current_page_num = response['current_page_num']
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'per_page_count' in response:
            self.per_page_count = response['per_page_count']
        if 'total_count' in response:
            self.total_count = response['total_count']
