#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalTradeCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalTradeCancelResponse, self).__init__()
        self._alipay_trade_no = None
        self._bank_id = None
        self._bank_name = None
        self._bank_order_id = None
        self._medical_pay_cancel_msg = None
        self._medical_pay_cancel_result = None
        self._order_type = None
        self._out_trade_no = None
        self._own_pay_cancel_msg = None
        self._own_pay_cancel_result = None
        self._trade_cancel_result = None
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
    def medical_pay_cancel_msg(self):
        return self._medical_pay_cancel_msg

    @medical_pay_cancel_msg.setter
    def medical_pay_cancel_msg(self, value):
        self._medical_pay_cancel_msg = value
    @property
    def medical_pay_cancel_result(self):
        return self._medical_pay_cancel_result

    @medical_pay_cancel_result.setter
    def medical_pay_cancel_result(self, value):
        self._medical_pay_cancel_result = value
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
    def trade_cancel_result(self):
        return self._trade_cancel_result

    @trade_cancel_result.setter
    def trade_cancel_result(self, value):
        self._trade_cancel_result = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalTradeCancelResponse, self).parse_response_content(response_content)
        if 'alipay_trade_no' in response:
            self.alipay_trade_no = response['alipay_trade_no']
        if 'bank_id' in response:
            self.bank_id = response['bank_id']
        if 'bank_name' in response:
            self.bank_name = response['bank_name']
        if 'bank_order_id' in response:
            self.bank_order_id = response['bank_order_id']
        if 'medical_pay_cancel_msg' in response:
            self.medical_pay_cancel_msg = response['medical_pay_cancel_msg']
        if 'medical_pay_cancel_result' in response:
            self.medical_pay_cancel_result = response['medical_pay_cancel_result']
        if 'order_type' in response:
            self.order_type = response['order_type']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'own_pay_cancel_msg' in response:
            self.own_pay_cancel_msg = response['own_pay_cancel_msg']
        if 'own_pay_cancel_result' in response:
            self.own_pay_cancel_result = response['own_pay_cancel_result']
        if 'trade_cancel_result' in response:
            self.trade_cancel_result = response['trade_cancel_result']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
