#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WarehouseVO import WarehouseVO


class KoubeiRetailWmsWarehouseQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsWarehouseQueryResponse, self).__init__()
        self._total_count = None
        self._warehouses = None

    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def warehouses(self):
        return self._warehouses

    @warehouses.setter
    def warehouses(self, value):
        if isinstance(value, list):
            self._warehouses = list()
            for i in value:
                if isinstance(i, WarehouseVO):
                    self._warehouses.append(i)
                else:
                    self._warehouses.append(WarehouseVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsWarehouseQueryResponse, self).parse_response_content(response_content)
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'warehouses' in response:
            self.warehouses = response['warehouses']
