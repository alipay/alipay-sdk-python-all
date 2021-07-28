#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinancialnetAuthPbcQueryModel(object):

    def __init__(self):
        self._bank_code = None
        self._branch_name = None
        self._ext_info = None

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
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value


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
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinancialnetAuthPbcQueryModel()
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'branch_name' in d:
            o.branch_name = d['branch_name']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        return o


