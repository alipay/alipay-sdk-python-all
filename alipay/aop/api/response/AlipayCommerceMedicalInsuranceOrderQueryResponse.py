#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInsuranceOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceOrderQueryResponse, self).__init__()
        self._open_id = None
        self._order_status = None
        self._out_hospital_id = None
        self._out_hospital_name = None
        self._out_trade_no = None
        self._pay_amount = None
        self._pay_time = None
        self._total_amount = None
        self._trade_no = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_hospital_id(self):
        return self._out_hospital_id

    @out_hospital_id.setter
    def out_hospital_id(self, value):
        self._out_hospital_id = value
    @property
    def out_hospital_name(self):
        return self._out_hospital_name

    @out_hospital_name.setter
    def out_hospital_name(self, value):
        self._out_hospital_name = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceOrderQueryResponse, self).parse_response_content(response_content)
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'out_hospital_id' in response:
            self.out_hospital_id = response['out_hospital_id']
        if 'out_hospital_name' in response:
            self.out_hospital_name = response['out_hospital_name']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'user_id' in response:
            self.user_id = response['user_id']
