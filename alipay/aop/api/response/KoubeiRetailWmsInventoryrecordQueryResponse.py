#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InventoryRecord import InventoryRecord


class KoubeiRetailWmsInventoryrecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsInventoryrecordQueryResponse, self).__init__()
        self._inventory_record_list = None
        self._page_no = None
        self._page_size = None
        self._total_count = None

    @property
    def inventory_record_list(self):
        return self._inventory_record_list

    @inventory_record_list.setter
    def inventory_record_list(self, value):
        if isinstance(value, list):
            self._inventory_record_list = list()
            for i in value:
                if isinstance(i, InventoryRecord):
                    self._inventory_record_list.append(i)
                else:
                    self._inventory_record_list.append(InventoryRecord.from_alipay_dict(i))
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsInventoryrecordQueryResponse, self).parse_response_content(response_content)
        if 'inventory_record_list' in response:
            self.inventory_record_list = response['inventory_record_list']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
