#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundMbpcardPurchaseSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundMbpcardPurchaseSignResponse, self).__init__()
        self._encrypt_algorithm_name = None
        self._fund_account_name = None
        self._fund_account_no = None
        self._purchase_id = None
        self._rsa_public_key_alias = None

    @property
    def encrypt_algorithm_name(self):
        return self._encrypt_algorithm_name

    @encrypt_algorithm_name.setter
    def encrypt_algorithm_name(self, value):
        self._encrypt_algorithm_name = value
    @property
    def fund_account_name(self):
        return self._fund_account_name

    @fund_account_name.setter
    def fund_account_name(self, value):
        self._fund_account_name = value
    @property
    def fund_account_no(self):
        return self._fund_account_no

    @fund_account_no.setter
    def fund_account_no(self, value):
        self._fund_account_no = value
    @property
    def purchase_id(self):
        return self._purchase_id

    @purchase_id.setter
    def purchase_id(self, value):
        self._purchase_id = value
    @property
    def rsa_public_key_alias(self):
        return self._rsa_public_key_alias

    @rsa_public_key_alias.setter
    def rsa_public_key_alias(self, value):
        self._rsa_public_key_alias = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundMbpcardPurchaseSignResponse, self).parse_response_content(response_content)
        if 'encrypt_algorithm_name' in response:
            self.encrypt_algorithm_name = response['encrypt_algorithm_name']
        if 'fund_account_name' in response:
            self.fund_account_name = response['fund_account_name']
        if 'fund_account_no' in response:
            self.fund_account_no = response['fund_account_no']
        if 'purchase_id' in response:
            self.purchase_id = response['purchase_id']
        if 'rsa_public_key_alias' in response:
            self.rsa_public_key_alias = response['rsa_public_key_alias']
