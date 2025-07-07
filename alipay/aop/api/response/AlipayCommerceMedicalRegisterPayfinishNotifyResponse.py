#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalRegisterPayfinishNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterPayfinishNotifyResponse, self).__init__()
        self._order_pay_status = None

    @property
    def order_pay_status(self):
        return self._order_pay_status

    @order_pay_status.setter
    def order_pay_status(self, value):
        self._order_pay_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterPayfinishNotifyResponse, self).parse_response_content(response_content)
        if 'order_pay_status' in response:
            self.order_pay_status = response['order_pay_status']
