#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainInventoryOutApplyResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainInventoryOutApplyResponse, self).__init__()
        self._normal_int_amt = None
        self._ovd_int_amt = None
        self._ovd_int_pen_int_amt = None
        self._ovd_prin_pen_int_amt = None
        self._prin_amt = None
        self._repay_amt = None

    @property
    def normal_int_amt(self):
        return self._normal_int_amt

    @normal_int_amt.setter
    def normal_int_amt(self, value):
        self._normal_int_amt = value
    @property
    def ovd_int_amt(self):
        return self._ovd_int_amt

    @ovd_int_amt.setter
    def ovd_int_amt(self, value):
        self._ovd_int_amt = value
    @property
    def ovd_int_pen_int_amt(self):
        return self._ovd_int_pen_int_amt

    @ovd_int_pen_int_amt.setter
    def ovd_int_pen_int_amt(self, value):
        self._ovd_int_pen_int_amt = value
    @property
    def ovd_prin_pen_int_amt(self):
        return self._ovd_prin_pen_int_amt

    @ovd_prin_pen_int_amt.setter
    def ovd_prin_pen_int_amt(self, value):
        self._ovd_prin_pen_int_amt = value
    @property
    def prin_amt(self):
        return self._prin_amt

    @prin_amt.setter
    def prin_amt(self, value):
        self._prin_amt = value
    @property
    def repay_amt(self):
        return self._repay_amt

    @repay_amt.setter
    def repay_amt(self, value):
        self._repay_amt = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainInventoryOutApplyResponse, self).parse_response_content(response_content)
        if 'normal_int_amt' in response:
            self.normal_int_amt = response['normal_int_amt']
        if 'ovd_int_amt' in response:
            self.ovd_int_amt = response['ovd_int_amt']
        if 'ovd_int_pen_int_amt' in response:
            self.ovd_int_pen_int_amt = response['ovd_int_pen_int_amt']
        if 'ovd_prin_pen_int_amt' in response:
            self.ovd_prin_pen_int_amt = response['ovd_prin_pen_int_amt']
        if 'prin_amt' in response:
            self.prin_amt = response['prin_amt']
        if 'repay_amt' in response:
            self.repay_amt = response['repay_amt']
