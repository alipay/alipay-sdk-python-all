#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainInventoryOutConsultResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainInventoryOutConsultResponse, self).__init__()
        self._alert_amt = None
        self._arg_status = None
        self._controll_status = None
        self._credit_amt = None
        self._normal_int_amt = None
        self._ovd_int_amt = None
        self._ovd_int_pen_int_amt = None
        self._ovd_prin_pen_int_amt = None
        self._prin_amt = None
        self._repay_amt = None
        self._water_level_amt = None

    @property
    def alert_amt(self):
        return self._alert_amt

    @alert_amt.setter
    def alert_amt(self, value):
        self._alert_amt = value
    @property
    def arg_status(self):
        return self._arg_status

    @arg_status.setter
    def arg_status(self, value):
        self._arg_status = value
    @property
    def controll_status(self):
        return self._controll_status

    @controll_status.setter
    def controll_status(self, value):
        self._controll_status = value
    @property
    def credit_amt(self):
        return self._credit_amt

    @credit_amt.setter
    def credit_amt(self, value):
        self._credit_amt = value
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
    @property
    def water_level_amt(self):
        return self._water_level_amt

    @water_level_amt.setter
    def water_level_amt(self, value):
        self._water_level_amt = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainInventoryOutConsultResponse, self).parse_response_content(response_content)
        if 'alert_amt' in response:
            self.alert_amt = response['alert_amt']
        if 'arg_status' in response:
            self.arg_status = response['arg_status']
        if 'controll_status' in response:
            self.controll_status = response['controll_status']
        if 'credit_amt' in response:
            self.credit_amt = response['credit_amt']
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
        if 'water_level_amt' in response:
            self.water_level_amt = response['water_level_amt']
