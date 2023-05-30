#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeQrcodePayresultQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeQrcodePayresultQueryResponse, self).__init__()
        self._accept_time = None
        self._biz_no = None
        self._currency = None
        self._error_message = None
        self._finish_time = None
        self._operate_no = None
        self._operate_state = None
        self._operate_type = None
        self._order_no = None
        self._order_type = None
        self._payer_card_name = None
        self._payer_card_no = None
        self._real_trade_amt = None
        self._request_no = None
        self._trade_amt = None

    @property
    def accept_time(self):
        return self._accept_time

    @accept_time.setter
    def accept_time(self, value):
        self._accept_time = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
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
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def payer_card_name(self):
        return self._payer_card_name

    @payer_card_name.setter
    def payer_card_name(self, value):
        self._payer_card_name = value
    @property
    def payer_card_no(self):
        return self._payer_card_no

    @payer_card_no.setter
    def payer_card_no(self, value):
        self._payer_card_no = value
    @property
    def real_trade_amt(self):
        return self._real_trade_amt

    @real_trade_amt.setter
    def real_trade_amt(self, value):
        self._real_trade_amt = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def trade_amt(self):
        return self._trade_amt

    @trade_amt.setter
    def trade_amt(self, value):
        self._trade_amt = value

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeQrcodePayresultQueryResponse, self).parse_response_content(response_content)
        if 'accept_time' in response:
            self.accept_time = response['accept_time']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'currency' in response:
            self.currency = response['currency']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'finish_time' in response:
            self.finish_time = response['finish_time']
        if 'operate_no' in response:
            self.operate_no = response['operate_no']
        if 'operate_state' in response:
            self.operate_state = response['operate_state']
        if 'operate_type' in response:
            self.operate_type = response['operate_type']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_type' in response:
            self.order_type = response['order_type']
        if 'payer_card_name' in response:
            self.payer_card_name = response['payer_card_name']
        if 'payer_card_no' in response:
            self.payer_card_no = response['payer_card_no']
        if 'real_trade_amt' in response:
            self.real_trade_amt = response['real_trade_amt']
        if 'request_no' in response:
            self.request_no = response['request_no']
        if 'trade_amt' in response:
            self.trade_amt = response['trade_amt']
