#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcCreditBillGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcCreditBillGetResponse, self).__init__()
        self._cp_numbers = None
        self._cp_payable_interest = None
        self._cp_payable_penalty = None
        self._cp_payable_principal = None
        self._cp_unpaid_interest = None
        self._cp_unpaid_penalty = None
        self._cp_unpaid_principal = None
        self._enterprise_id = None
        self._overdue = None
        self._payment_status = None
        self._repayment_date = None

    @property
    def cp_numbers(self):
        return self._cp_numbers

    @cp_numbers.setter
    def cp_numbers(self, value):
        self._cp_numbers = value
    @property
    def cp_payable_interest(self):
        return self._cp_payable_interest

    @cp_payable_interest.setter
    def cp_payable_interest(self, value):
        self._cp_payable_interest = value
    @property
    def cp_payable_penalty(self):
        return self._cp_payable_penalty

    @cp_payable_penalty.setter
    def cp_payable_penalty(self, value):
        self._cp_payable_penalty = value
    @property
    def cp_payable_principal(self):
        return self._cp_payable_principal

    @cp_payable_principal.setter
    def cp_payable_principal(self, value):
        self._cp_payable_principal = value
    @property
    def cp_unpaid_interest(self):
        return self._cp_unpaid_interest

    @cp_unpaid_interest.setter
    def cp_unpaid_interest(self, value):
        self._cp_unpaid_interest = value
    @property
    def cp_unpaid_penalty(self):
        return self._cp_unpaid_penalty

    @cp_unpaid_penalty.setter
    def cp_unpaid_penalty(self, value):
        self._cp_unpaid_penalty = value
    @property
    def cp_unpaid_principal(self):
        return self._cp_unpaid_principal

    @cp_unpaid_principal.setter
    def cp_unpaid_principal(self, value):
        self._cp_unpaid_principal = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def overdue(self):
        return self._overdue

    @overdue.setter
    def overdue(self, value):
        self._overdue = value
    @property
    def payment_status(self):
        return self._payment_status

    @payment_status.setter
    def payment_status(self, value):
        self._payment_status = value
    @property
    def repayment_date(self):
        return self._repayment_date

    @repayment_date.setter
    def repayment_date(self, value):
        self._repayment_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcCreditBillGetResponse, self).parse_response_content(response_content)
        if 'cp_numbers' in response:
            self.cp_numbers = response['cp_numbers']
        if 'cp_payable_interest' in response:
            self.cp_payable_interest = response['cp_payable_interest']
        if 'cp_payable_penalty' in response:
            self.cp_payable_penalty = response['cp_payable_penalty']
        if 'cp_payable_principal' in response:
            self.cp_payable_principal = response['cp_payable_principal']
        if 'cp_unpaid_interest' in response:
            self.cp_unpaid_interest = response['cp_unpaid_interest']
        if 'cp_unpaid_penalty' in response:
            self.cp_unpaid_penalty = response['cp_unpaid_penalty']
        if 'cp_unpaid_principal' in response:
            self.cp_unpaid_principal = response['cp_unpaid_principal']
        if 'enterprise_id' in response:
            self.enterprise_id = response['enterprise_id']
        if 'overdue' in response:
            self.overdue = response['overdue']
        if 'payment_status' in response:
            self.payment_status = response['payment_status']
        if 'repayment_date' in response:
            self.repayment_date = response['repayment_date']
