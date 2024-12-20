#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanSideloanrepayBudgetQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanSideloanrepayBudgetQueryResponse, self).__init__()
        self._calculate_repay_interest = None
        self._calculate_repay_penalty = None
        self._calculate_repay_principal = None
        self._calculate_repay_total_amount = None
        self._extension = None
        self._return_code = None
        self._return_sub_code = None
        self._return_sub_message = None

    @property
    def calculate_repay_interest(self):
        return self._calculate_repay_interest

    @calculate_repay_interest.setter
    def calculate_repay_interest(self, value):
        self._calculate_repay_interest = value
    @property
    def calculate_repay_penalty(self):
        return self._calculate_repay_penalty

    @calculate_repay_penalty.setter
    def calculate_repay_penalty(self, value):
        self._calculate_repay_penalty = value
    @property
    def calculate_repay_principal(self):
        return self._calculate_repay_principal

    @calculate_repay_principal.setter
    def calculate_repay_principal(self, value):
        self._calculate_repay_principal = value
    @property
    def calculate_repay_total_amount(self):
        return self._calculate_repay_total_amount

    @calculate_repay_total_amount.setter
    def calculate_repay_total_amount(self, value):
        self._calculate_repay_total_amount = value
    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        self._extension = value
    @property
    def return_code(self):
        return self._return_code

    @return_code.setter
    def return_code(self, value):
        self._return_code = value
    @property
    def return_sub_code(self):
        return self._return_sub_code

    @return_sub_code.setter
    def return_sub_code(self, value):
        self._return_sub_code = value
    @property
    def return_sub_message(self):
        return self._return_sub_message

    @return_sub_message.setter
    def return_sub_message(self, value):
        self._return_sub_message = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanSideloanrepayBudgetQueryResponse, self).parse_response_content(response_content)
        if 'calculate_repay_interest' in response:
            self.calculate_repay_interest = response['calculate_repay_interest']
        if 'calculate_repay_penalty' in response:
            self.calculate_repay_penalty = response['calculate_repay_penalty']
        if 'calculate_repay_principal' in response:
            self.calculate_repay_principal = response['calculate_repay_principal']
        if 'calculate_repay_total_amount' in response:
            self.calculate_repay_total_amount = response['calculate_repay_total_amount']
        if 'extension' in response:
            self.extension = response['extension']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_sub_code' in response:
            self.return_sub_code = response['return_sub_code']
        if 'return_sub_message' in response:
            self.return_sub_message = response['return_sub_message']
