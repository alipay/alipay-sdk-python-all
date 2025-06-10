#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcOrderSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcOrderSyncResponse, self).__init__()
        self._order_sync_id = None

    @property
    def order_sync_id(self):
        return self._order_sync_id

    @order_sync_id.setter
    def order_sync_id(self, value):
        self._order_sync_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcOrderSyncResponse, self).parse_response_content(response_content)
        if 'order_sync_id' in response:
            self.order_sync_id = response['order_sync_id']
