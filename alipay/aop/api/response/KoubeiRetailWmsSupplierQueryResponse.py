#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SupplierVO import SupplierVO


class KoubeiRetailWmsSupplierQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsSupplierQueryResponse, self).__init__()
        self._suppliers = None
        self._total_count = None

    @property
    def suppliers(self):
        return self._suppliers

    @suppliers.setter
    def suppliers(self, value):
        if isinstance(value, list):
            self._suppliers = list()
            for i in value:
                if isinstance(i, SupplierVO):
                    self._suppliers.append(i)
                else:
                    self._suppliers.append(SupplierVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsSupplierQueryResponse, self).parse_response_content(response_content)
        if 'suppliers' in response:
            self.suppliers = response['suppliers']
        if 'total_count' in response:
            self.total_count = response['total_count']
