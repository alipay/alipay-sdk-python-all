#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeNormalpayOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeNormalpayOrderQueryResponse, self).__init__()
        self._amount = None
        self._biz_channel = None
        self._biz_no = None
        self._currency_value = None
        self._ext_info = None
        self._order_type = None
        self._pay_amount = None
        self._paying_amount = None
        self._receipt_amount = None
        self._receipting_amount = None
        self._request_accept_time = None
        self._request_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_channel(self):
        return self._biz_channel

    @biz_channel.setter
    def biz_channel(self, value):
        self._biz_channel = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def currency_value(self):
        return self._currency_value

    @currency_value.setter
    def currency_value(self, value):
        self._currency_value = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def paying_amount(self):
        return self._paying_amount

    @paying_amount.setter
    def paying_amount(self, value):
        self._paying_amount = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def receipting_amount(self):
        return self._receipting_amount

    @receipting_amount.setter
    def receipting_amount(self, value):
        self._receipting_amount = value
    @property
    def request_accept_time(self):
        return self._request_accept_time

    @request_accept_time.setter
    def request_accept_time(self, value):
        self._request_accept_time = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeNormalpayOrderQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'biz_channel' in response:
            self.biz_channel = response['biz_channel']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'currency_value' in response:
            self.currency_value = response['currency_value']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'order_type' in response:
            self.order_type = response['order_type']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'paying_amount' in response:
            self.paying_amount = response['paying_amount']
        if 'receipt_amount' in response:
            self.receipt_amount = response['receipt_amount']
        if 'receipting_amount' in response:
            self.receipting_amount = response['receipting_amount']
        if 'request_accept_time' in response:
            self.request_accept_time = response['request_accept_time']
        if 'request_no' in response:
            self.request_no = response['request_no']
