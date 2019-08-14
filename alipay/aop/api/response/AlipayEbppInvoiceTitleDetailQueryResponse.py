#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceTitleDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceTitleDetailQueryResponse, self).__init__()
        self._address = None
        self._name = None
        self._open_bank_account = None
        self._open_bank_name = None
        self._tax_register_no = None
        self._telephone = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open_bank_account(self):
        return self._open_bank_account

    @open_bank_account.setter
    def open_bank_account(self, value):
        self._open_bank_account = value
    @property
    def open_bank_name(self):
        return self._open_bank_name

    @open_bank_name.setter
    def open_bank_name(self, value):
        self._open_bank_name = value
    @property
    def tax_register_no(self):
        return self._tax_register_no

    @tax_register_no.setter
    def tax_register_no(self, value):
        self._tax_register_no = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceTitleDetailQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'name' in response:
            self.name = response['name']
        if 'open_bank_account' in response:
            self.open_bank_account = response['open_bank_account']
        if 'open_bank_name' in response:
            self.open_bank_name = response['open_bank_name']
        if 'tax_register_no' in response:
            self.tax_register_no = response['tax_register_no']
        if 'telephone' in response:
            self.telephone = response['telephone']
