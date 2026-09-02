#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentProcurementOrderModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentProcurementOrderModifyResponse, self).__init__()
        self._modify_status = None
        self._procurement_order_id = None

    @property
    def modify_status(self):
        return self._modify_status

    @modify_status.setter
    def modify_status(self, value):
        self._modify_status = value
    @property
    def procurement_order_id(self):
        return self._procurement_order_id

    @procurement_order_id.setter
    def procurement_order_id(self, value):
        self._procurement_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentProcurementOrderModifyResponse, self).parse_response_content(response_content)
        if 'modify_status' in response:
            self.modify_status = response['modify_status']
        if 'procurement_order_id' in response:
            self.procurement_order_id = response['procurement_order_id']
