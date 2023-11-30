#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SupplierSkuInfo import SupplierSkuInfo


class AntProdpaasProductSkuListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntProdpaasProductSkuListQueryResponse, self).__init__()
        self._flag = None
        self._item = None

    @property
    def flag(self):
        return self._flag

    @flag.setter
    def flag(self, value):
        self._flag = value
    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        if isinstance(value, SupplierSkuInfo):
            self._item = value
        else:
            self._item = SupplierSkuInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntProdpaasProductSkuListQueryResponse, self).parse_response_content(response_content)
        if 'flag' in response:
            self.flag = response['flag']
        if 'item' in response:
            self.item = response['item']
