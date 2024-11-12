#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ReferenceBankAccount import ReferenceBankAccount


class AnttechBlockchainFinanceTvpAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceTvpAccountQueryResponse, self).__init__()
        self._account_no = None
        self._agreement_no = None
        self._alipay_logon_id = None
        self._balance_amount = None
        self._reference_bank_account = None
        self._status = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def balance_amount(self):
        return self._balance_amount

    @balance_amount.setter
    def balance_amount(self, value):
        self._balance_amount = value
    @property
    def reference_bank_account(self):
        return self._reference_bank_account

    @reference_bank_account.setter
    def reference_bank_account(self, value):
        if isinstance(value, ReferenceBankAccount):
            self._reference_bank_account = value
        else:
            self._reference_bank_account = ReferenceBankAccount.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceTvpAccountQueryResponse, self).parse_response_content(response_content)
        if 'account_no' in response:
            self.account_no = response['account_no']
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'alipay_logon_id' in response:
            self.alipay_logon_id = response['alipay_logon_id']
        if 'balance_amount' in response:
            self.balance_amount = response['balance_amount']
        if 'reference_bank_account' in response:
            self.reference_bank_account = response['reference_bank_account']
        if 'status' in response:
            self.status = response['status']
