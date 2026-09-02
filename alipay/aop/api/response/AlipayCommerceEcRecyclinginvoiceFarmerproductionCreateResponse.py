#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcRecyclinginvoiceFarmerproductionCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceFarmerproductionCreateResponse, self).__init__()
        self._farmer_item_id = None

    @property
    def farmer_item_id(self):
        return self._farmer_item_id

    @farmer_item_id.setter
    def farmer_item_id(self, value):
        self._farmer_item_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceFarmerproductionCreateResponse, self).parse_response_content(response_content)
        if 'farmer_item_id' in response:
            self.farmer_item_id = response['farmer_item_id']
