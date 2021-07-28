#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExtContext import ExtContext


class HuanxuTradeOrderCloseResponse(AlipayResponse):

    def __init__(self):
        super(HuanxuTradeOrderCloseResponse, self).__init__()
        self._channel = None
        self._ext_context = None
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
    def ext_context(self):
        return self._ext_context

    @ext_context.setter
    def ext_context(self, value):
        if isinstance(value, ExtContext):
            self._ext_context = value
        else:
            self._ext_context = ExtContext.from_alipay_dict(value)
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
        response = super(HuanxuTradeOrderCloseResponse, self).parse_response_content(response_content)
        if 'channel' in response:
            self.channel = response['channel']
        if 'ext_context' in response:
            self.ext_context = response['ext_context']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'pay_request_no' in response:
            self.pay_request_no = response['pay_request_no']
        if 'payment_id' in response:
            self.payment_id = response['payment_id']
