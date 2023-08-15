#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpAeprepayContractQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpAeprepayContractQueryResponse, self).__init__()
        self._admitted = None
        self._credit_limit_amount = None
        self._credit_limit_currency = None
        self._denied_reason = None
        self._loanable_amount = None
        self._loanable_currency = None
        self._signed = None
        self._unsigned = None
        self._unsigned_date = None

    @property
    def admitted(self):
        return self._admitted

    @admitted.setter
    def admitted(self, value):
        self._admitted = value
    @property
    def credit_limit_amount(self):
        return self._credit_limit_amount

    @credit_limit_amount.setter
    def credit_limit_amount(self, value):
        self._credit_limit_amount = value
    @property
    def credit_limit_currency(self):
        return self._credit_limit_currency

    @credit_limit_currency.setter
    def credit_limit_currency(self, value):
        self._credit_limit_currency = value
    @property
    def denied_reason(self):
        return self._denied_reason

    @denied_reason.setter
    def denied_reason(self, value):
        self._denied_reason = value
    @property
    def loanable_amount(self):
        return self._loanable_amount

    @loanable_amount.setter
    def loanable_amount(self, value):
        self._loanable_amount = value
    @property
    def loanable_currency(self):
        return self._loanable_currency

    @loanable_currency.setter
    def loanable_currency(self, value):
        self._loanable_currency = value
    @property
    def signed(self):
        return self._signed

    @signed.setter
    def signed(self, value):
        self._signed = value
    @property
    def unsigned(self):
        return self._unsigned

    @unsigned.setter
    def unsigned(self, value):
        self._unsigned = value
    @property
    def unsigned_date(self):
        return self._unsigned_date

    @unsigned_date.setter
    def unsigned_date(self, value):
        self._unsigned_date = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpAeprepayContractQueryResponse, self).parse_response_content(response_content)
        if 'admitted' in response:
            self.admitted = response['admitted']
        if 'credit_limit_amount' in response:
            self.credit_limit_amount = response['credit_limit_amount']
        if 'credit_limit_currency' in response:
            self.credit_limit_currency = response['credit_limit_currency']
        if 'denied_reason' in response:
            self.denied_reason = response['denied_reason']
        if 'loanable_amount' in response:
            self.loanable_amount = response['loanable_amount']
        if 'loanable_currency' in response:
            self.loanable_currency = response['loanable_currency']
        if 'signed' in response:
            self.signed = response['signed']
        if 'unsigned' in response:
            self.unsigned = response['unsigned']
        if 'unsigned_date' in response:
            self.unsigned_date = response['unsigned_date']
