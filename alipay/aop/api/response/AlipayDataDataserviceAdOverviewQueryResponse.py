#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdOverviewQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdOverviewQueryResponse, self).__init__()
        self._account_amount_total = None
        self._format_available_amount_total = None
        self._format_credit_amount = None
        self._format_not_available_amount_total = None
        self._format_principal_amount = None
        self._format_red_envelope_amount = None

    @property
    def account_amount_total(self):
        return self._account_amount_total

    @account_amount_total.setter
    def account_amount_total(self, value):
        self._account_amount_total = value
    @property
    def format_available_amount_total(self):
        return self._format_available_amount_total

    @format_available_amount_total.setter
    def format_available_amount_total(self, value):
        self._format_available_amount_total = value
    @property
    def format_credit_amount(self):
        return self._format_credit_amount

    @format_credit_amount.setter
    def format_credit_amount(self, value):
        self._format_credit_amount = value
    @property
    def format_not_available_amount_total(self):
        return self._format_not_available_amount_total

    @format_not_available_amount_total.setter
    def format_not_available_amount_total(self, value):
        self._format_not_available_amount_total = value
    @property
    def format_principal_amount(self):
        return self._format_principal_amount

    @format_principal_amount.setter
    def format_principal_amount(self, value):
        self._format_principal_amount = value
    @property
    def format_red_envelope_amount(self):
        return self._format_red_envelope_amount

    @format_red_envelope_amount.setter
    def format_red_envelope_amount(self, value):
        self._format_red_envelope_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdOverviewQueryResponse, self).parse_response_content(response_content)
        if 'account_amount_total' in response:
            self.account_amount_total = response['account_amount_total']
        if 'format_available_amount_total' in response:
            self.format_available_amount_total = response['format_available_amount_total']
        if 'format_credit_amount' in response:
            self.format_credit_amount = response['format_credit_amount']
        if 'format_not_available_amount_total' in response:
            self.format_not_available_amount_total = response['format_not_available_amount_total']
        if 'format_principal_amount' in response:
            self.format_principal_amount = response['format_principal_amount']
        if 'format_red_envelope_amount' in response:
            self.format_red_envelope_amount = response['format_red_envelope_amount']
