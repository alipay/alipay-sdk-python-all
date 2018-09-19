#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsUserOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsUserOrderQueryResponse, self).__init__()
        self._order_info = None

    @property
    def order_info(self):
        return self._order_info

    @order_info.setter
    def order_info(self, value):
        self._order_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsUserOrderQueryResponse, self).parse_response_content(response_content)
        if 'order_info' in response:
            self.order_info = response['order_info']
