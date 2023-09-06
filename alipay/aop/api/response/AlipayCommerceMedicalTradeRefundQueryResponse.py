#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalTradeRefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalTradeRefundQueryResponse, self).__init__()
        self._alipay_trade_no = None
        self._bank_id = None
        self._bank_name = None
        self._bank_order_id = None
        self._order_type = None
        self._out_trade_no = None
        self._refund_amount = None
        self._refund_msg = None
        self._refund_request_no = None
        self._refund_status = None
        self._refund_time = None
        self._trade_no = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def bank_id(self):
        return self._bank_id

    @bank_id.setter
    def bank_id(self, value):
        self._bank_id = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def bank_order_id(self):
        return self._bank_order_id

    @bank_order_id.setter
    def bank_order_id(self, value):
        self._bank_order_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_msg(self):
        return self._refund_msg

    @refund_msg.setter
    def refund_msg(self, value):
        self._refund_msg = value
    @property
    def refund_request_no(self):
        return self._refund_request_no

    @refund_request_no.setter
    def refund_request_no(self, value):
        self._refund_request_no = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalTradeRefundQueryResponse, self).parse_response_content(response_content)
        if 'alipay_trade_no' in response:
            self.alipay_trade_no = response['alipay_trade_no']
        if 'bank_id' in response:
            self.bank_id = response['bank_id']
        if 'bank_name' in response:
            self.bank_name = response['bank_name']
        if 'bank_order_id' in response:
            self.bank_order_id = response['bank_order_id']
        if 'order_type' in response:
            self.order_type = response['order_type']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_msg' in response:
            self.refund_msg = response['refund_msg']
        if 'refund_request_no' in response:
            self.refund_request_no = response['refund_request_no']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
        if 'refund_time' in response:
            self.refund_time = response['refund_time']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
