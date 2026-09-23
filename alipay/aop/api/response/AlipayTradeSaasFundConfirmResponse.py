#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSaasFundConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasFundConfirmResponse, self).__init__()
        self._auto_refund_amount = None
        self._buyer_pay_amount = None
        self._claim_amount = None
        self._claim_request_no = None
        self._fund_no = None
        self._order_no = None
        self._out_trade_no = None
        self._trade_no = None
        self._trade_status = None

    @property
    def auto_refund_amount(self):
        return self._auto_refund_amount

    @auto_refund_amount.setter
    def auto_refund_amount(self, value):
        self._auto_refund_amount = value
    @property
    def buyer_pay_amount(self):
        return self._buyer_pay_amount

    @buyer_pay_amount.setter
    def buyer_pay_amount(self, value):
        self._buyer_pay_amount = value
    @property
    def claim_amount(self):
        return self._claim_amount

    @claim_amount.setter
    def claim_amount(self, value):
        self._claim_amount = value
    @property
    def claim_request_no(self):
        return self._claim_request_no

    @claim_request_no.setter
    def claim_request_no(self, value):
        self._claim_request_no = value
    @property
    def fund_no(self):
        return self._fund_no

    @fund_no.setter
    def fund_no(self, value):
        self._fund_no = value
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
        response = super(AlipayTradeSaasFundConfirmResponse, self).parse_response_content(response_content)
        if 'auto_refund_amount' in response:
            self.auto_refund_amount = response['auto_refund_amount']
        if 'buyer_pay_amount' in response:
            self.buyer_pay_amount = response['buyer_pay_amount']
        if 'claim_amount' in response:
            self.claim_amount = response['claim_amount']
        if 'claim_request_no' in response:
            self.claim_request_no = response['claim_request_no']
        if 'fund_no' in response:
            self.fund_no = response['fund_no']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
