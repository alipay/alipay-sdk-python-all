#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Inventory import Inventory


class KoubeiRetailWmsBatchinventoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsBatchinventoryQueryResponse, self).__init__()
        self._inventory_list = None

    @property
    def inventory_list(self):
        return self._inventory_list

    @inventory_list.setter
    def inventory_list(self, value):
        if isinstance(value, list):
            self._inventory_list = list()
            for i in value:
                if isinstance(i, Inventory):
                    self._inventory_list.append(i)
                else:
                    self._inventory_list.append(Inventory.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsBatchinventoryQueryResponse, self).parse_response_content(response_content)
        if 'inventory_list' in response:
            self.inventory_list = response['inventory_list']
