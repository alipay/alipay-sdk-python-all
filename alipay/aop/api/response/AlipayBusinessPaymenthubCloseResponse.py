#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBusinessPaymenthubCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessPaymenthubCloseResponse, self).__init__()
        self._channel = None
        self._pay_amount = None
        self._pay_request_no = None
        self._payment_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_request_no(self):
        return self._pay_request_no

    @pay_request_no.setter
    def pay_request_no(self, value):
        self._pay_request_no = value
    @property
    def payment_id(self):
        return self._payment_id

    @payment_id.setter
    def payment_id(self, value):
        self._payment_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessPaymenthubCloseResponse, self).parse_response_content(response_content)
        if 'channel' in response:
            self.channel = response['channel']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'pay_request_no' in response:
            self.pay_request_no = response['pay_request_no']
        if 'payment_id' in response:
            self.payment_id = response['payment_id']
