#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTaxOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTaxOrderQueryResponse, self).__init__()
        self._identify_account_no = None
        self._identify_account_type = None
        self._out_order_no = None
        self._status = None
        self._success_time = None
        self._tax_no = None

    @property
    def identify_account_no(self):
        return self._identify_account_no

    @identify_account_no.setter
    def identify_account_no(self, value):
        self._identify_account_no = value
    @property
    def identify_account_type(self):
        return self._identify_account_type

    @identify_account_type.setter
    def identify_account_type(self, value):
        self._identify_account_type = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def success_time(self):
        return self._success_time

    @success_time.setter
    def success_time(self, value):
        self._success_time = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTaxOrderQueryResponse, self).parse_response_content(response_content)
        if 'identify_account_no' in response:
            self.identify_account_no = response['identify_account_no']
        if 'identify_account_type' in response:
            self.identify_account_type = response['identify_account_type']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'status' in response:
            self.status = response['status']
        if 'success_time' in response:
            self.success_time = response['success_time']
        if 'tax_no' in response:
            self.tax_no = response['tax_no']
