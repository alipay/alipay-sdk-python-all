#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoEduKtSettleinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoEduKtSettleinfoQueryResponse, self).__init__()
        self._account_type = None
        self._bank_account_name = None
        self._bank_account_no = None
        self._bank_name = None
        self._dishonoured_time = None
        self._fail_code = None
        self._fail_desc = None
        self._settle_amount = None
        self._settle_currency = None
        self._settle_id = None
        self._settle_period_begin_time = None
        self._settle_period_end_time = None
        self._settle_time = None
        self._status = None

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def bank_account_name(self):
        return self._bank_account_name

    @bank_account_name.setter
    def bank_account_name(self, value):
        self._bank_account_name = value
    @property
    def bank_account_no(self):
        return self._bank_account_no

    @bank_account_no.setter
    def bank_account_no(self, value):
        self._bank_account_no = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def dishonoured_time(self):
        return self._dishonoured_time

    @dishonoured_time.setter
    def dishonoured_time(self, value):
        self._dishonoured_time = value
    @property
    def fail_code(self):
        return self._fail_code

    @fail_code.setter
    def fail_code(self, value):
        self._fail_code = value
    @property
    def fail_desc(self):
        return self._fail_desc

    @fail_desc.setter
    def fail_desc(self, value):
        self._fail_desc = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def settle_currency(self):
        return self._settle_currency

    @settle_currency.setter
    def settle_currency(self, value):
        self._settle_currency = value
    @property
    def settle_id(self):
        return self._settle_id

    @settle_id.setter
    def settle_id(self, value):
        self._settle_id = value
    @property
    def settle_period_begin_time(self):
        return self._settle_period_begin_time

    @settle_period_begin_time.setter
    def settle_period_begin_time(self, value):
        self._settle_period_begin_time = value
    @property
    def settle_period_end_time(self):
        return self._settle_period_end_time

    @settle_period_end_time.setter
    def settle_period_end_time(self, value):
        self._settle_period_end_time = value
    @property
    def settle_time(self):
        return self._settle_time

    @settle_time.setter
    def settle_time(self, value):
        self._settle_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoEduKtSettleinfoQueryResponse, self).parse_response_content(response_content)
        if 'account_type' in response:
            self.account_type = response['account_type']
        if 'bank_account_name' in response:
            self.bank_account_name = response['bank_account_name']
        if 'bank_account_no' in response:
            self.bank_account_no = response['bank_account_no']
        if 'bank_name' in response:
            self.bank_name = response['bank_name']
        if 'dishonoured_time' in response:
            self.dishonoured_time = response['dishonoured_time']
        if 'fail_code' in response:
            self.fail_code = response['fail_code']
        if 'fail_desc' in response:
            self.fail_desc = response['fail_desc']
        if 'settle_amount' in response:
            self.settle_amount = response['settle_amount']
        if 'settle_currency' in response:
            self.settle_currency = response['settle_currency']
        if 'settle_id' in response:
            self.settle_id = response['settle_id']
        if 'settle_period_begin_time' in response:
            self.settle_period_begin_time = response['settle_period_begin_time']
        if 'settle_period_end_time' in response:
            self.settle_period_end_time = response['settle_period_end_time']
        if 'settle_time' in response:
            self.settle_time = response['settle_time']
        if 'status' in response:
            self.status = response['status']
