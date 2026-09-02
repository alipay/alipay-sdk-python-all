#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentProcurementOrderCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentProcurementOrderCancelResponse, self).__init__()
        self._cancel_status = None
        self._procurement_order_id = None

    @property
    def cancel_status(self):
        return self._cancel_status

    @cancel_status.setter
    def cancel_status(self, value):
        self._cancel_status = value
    @property
    def procurement_order_id(self):
        return self._procurement_order_id

    @procurement_order_id.setter
    def procurement_order_id(self, value):
        self._procurement_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentProcurementOrderCancelResponse, self).parse_response_content(response_content)
        if 'cancel_status' in response:
            self.cancel_status = response['cancel_status']
        if 'procurement_order_id' in response:
            self.procurement_order_id = response['procurement_order_id']
