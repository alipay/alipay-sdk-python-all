#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentProcurementOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentProcurementOrderCreateResponse, self).__init__()
        self._out_procurement_order_id = None
        self._procurement_order_id = None

    @property
    def out_procurement_order_id(self):
        return self._out_procurement_order_id

    @out_procurement_order_id.setter
    def out_procurement_order_id(self, value):
        self._out_procurement_order_id = value
    @property
    def procurement_order_id(self):
        return self._procurement_order_id

    @procurement_order_id.setter
    def procurement_order_id(self, value):
        self._procurement_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentProcurementOrderCreateResponse, self).parse_response_content(response_content)
        if 'out_procurement_order_id' in response:
            self.out_procurement_order_id = response['out_procurement_order_id']
        if 'procurement_order_id' in response:
            self.procurement_order_id = response['procurement_order_id']
