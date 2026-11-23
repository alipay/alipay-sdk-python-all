#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalRegisterPaymentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterPaymentQueryResponse, self).__init__()
        self._pay_status = None
        self._pay_time = None

    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterPaymentQueryResponse, self).parse_response_content(response_content)
        if 'pay_status' in response:
            self.pay_status = response['pay_status']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
