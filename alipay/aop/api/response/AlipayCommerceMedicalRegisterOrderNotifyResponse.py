#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalRegisterOrderNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterOrderNotifyResponse, self).__init__()
        self._order_id = None
        self._register_id = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def register_id(self):
        return self._register_id

    @register_id.setter
    def register_id(self, value):
        self._register_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterOrderNotifyResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'register_id' in response:
            self.register_id = response['register_id']
