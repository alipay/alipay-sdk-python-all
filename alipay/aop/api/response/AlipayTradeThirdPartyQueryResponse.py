#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeThirdPartyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeThirdPartyQueryResponse, self).__init__()
        self._gmt_payment = None
        self._out_trade_no = None
        self._partner_id = None
        self._secondary_merchant_no = None
        self._total_amount = None
        self._trade_no = None
        self._trade_status = None

    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def secondary_merchant_no(self):
        return self._secondary_merchant_no

    @secondary_merchant_no.setter
    def secondary_merchant_no(self, value):
        self._secondary_merchant_no = value
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
        response = super(AlipayTradeThirdPartyQueryResponse, self).parse_response_content(response_content)
        if 'gmt_payment' in response:
            self.gmt_payment = response['gmt_payment']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'secondary_merchant_no' in response:
            self.secondary_merchant_no = response['secondary_merchant_no']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
