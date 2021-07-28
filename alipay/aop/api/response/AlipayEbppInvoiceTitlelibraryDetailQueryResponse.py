#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceTitlelibraryDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceTitlelibraryDetailQueryResponse, self).__init__()
        self._address = None
        self._bank_account = None
        self._bank_name = None
        self._register_no = None
        self._telephone = None
        self._title_name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def bank_account(self):
        return self._bank_account

    @bank_account.setter
    def bank_account(self, value):
        self._bank_account = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def register_no(self):
        return self._register_no

    @register_no.setter
    def register_no(self, value):
        self._register_no = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value
    @property
    def title_name(self):
        return self._title_name

    @title_name.setter
    def title_name(self, value):
        self._title_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceTitlelibraryDetailQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'bank_account' in response:
            self.bank_account = response['bank_account']
        if 'bank_name' in response:
            self.bank_name = response['bank_name']
        if 'register_no' in response:
            self.register_no = response['register_no']
        if 'telephone' in response:
            self.telephone = response['telephone']
        if 'title_name' in response:
            self.title_name = response['title_name']
