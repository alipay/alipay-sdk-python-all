#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantOrderRentCreateResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantOrderRentCreateResponse, self).__init__()
        self._admit_state = None
        self._invoke_state = None
        self._order_no = None
        self._out_order_no = None
        self._user_id = None

    @property
    def admit_state(self):
        return self._admit_state

    @admit_state.setter
    def admit_state(self, value):
        self._admit_state = value
    @property
    def invoke_state(self):
        return self._invoke_state

    @invoke_state.setter
    def invoke_state(self, value):
        self._invoke_state = value
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
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantOrderRentCreateResponse, self).parse_response_content(response_content)
        if 'admit_state' in response:
            self.admit_state = response['admit_state']
        if 'invoke_state' in response:
            self.invoke_state = response['invoke_state']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'user_id' in response:
            self.user_id = response['user_id']
