#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PayInfoResponse import PayInfoResponse


class AlipayOpenMiniOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniOrderCreateResponse, self).__init__()
        self._customer_display_text = None
        self._order_id = None
        self._out_order_id = None
        self._pay_info_response = None

    @property
    def customer_display_text(self):
        return self._customer_display_text

    @customer_display_text.setter
    def customer_display_text(self, value):
        self._customer_display_text = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def pay_info_response(self):
        return self._pay_info_response

    @pay_info_response.setter
    def pay_info_response(self, value):
        if isinstance(value, PayInfoResponse):
            self._pay_info_response = value
        else:
            self._pay_info_response = PayInfoResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniOrderCreateResponse, self).parse_response_content(response_content)
        if 'customer_display_text' in response:
            self.customer_display_text = response['customer_display_text']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'pay_info_response' in response:
            self.pay_info_response = response['pay_info_response']
