#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalDirectTradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalDirectTradeQueryResponse, self).__init__()
        self._alipay_trade_no = None
        self._ch_info = None
        self._gmt_out_create = None
        self._gmt_own_paid = None
        self._order_type = None
        self._out_trade_no = None
        self._own_error_reason = None
        self._own_pay_status = None
        self._real_amount = None
        self._total_amount = None
        self._trade_no = None
        self._trade_status = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def ch_info(self):
        return self._ch_info

    @ch_info.setter
    def ch_info(self, value):
        self._ch_info = value
    @property
    def gmt_out_create(self):
        return self._gmt_out_create

    @gmt_out_create.setter
    def gmt_out_create(self, value):
        self._gmt_out_create = value
    @property
    def gmt_own_paid(self):
        return self._gmt_own_paid

    @gmt_own_paid.setter
    def gmt_own_paid(self, value):
        self._gmt_own_paid = value
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
    def own_error_reason(self):
        return self._own_error_reason

    @own_error_reason.setter
    def own_error_reason(self, value):
        self._own_error_reason = value
    @property
    def own_pay_status(self):
        return self._own_pay_status

    @own_pay_status.setter
    def own_pay_status(self, value):
        self._own_pay_status = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
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
        response = super(AlipayCommerceMedicalDirectTradeQueryResponse, self).parse_response_content(response_content)
        if 'alipay_trade_no' in response:
            self.alipay_trade_no = response['alipay_trade_no']
        if 'ch_info' in response:
            self.ch_info = response['ch_info']
        if 'gmt_out_create' in response:
            self.gmt_out_create = response['gmt_out_create']
        if 'gmt_own_paid' in response:
            self.gmt_own_paid = response['gmt_own_paid']
        if 'order_type' in response:
            self.order_type = response['order_type']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'own_error_reason' in response:
            self.own_error_reason = response['own_error_reason']
        if 'own_pay_status' in response:
            self.own_pay_status = response['own_pay_status']
        if 'real_amount' in response:
            self.real_amount = response['real_amount']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
