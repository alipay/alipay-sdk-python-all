#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainDefinInsuranceApplyCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinInsuranceApplyCreateResponse, self).__init__()
        self._amount = None
        self._apply_no = None
        self._insure_end_date = None
        self._insure_start_date = None
        self._parm = None
        self._policy_no = None
        self._policy_url = None
        self._premium = None
        self._trade_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def insure_end_date(self):
        return self._insure_end_date

    @insure_end_date.setter
    def insure_end_date(self, value):
        self._insure_end_date = value
    @property
    def insure_start_date(self):
        return self._insure_start_date

    @insure_start_date.setter
    def insure_start_date(self, value):
        self._insure_start_date = value
    @property
    def parm(self):
        return self._parm

    @parm.setter
    def parm(self, value):
        self._parm = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def policy_url(self):
        return self._policy_url

    @policy_url.setter
    def policy_url(self, value):
        self._policy_url = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinInsuranceApplyCreateResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'apply_no' in response:
            self.apply_no = response['apply_no']
        if 'insure_end_date' in response:
            self.insure_end_date = response['insure_end_date']
        if 'insure_start_date' in response:
            self.insure_start_date = response['insure_start_date']
        if 'parm' in response:
            self.parm = response['parm']
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
        if 'policy_url' in response:
            self.policy_url = response['policy_url']
        if 'premium' in response:
            self.premium = response['premium']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
