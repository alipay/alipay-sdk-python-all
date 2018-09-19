#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiTradeTicketTicketcodeSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeTicketTicketcodeSyncResponse, self).__init__()
        self._biz_code = None
        self._order_no = None
        self._request_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        if isinstance(value, list):
            self._request_id = list()
            for i in value:
                self._request_id.append(i)

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeTicketTicketcodeSyncResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'request_id' in response:
            self.request_id = response['request_id']
