#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiAffinitycardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiAffinitycardQueryResponse, self).__init__()
        self._available_amount = None
        self._close_reason = None
        self._close_type = None
        self._opened = None
        self._repay_date = None
        self._total_amount = None
        self._user_prod_account_no = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def close_reason(self):
        return self._close_reason

    @close_reason.setter
    def close_reason(self, value):
        self._close_reason = value
    @property
    def close_type(self):
        return self._close_type

    @close_type.setter
    def close_type(self, value):
        self._close_type = value
    @property
    def opened(self):
        return self._opened

    @opened.setter
    def opened(self, value):
        self._opened = value
    @property
    def repay_date(self):
        return self._repay_date

    @repay_date.setter
    def repay_date(self, value):
        self._repay_date = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def user_prod_account_no(self):
        return self._user_prod_account_no

    @user_prod_account_no.setter
    def user_prod_account_no(self, value):
        self._user_prod_account_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiAffinitycardQueryResponse, self).parse_response_content(response_content)
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'close_reason' in response:
            self.close_reason = response['close_reason']
        if 'close_type' in response:
            self.close_type = response['close_type']
        if 'opened' in response:
            self.opened = response['opened']
        if 'repay_date' in response:
            self.repay_date = response['repay_date']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'user_prod_account_no' in response:
            self.user_prod_account_no = response['user_prod_account_no']
