#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainCloudfundSubaccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainCloudfundSubaccountQueryResponse, self).__init__()
        self._account_ext_no = None
        self._account_status = None
        self._available_balance = None
        self._cert_name = None
        self._ip_role_id = None

    @property
    def account_ext_no(self):
        return self._account_ext_no

    @account_ext_no.setter
    def account_ext_no(self, value):
        self._account_ext_no = value
    @property
    def account_status(self):
        return self._account_status

    @account_status.setter
    def account_status(self, value):
        self._account_status = value
    @property
    def available_balance(self):
        return self._available_balance

    @available_balance.setter
    def available_balance(self, value):
        self._available_balance = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainCloudfundSubaccountQueryResponse, self).parse_response_content(response_content)
        if 'account_ext_no' in response:
            self.account_ext_no = response['account_ext_no']
        if 'account_status' in response:
            self.account_status = response['account_status']
        if 'available_balance' in response:
            self.available_balance = response['available_balance']
        if 'cert_name' in response:
            self.cert_name = response['cert_name']
        if 'ip_role_id' in response:
            self.ip_role_id = response['ip_role_id']
