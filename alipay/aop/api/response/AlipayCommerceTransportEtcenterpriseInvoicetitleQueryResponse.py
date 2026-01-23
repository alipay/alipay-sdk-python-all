#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcenterpriseInvoicetitleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcenterpriseInvoicetitleQueryResponse, self).__init__()
        self._buyer_addr = None
        self._buyer_bank = None
        self._buyer_bank_account = None
        self._buyer_name = None
        self._buyer_tax_num = None
        self._buyer_tel = None
        self._title_type = None

    @property
    def buyer_addr(self):
        return self._buyer_addr

    @buyer_addr.setter
    def buyer_addr(self, value):
        self._buyer_addr = value
    @property
    def buyer_bank(self):
        return self._buyer_bank

    @buyer_bank.setter
    def buyer_bank(self, value):
        self._buyer_bank = value
    @property
    def buyer_bank_account(self):
        return self._buyer_bank_account

    @buyer_bank_account.setter
    def buyer_bank_account(self, value):
        self._buyer_bank_account = value
    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value
    @property
    def buyer_tax_num(self):
        return self._buyer_tax_num

    @buyer_tax_num.setter
    def buyer_tax_num(self, value):
        self._buyer_tax_num = value
    @property
    def buyer_tel(self):
        return self._buyer_tel

    @buyer_tel.setter
    def buyer_tel(self, value):
        self._buyer_tel = value
    @property
    def title_type(self):
        return self._title_type

    @title_type.setter
    def title_type(self, value):
        self._title_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcenterpriseInvoicetitleQueryResponse, self).parse_response_content(response_content)
        if 'buyer_addr' in response:
            self.buyer_addr = response['buyer_addr']
        if 'buyer_bank' in response:
            self.buyer_bank = response['buyer_bank']
        if 'buyer_bank_account' in response:
            self.buyer_bank_account = response['buyer_bank_account']
        if 'buyer_name' in response:
            self.buyer_name = response['buyer_name']
        if 'buyer_tax_num' in response:
            self.buyer_tax_num = response['buyer_tax_num']
        if 'buyer_tel' in response:
            self.buyer_tel = response['buyer_tel']
        if 'title_type' in response:
            self.title_type = response['title_type']
