#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySalaryAccountbalanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySalaryAccountbalanceQueryResponse, self).__init__()
        self._amount = None
        self._bank_card_no = None
        self._currency = None
        self._sign_xml = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def sign_xml(self):
        return self._sign_xml

    @sign_xml.setter
    def sign_xml(self, value):
        self._sign_xml = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySalaryAccountbalanceQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'bank_card_no' in response:
            self.bank_card_no = response['bank_card_no']
        if 'currency' in response:
            self.currency = response['currency']
        if 'sign_xml' in response:
            self.sign_xml = response['sign_xml']
