#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTaxSingleTaxdataSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTaxSingleTaxdataSendResponse, self).__init__()
        self._full_name = None
        self._open_id = None
        self._pay_time = None
        self._refund_order_no = None
        self._user_id = None
        self._user_login_id = None

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def refund_order_no(self):
        return self._refund_order_no

    @refund_order_no.setter
    def refund_order_no(self, value):
        self._refund_order_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_login_id(self):
        return self._user_login_id

    @user_login_id.setter
    def user_login_id(self, value):
        self._user_login_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTaxSingleTaxdataSendResponse, self).parse_response_content(response_content)
        if 'full_name' in response:
            self.full_name = response['full_name']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'refund_order_no' in response:
            self.refund_order_no = response['refund_order_no']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_login_id' in response:
            self.user_login_id = response['user_login_id']
