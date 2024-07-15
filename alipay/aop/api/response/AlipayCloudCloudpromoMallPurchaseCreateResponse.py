#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoMallPurchaseCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMallPurchaseCreateResponse, self).__init__()
        self._purchase_order_id = None

    @property
    def purchase_order_id(self):
        return self._purchase_order_id

    @purchase_order_id.setter
    def purchase_order_id(self, value):
        self._purchase_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMallPurchaseCreateResponse, self).parse_response_content(response_content)
        if 'purchase_order_id' in response:
            self.purchase_order_id = response['purchase_order_id']
