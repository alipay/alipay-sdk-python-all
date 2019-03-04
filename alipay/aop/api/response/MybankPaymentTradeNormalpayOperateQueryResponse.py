#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeNormalpayOperateQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeNormalpayOperateQueryResponse, self).__init__()
        self._amount = None
        self._biz_no = None
        self._currency_value = None
        self._ext_info = None
        self._operate_no = None
        self._operate_state = None
        self._operate_type = None
        self._order_no = None
        self._real_amount = None
        self._request_accept_time = None
        self._request_no = None
        self._trans_time = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
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
    def operate_no(self):
        return self._operate_no

    @operate_no.setter
    def operate_no(self, value):
        self._operate_no = value
    @property
    def operate_state(self):
        return self._operate_state

    @operate_state.setter
    def operate_state(self, value):
        self._operate_state = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
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
    @property
    def trans_time(self):
        return self._trans_time

    @trans_time.setter
    def trans_time(self, value):
        self._trans_time = value

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeNormalpayOperateQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'currency_value' in response:
            self.currency_value = response['currency_value']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'operate_no' in response:
            self.operate_no = response['operate_no']
        if 'operate_state' in response:
            self.operate_state = response['operate_state']
        if 'operate_type' in response:
            self.operate_type = response['operate_type']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'real_amount' in response:
            self.real_amount = response['real_amount']
        if 'request_accept_time' in response:
            self.request_accept_time = response['request_accept_time']
        if 'request_no' in response:
            self.request_no = response['request_no']
        if 'trans_time' in response:
            self.trans_time = response['trans_time']
