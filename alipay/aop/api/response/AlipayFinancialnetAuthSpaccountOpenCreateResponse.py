#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthSpaccountOpenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthSpaccountOpenCreateResponse, self).__init__()
        self._opened_account = None
        self._opened_account_user_id = None
        self._opened_account_user_open_id = None

    @property
    def opened_account(self):
        return self._opened_account

    @opened_account.setter
    def opened_account(self, value):
        self._opened_account = value
    @property
    def opened_account_user_id(self):
        return self._opened_account_user_id

    @opened_account_user_id.setter
    def opened_account_user_id(self, value):
        self._opened_account_user_id = value
    @property
    def opened_account_user_open_id(self):
        return self._opened_account_user_open_id

    @opened_account_user_open_id.setter
    def opened_account_user_open_id(self, value):
        self._opened_account_user_open_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthSpaccountOpenCreateResponse, self).parse_response_content(response_content)
        if 'opened_account' in response:
            self.opened_account = response['opened_account']
        if 'opened_account_user_id' in response:
            self.opened_account_user_id = response['opened_account_user_id']
        if 'opened_account_user_open_id' in response:
            self.opened_account_user_open_id = response['opened_account_user_open_id']
