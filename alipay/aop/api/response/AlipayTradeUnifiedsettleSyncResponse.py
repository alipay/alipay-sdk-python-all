#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeUnifiedsettleSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeUnifiedsettleSyncResponse, self).__init__()
        self._order_sync_id = None
        self._out_request_no = None
        self._out_trade_no = None
        self._status = None

    @property
    def order_sync_id(self):
        return self._order_sync_id

    @order_sync_id.setter
    def order_sync_id(self, value):
        self._order_sync_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeUnifiedsettleSyncResponse, self).parse_response_content(response_content)
        if 'order_sync_id' in response:
            self.order_sync_id = response['order_sync_id']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'status' in response:
            self.status = response['status']
