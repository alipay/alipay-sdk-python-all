#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecyclingFarmerItemResult import RecyclingFarmerItemResult


class AlipayCommerceEcRecyclinginvoiceFarmerproductionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceFarmerproductionQueryResponse, self).__init__()
        self._farmer_item_list = None
        self._total_count = None

    @property
    def farmer_item_list(self):
        return self._farmer_item_list

    @farmer_item_list.setter
    def farmer_item_list(self, value):
        if isinstance(value, list):
            self._farmer_item_list = list()
            for i in value:
                if isinstance(i, RecyclingFarmerItemResult):
                    self._farmer_item_list.append(i)
                else:
                    self._farmer_item_list.append(RecyclingFarmerItemResult.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceFarmerproductionQueryResponse, self).parse_response_content(response_content)
        if 'farmer_item_list' in response:
            self.farmer_item_list = response['farmer_item_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
