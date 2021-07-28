#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainPoolCreditsignadmitQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainPoolCreditsignadmitQueryResponse, self).__init__()
        self._admit = None
        self._amt_ccy = None
        self._credit_lmt_amt = None
        self._factoring_sign_status = None
        self._loan_balance_amt = None
        self._loanable_amt = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def amt_ccy(self):
        return self._amt_ccy

    @amt_ccy.setter
    def amt_ccy(self, value):
        self._amt_ccy = value
    @property
    def credit_lmt_amt(self):
        return self._credit_lmt_amt

    @credit_lmt_amt.setter
    def credit_lmt_amt(self, value):
        self._credit_lmt_amt = value
    @property
    def factoring_sign_status(self):
        return self._factoring_sign_status

    @factoring_sign_status.setter
    def factoring_sign_status(self, value):
        self._factoring_sign_status = value
    @property
    def loan_balance_amt(self):
        return self._loan_balance_amt

    @loan_balance_amt.setter
    def loan_balance_amt(self, value):
        self._loan_balance_amt = value
    @property
    def loanable_amt(self):
        return self._loanable_amt

    @loanable_amt.setter
    def loanable_amt(self, value):
        self._loanable_amt = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainPoolCreditsignadmitQueryResponse, self).parse_response_content(response_content)
        if 'admit' in response:
            self.admit = response['admit']
        if 'amt_ccy' in response:
            self.amt_ccy = response['amt_ccy']
        if 'credit_lmt_amt' in response:
            self.credit_lmt_amt = response['credit_lmt_amt']
        if 'factoring_sign_status' in response:
            self.factoring_sign_status = response['factoring_sign_status']
        if 'loan_balance_amt' in response:
            self.loan_balance_amt = response['loan_balance_amt']
        if 'loanable_amt' in response:
            self.loanable_amt = response['loanable_amt']
