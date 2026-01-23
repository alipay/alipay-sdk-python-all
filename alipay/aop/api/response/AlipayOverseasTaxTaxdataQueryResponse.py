#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTaxTaxdataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTaxTaxdataQueryResponse, self).__init__()
        self._final_refund_amount = None
        self._final_refund_currency = None
        self._full_name = None
        self._out_order_no = None
        self._partner_id = None
        self._pay_time = None
        self._phone_no = None
        self._status = None
        self._tax_no = None
        self._user_id = None
        self._user_id_open_id = None
        self._user_login_id = None

    @property
    def final_refund_amount(self):
        return self._final_refund_amount

    @final_refund_amount.setter
    def final_refund_amount(self, value):
        self._final_refund_amount = value
    @property
    def final_refund_currency(self):
        return self._final_refund_currency

    @final_refund_currency.setter
    def final_refund_currency(self, value):
        self._final_refund_currency = value
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_id_open_id(self):
        return self._user_id_open_id

    @user_id_open_id.setter
    def user_id_open_id(self, value):
        self._user_id_open_id = value
    @property
    def user_login_id(self):
        return self._user_login_id

    @user_login_id.setter
    def user_login_id(self, value):
        self._user_login_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTaxTaxdataQueryResponse, self).parse_response_content(response_content)
        if 'final_refund_amount' in response:
            self.final_refund_amount = response['final_refund_amount']
        if 'final_refund_currency' in response:
            self.final_refund_currency = response['final_refund_currency']
        if 'full_name' in response:
            self.full_name = response['full_name']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'phone_no' in response:
            self.phone_no = response['phone_no']
        if 'status' in response:
            self.status = response['status']
        if 'tax_no' in response:
            self.tax_no = response['tax_no']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_id_open_id' in response:
            self.user_id_open_id = response['user_id_open_id']
        if 'user_login_id' in response:
            self.user_login_id = response['user_login_id']
