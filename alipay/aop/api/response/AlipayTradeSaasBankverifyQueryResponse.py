#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSaasBankverifyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasBankverifyQueryResponse, self).__init__()
        self._account_name = None
        self._bank_card_no = None
        self._bank_verify_order_no = None
        self._branch_bank_code = None
        self._branch_bank_name = None
        self._out_request_no = None
        self._root_bank_name = None
        self._status = None
        self._status_desc = None
        self._verify_end_time = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def bank_verify_order_no(self):
        return self._bank_verify_order_no

    @bank_verify_order_no.setter
    def bank_verify_order_no(self, value):
        self._bank_verify_order_no = value
    @property
    def branch_bank_code(self):
        return self._branch_bank_code

    @branch_bank_code.setter
    def branch_bank_code(self, value):
        self._branch_bank_code = value
    @property
    def branch_bank_name(self):
        return self._branch_bank_name

    @branch_bank_name.setter
    def branch_bank_name(self, value):
        self._branch_bank_name = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def root_bank_name(self):
        return self._root_bank_name

    @root_bank_name.setter
    def root_bank_name(self, value):
        self._root_bank_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value
    @property
    def verify_end_time(self):
        return self._verify_end_time

    @verify_end_time.setter
    def verify_end_time(self, value):
        self._verify_end_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasBankverifyQueryResponse, self).parse_response_content(response_content)
        if 'account_name' in response:
            self.account_name = response['account_name']
        if 'bank_card_no' in response:
            self.bank_card_no = response['bank_card_no']
        if 'bank_verify_order_no' in response:
            self.bank_verify_order_no = response['bank_verify_order_no']
        if 'branch_bank_code' in response:
            self.branch_bank_code = response['branch_bank_code']
        if 'branch_bank_name' in response:
            self.branch_bank_name = response['branch_bank_name']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'root_bank_name' in response:
            self.root_bank_name = response['root_bank_name']
        if 'status' in response:
            self.status = response['status']
        if 'status_desc' in response:
            self.status_desc = response['status_desc']
        if 'verify_end_time' in response:
            self.verify_end_time = response['verify_end_time']
