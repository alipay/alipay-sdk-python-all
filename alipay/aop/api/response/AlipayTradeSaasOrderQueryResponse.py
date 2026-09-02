#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSaasOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasOrderQueryResponse, self).__init__()
        self._buyer_bank_account = None
        self._buyer_bank_name = None
        self._buyer_name = None
        self._buyer_pay_amount = None
        self._close_reason = None
        self._memo = None
        self._order_no = None
        self._out_trade_no = None
        self._passback_params = None
        self._pay_channel = None
        self._receipt_amount = None
        self._send_pay_date = None
        self._subject = None
        self._total_amount = None
        self._trade_no = None
        self._trade_status = None

    @property
    def buyer_bank_account(self):
        return self._buyer_bank_account

    @buyer_bank_account.setter
    def buyer_bank_account(self, value):
        self._buyer_bank_account = value
    @property
    def buyer_bank_name(self):
        return self._buyer_bank_name

    @buyer_bank_name.setter
    def buyer_bank_name(self, value):
        self._buyer_bank_name = value
    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value
    @property
    def buyer_pay_amount(self):
        return self._buyer_pay_amount

    @buyer_pay_amount.setter
    def buyer_pay_amount(self, value):
        self._buyer_pay_amount = value
    @property
    def close_reason(self):
        return self._close_reason

    @close_reason.setter
    def close_reason(self, value):
        self._close_reason = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def passback_params(self):
        return self._passback_params

    @passback_params.setter
    def passback_params(self, value):
        self._passback_params = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def send_pay_date(self):
        return self._send_pay_date

    @send_pay_date.setter
    def send_pay_date(self, value):
        self._send_pay_date = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasOrderQueryResponse, self).parse_response_content(response_content)
        if 'buyer_bank_account' in response:
            self.buyer_bank_account = response['buyer_bank_account']
        if 'buyer_bank_name' in response:
            self.buyer_bank_name = response['buyer_bank_name']
        if 'buyer_name' in response:
            self.buyer_name = response['buyer_name']
        if 'buyer_pay_amount' in response:
            self.buyer_pay_amount = response['buyer_pay_amount']
        if 'close_reason' in response:
            self.close_reason = response['close_reason']
        if 'memo' in response:
            self.memo = response['memo']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'passback_params' in response:
            self.passback_params = response['passback_params']
        if 'pay_channel' in response:
            self.pay_channel = response['pay_channel']
        if 'receipt_amount' in response:
            self.receipt_amount = response['receipt_amount']
        if 'send_pay_date' in response:
            self.send_pay_date = response['send_pay_date']
        if 'subject' in response:
            self.subject = response['subject']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
