#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class XingheLendassistCarfinauctionApplystatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(XingheLendassistCarfinauctionApplystatusQueryResponse, self).__init__()
        self._apply_no = None
        self._bank_account_manager_contract_number = None
        self._disburse_time = None
        self._loan_amount = None
        self._out_order_no = None
        self._status = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def bank_account_manager_contract_number(self):
        return self._bank_account_manager_contract_number

    @bank_account_manager_contract_number.setter
    def bank_account_manager_contract_number(self, value):
        self._bank_account_manager_contract_number = value
    @property
    def disburse_time(self):
        return self._disburse_time

    @disburse_time.setter
    def disburse_time(self, value):
        self._disburse_time = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(XingheLendassistCarfinauctionApplystatusQueryResponse, self).parse_response_content(response_content)
        if 'apply_no' in response:
            self.apply_no = response['apply_no']
        if 'bank_account_manager_contract_number' in response:
            self.bank_account_manager_contract_number = response['bank_account_manager_contract_number']
        if 'disburse_time' in response:
            self.disburse_time = response['disburse_time']
        if 'loan_amount' in response:
            self.loan_amount = response['loan_amount']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'status' in response:
            self.status = response['status']
