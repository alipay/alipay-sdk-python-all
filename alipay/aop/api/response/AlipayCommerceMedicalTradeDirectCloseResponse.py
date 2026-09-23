#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalTradeDirectCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalTradeDirectCloseResponse, self).__init__()
        self._alipay_trade_no = None
        self._out_trade_no = None
        self._own_pay_cancel_msg = None
        self._own_pay_cancel_result = None
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
    def own_pay_cancel_msg(self):
        return self._own_pay_cancel_msg

    @own_pay_cancel_msg.setter
    def own_pay_cancel_msg(self, value):
        self._own_pay_cancel_msg = value
    @property
    def own_pay_cancel_result(self):
        return self._own_pay_cancel_result

    @own_pay_cancel_result.setter
    def own_pay_cancel_result(self, value):
        self._own_pay_cancel_result = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalTradeDirectCloseResponse, self).parse_response_content(response_content)
        if 'alipay_trade_no' in response:
            self.alipay_trade_no = response['alipay_trade_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'own_pay_cancel_msg' in response:
            self.own_pay_cancel_msg = response['own_pay_cancel_msg']
        if 'own_pay_cancel_result' in response:
            self.own_pay_cancel_result = response['own_pay_cancel_result']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
