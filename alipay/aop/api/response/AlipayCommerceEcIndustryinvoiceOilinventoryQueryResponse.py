#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CompanyRefinedOilInventoryItem import CompanyRefinedOilInventoryItem


class AlipayCommerceEcIndustryinvoiceOilinventoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcIndustryinvoiceOilinventoryQueryResponse, self).__init__()
        self._inventory_list = None

    @property
    def inventory_list(self):
        return self._inventory_list

    @inventory_list.setter
    def inventory_list(self, value):
        if isinstance(value, list):
            self._inventory_list = list()
            for i in value:
                if isinstance(i, CompanyRefinedOilInventoryItem):
                    self._inventory_list.append(i)
                else:
                    self._inventory_list.append(CompanyRefinedOilInventoryItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcIndustryinvoiceOilinventoryQueryResponse, self).parse_response_content(response_content)
        if 'inventory_list' in response:
            self.inventory_list = response['inventory_list']
