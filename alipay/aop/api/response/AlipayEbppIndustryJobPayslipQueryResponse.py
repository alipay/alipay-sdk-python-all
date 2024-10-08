#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryJobPayslipQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryJobPayslipQueryResponse, self).__init__()
        self._account_no = None
        self._alipay_login_id = None
        self._open_id = None
        self._user_id = None

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
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryJobPayslipQueryResponse, self).parse_response_content(response_content)
        if 'account_no' in response:
            self.account_no = response['account_no']
        if 'alipay_login_id' in response:
            self.alipay_login_id = response['alipay_login_id']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
