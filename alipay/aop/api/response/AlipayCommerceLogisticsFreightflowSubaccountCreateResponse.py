#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowSubaccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowSubaccountCreateResponse, self).__init__()
        self._auth_code = None
        self._bank_cert_name = None
        self._branch_name = None
        self._branch_no = None
        self._corporate_settlement_card = None
        self._sub_account_name = None
        self._sub_bank_card_no = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def bank_cert_name(self):
        return self._bank_cert_name

    @bank_cert_name.setter
    def bank_cert_name(self, value):
        self._bank_cert_name = value
    @property
    def branch_name(self):
        return self._branch_name

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = value
    @property
    def branch_no(self):
        return self._branch_no

    @branch_no.setter
    def branch_no(self, value):
        self._branch_no = value
    @property
    def corporate_settlement_card(self):
        return self._corporate_settlement_card

    @corporate_settlement_card.setter
    def corporate_settlement_card(self, value):
        self._corporate_settlement_card = value
    @property
    def sub_account_name(self):
        return self._sub_account_name

    @sub_account_name.setter
    def sub_account_name(self, value):
        self._sub_account_name = value
    @property
    def sub_bank_card_no(self):
        return self._sub_bank_card_no

    @sub_bank_card_no.setter
    def sub_bank_card_no(self, value):
        self._sub_bank_card_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowSubaccountCreateResponse, self).parse_response_content(response_content)
        if 'auth_code' in response:
            self.auth_code = response['auth_code']
        if 'bank_cert_name' in response:
            self.bank_cert_name = response['bank_cert_name']
        if 'branch_name' in response:
            self.branch_name = response['branch_name']
        if 'branch_no' in response:
            self.branch_no = response['branch_no']
        if 'corporate_settlement_card' in response:
            self.corporate_settlement_card = response['corporate_settlement_card']
        if 'sub_account_name' in response:
            self.sub_account_name = response['sub_account_name']
        if 'sub_bank_card_no' in response:
            self.sub_bank_card_no = response['sub_bank_card_no']
