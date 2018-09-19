#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccessPurchaseOrder import AccessPurchaseOrder


class KoubeiSalesKbassetStuffPurchaseorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiSalesKbassetStuffPurchaseorderQueryResponse, self).__init__()
        self._asset_purchase_orders = None
        self._has_next_page = None

    @property
    def asset_purchase_orders(self):
        return self._asset_purchase_orders

    @asset_purchase_orders.setter
    def asset_purchase_orders(self, value):
        if isinstance(value, list):
            self._asset_purchase_orders = list()
            for i in value:
                if isinstance(i, AccessPurchaseOrder):
                    self._asset_purchase_orders.append(i)
                else:
                    self._asset_purchase_orders.append(AccessPurchaseOrder.from_alipay_dict(i))
    @property
    def has_next_page(self):
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, value):
        self._has_next_page = value

    def parse_response_content(self, response_content):
        response = super(KoubeiSalesKbassetStuffPurchaseorderQueryResponse, self).parse_response_content(response_content)
        if 'asset_purchase_orders' in response:
            self.asset_purchase_orders = response['asset_purchase_orders']
        if 'has_next_page' in response:
            self.has_next_page = response['has_next_page']
