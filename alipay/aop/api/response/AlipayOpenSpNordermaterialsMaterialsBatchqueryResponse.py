#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopMaterialsInfo import ShopMaterialsInfo


class AlipayOpenSpNordermaterialsMaterialsBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordermaterialsMaterialsBatchqueryResponse, self).__init__()
        self._data_list = None
        self._data_total = None
        self._has_next_page = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, ShopMaterialsInfo):
                    self._data_list.append(i)
                else:
                    self._data_list.append(ShopMaterialsInfo.from_alipay_dict(i))
    @property
    def data_total(self):
        return self._data_total

    @data_total.setter
    def data_total(self, value):
        self._data_total = value
    @property
    def has_next_page(self):
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, value):
        self._has_next_page = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordermaterialsMaterialsBatchqueryResponse, self).parse_response_content(response_content)
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'data_total' in response:
            self.data_total = response['data_total']
        if 'has_next_page' in response:
            self.has_next_page = response['has_next_page']
