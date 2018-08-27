#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserUnicomOrderInfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserUnicomOrderInfoSyncResponse, self).__init__()
        self._order_no = None
        self._order_sync_result = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_sync_result(self):
        return self._order_sync_result

    @order_sync_result.setter
    def order_sync_result(self, value):
        self._order_sync_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserUnicomOrderInfoSyncResponse, self).parse_response_content(response_content)
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_sync_result' in response:
            self.order_sync_result = response['order_sync_result']
