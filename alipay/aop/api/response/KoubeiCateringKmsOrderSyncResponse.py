#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringKmsOrderSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringKmsOrderSyncResponse, self).__init__()
        self._message = None
        self._order_no = None
        self._out_order_no = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringKmsOrderSyncResponse, self).parse_response_content(response_content)
        if 'message' in response:
            self.message = response['message']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
