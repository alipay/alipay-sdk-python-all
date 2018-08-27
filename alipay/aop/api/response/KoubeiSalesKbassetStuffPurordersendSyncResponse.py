#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccessPurchaseOrderSendResult import AccessPurchaseOrderSendResult


class KoubeiSalesKbassetStuffPurordersendSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiSalesKbassetStuffPurordersendSyncResponse, self).__init__()
        self._purchase_order_send_results = None

    @property
    def purchase_order_send_results(self):
        return self._purchase_order_send_results

    @purchase_order_send_results.setter
    def purchase_order_send_results(self, value):
        if isinstance(value, list):
            self._purchase_order_send_results = list()
            for i in value:
                if isinstance(i, AccessPurchaseOrderSendResult):
                    self._purchase_order_send_results.append(i)
                else:
                    self._purchase_order_send_results.append(AccessPurchaseOrderSendResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiSalesKbassetStuffPurordersendSyncResponse, self).parse_response_content(response_content)
        if 'purchase_order_send_results' in response:
            self.purchase_order_send_results = response['purchase_order_send_results']
