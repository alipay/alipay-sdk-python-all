#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankPaymentTradeBankBranchQueryModel(object):

    def __init__(self):
        self._bank_name = None
        self._branch_bank_code = None
        self._district_code = None
        self._root_bank_code = None

    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def branch_bank_code(self):
        return self._branch_bank_code

    @branch_bank_code.setter
    def branch_bank_code(self, value):
        self._branch_bank_code = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def root_bank_code(self):
        return self._root_bank_code

    @root_bank_code.setter
    def root_bank_code(self, value):
        self._root_bank_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.branch_bank_code:
            if hasattr(self.branch_bank_code, 'to_alipay_dict'):
                params['branch_bank_code'] = self.branch_bank_code.to_alipay_dict()
            else:
                params['branch_bank_code'] = self.branch_bank_code
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.root_bank_code:
            if hasattr(self.root_bank_code, 'to_alipay_dict'):
                params['root_bank_code'] = self.root_bank_code.to_alipay_dict()
            else:
                params['root_bank_code'] = self.root_bank_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankPaymentTradeBankBranchQueryModel()
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'branch_bank_code' in d:
            o.branch_bank_code = d['branch_bank_code']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'root_bank_code' in d:
            o.root_bank_code = d['root_bank_code']
        return o


