#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandTradeorderEventSendResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandTradeorderEventSendResponse, self).__init__()
        self._logistics_status = None
        self._order_status = None

    @property
    def logistics_status(self):
        return self._logistics_status

    @logistics_status.setter
    def logistics_status(self, value):
        self._logistics_status = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandTradeorderEventSendResponse, self).parse_response_content(response_content)
        if 'logistics_status' in response:
            self.logistics_status = response['logistics_status']
        if 'order_status' in response:
            self.order_status = response['order_status']
