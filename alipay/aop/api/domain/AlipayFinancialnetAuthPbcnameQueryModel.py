#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinancialnetAuthPbcnameQueryModel(object):

    def __init__(self):
        self._bank_code = None
        self._branch_name = None
        self._city = None
        self._exact = None
        self._inst_id = None
        self._inst_name = None
        self._provice = None

    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def branch_name(self):
        return self._branch_name

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def exact(self):
        return self._exact

    @exact.setter
    def exact(self, value):
        self._exact = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def provice(self):
        return self._provice

    @provice.setter
    def provice(self, value):
        self._provice = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.branch_name:
            if hasattr(self.branch_name, 'to_alipay_dict'):
                params['branch_name'] = self.branch_name.to_alipay_dict()
            else:
                params['branch_name'] = self.branch_name
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.exact:
            if hasattr(self.exact, 'to_alipay_dict'):
                params['exact'] = self.exact.to_alipay_dict()
            else:
                params['exact'] = self.exact
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.provice:
            if hasattr(self.provice, 'to_alipay_dict'):
                params['provice'] = self.provice.to_alipay_dict()
            else:
                params['provice'] = self.provice
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinancialnetAuthPbcnameQueryModel()
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'branch_name' in d:
            o.branch_name = d['branch_name']
        if 'city' in d:
            o.city = d['city']
        if 'exact' in d:
            o.exact = d['exact']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'provice' in d:
            o.provice = d['provice']
        return o


