#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO


class MybankCreditLoantradeGuarletterPayurlCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeGuarletterPayurlCreateResponse, self).__init__()
        self._accept_result = None
        self._bank_card_name = None
        self._bank_card_no = None
        self._bank_name = None
        self._bid_no = None
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
    def bank_card_name(self):
        return self._bank_card_name

    @bank_card_name.setter
    def bank_card_name(self, value):
        self._bank_card_name = value
    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def bid_no(self):
        return self._bid_no

    @bid_no.setter
    def bid_no(self, value):
        self._bid_no = value
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
        if 'bank_card_name' in response:
            self.bank_card_name = response['bank_card_name']
        if 'bank_card_no' in response:
            self.bank_card_no = response['bank_card_no']
        if 'bank_name' in response:
            self.bank_name = response['bank_name']
        if 'bid_no' in response:
            self.bid_no = response['bid_no']
        if 'fee_amt' in response:
            self.fee_amt = response['fee_amt']
        if 'fee_charge_url' in response:
            self.fee_charge_url = response['fee_charge_url']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
