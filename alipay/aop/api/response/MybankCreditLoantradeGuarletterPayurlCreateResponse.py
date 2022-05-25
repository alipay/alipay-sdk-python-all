#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO


class MybankCreditLoantradeGuarletterPayurlCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeGuarletterPayurlCreateResponse, self).__init__()
        self._accept_result = None
        self._fee_amt = None
        self._fee_charge_url = None
        self._reject_reason = None

    @property
    def accept_result(self):
        return self._accept_result

    @accept_result.setter
    def accept_result(self, value):
        self._accept_result = value
    @property
    def fee_amt(self):
        return self._fee_amt

    @fee_amt.setter
    def fee_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._fee_amt = value
        else:
            self._fee_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def fee_charge_url(self):
        return self._fee_charge_url

    @fee_charge_url.setter
    def fee_charge_url(self, value):
        self._fee_charge_url = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeGuarletterPayurlCreateResponse, self).parse_response_content(response_content)
        if 'accept_result' in response:
            self.accept_result = response['accept_result']
        if 'fee_amt' in response:
            self.fee_amt = response['fee_amt']
        if 'fee_charge_url' in response:
            self.fee_charge_url = response['fee_charge_url']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
