#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowSubaccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowSubaccountCreateResponse, self).__init__()
        self._bank_cert_name = None
        self._branch_name = None
        self._branch_no = None
        self._sub_bank_card_no = None

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
    def sub_bank_card_no(self):
        return self._sub_bank_card_no

    @sub_bank_card_no.setter
    def sub_bank_card_no(self, value):
        self._sub_bank_card_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowSubaccountCreateResponse, self).parse_response_content(response_content)
        if 'bank_cert_name' in response:
            self.bank_cert_name = response['bank_cert_name']
        if 'branch_name' in response:
            self.branch_name = response['branch_name']
        if 'branch_no' in response:
            self.branch_no = response['branch_no']
        if 'sub_bank_card_no' in response:
            self.sub_bank_card_no = response['sub_bank_card_no']
