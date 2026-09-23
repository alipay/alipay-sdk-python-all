#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalTradeDirectCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalTradeDirectCreateResponse, self).__init__()
        self._alipay_trade_no = None
        self._out_trade_no = None
        self._pay_url = None
        self._subject = None
        self._trade_no = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_url(self):
        return self._pay_url

    @pay_url.setter
    def pay_url(self, value):
        self._pay_url = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalTradeDirectCreateResponse, self).parse_response_content(response_content)
        if 'alipay_trade_no' in response:
            self.alipay_trade_no = response['alipay_trade_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'pay_url' in response:
            self.pay_url = response['pay_url']
        if 'subject' in response:
            self.subject = response['subject']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
