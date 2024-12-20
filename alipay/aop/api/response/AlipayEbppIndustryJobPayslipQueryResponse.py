#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryJobPayslipQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryJobPayslipQueryResponse, self).__init__()
        self._account_no = None
        self._alipay_login_id = None
        self._cert_num = None
        self._open_id = None
        self._out_biz_no = None
        self._phone = None
        self._user_id = None
        self._user_name = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def alipay_login_id(self):
        return self._alipay_login_id

    @alipay_login_id.setter
    def alipay_login_id(self, value):
        self._alipay_login_id = value
    @property
    def cert_num(self):
        return self._cert_num

    @cert_num.setter
    def cert_num(self, value):
        self._cert_num = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryJobPayslipQueryResponse, self).parse_response_content(response_content)
        if 'account_no' in response:
            self.account_no = response['account_no']
        if 'alipay_login_id' in response:
            self.alipay_login_id = response['alipay_login_id']
        if 'cert_num' in response:
            self.cert_num = response['cert_num']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'phone' in response:
            self.phone = response['phone']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_name' in response:
            self.user_name = response['user_name']
