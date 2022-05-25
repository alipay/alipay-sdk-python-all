#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FundSettleInfo(object):

    def __init__(self):
        self._bank_code = None
        self._cacl_type = None
        self._clearing_model = None
        self._fund_type = None
        self._sign_principal = None

    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def cacl_type(self):
        return self._cacl_type

    @cacl_type.setter
    def cacl_type(self, value):
        self._cacl_type = value
    @property
    def clearing_model(self):
        return self._clearing_model

    @clearing_model.setter
    def clearing_model(self, value):
        self._clearing_model = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def sign_principal(self):
        return self._sign_principal

    @sign_principal.setter
    def sign_principal(self, value):
        self._sign_principal = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.cacl_type:
            if hasattr(self.cacl_type, 'to_alipay_dict'):
                params['cacl_type'] = self.cacl_type.to_alipay_dict()
            else:
                params['cacl_type'] = self.cacl_type
        if self.clearing_model:
            if hasattr(self.clearing_model, 'to_alipay_dict'):
                params['clearing_model'] = self.clearing_model.to_alipay_dict()
            else:
                params['clearing_model'] = self.clearing_model
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        if self.sign_principal:
            if hasattr(self.sign_principal, 'to_alipay_dict'):
                params['sign_principal'] = self.sign_principal.to_alipay_dict()
            else:
                params['sign_principal'] = self.sign_principal
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundSettleInfo()
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'cacl_type' in d:
            o.cacl_type = d['cacl_type']
        if 'clearing_model' in d:
            o.clearing_model = d['clearing_model']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'sign_principal' in d:
            o.sign_principal = d['sign_principal']
        return o


