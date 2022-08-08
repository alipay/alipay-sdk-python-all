#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoanapplyBkamcAntauthsignConsultModel(object):

    def __init__(self):
        self._cust_id = None
        self._cust_type = None
        self._prod_code = None

    @property
    def cust_id(self):
        return self._cust_id

    @cust_id.setter
    def cust_id(self, value):
        self._cust_id = value
    @property
    def cust_type(self):
        return self._cust_type

    @cust_type.setter
    def cust_type(self, value):
        self._cust_type = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.cust_id:
            if hasattr(self.cust_id, 'to_alipay_dict'):
                params['cust_id'] = self.cust_id.to_alipay_dict()
            else:
                params['cust_id'] = self.cust_id
        if self.cust_type:
            if hasattr(self.cust_type, 'to_alipay_dict'):
                params['cust_type'] = self.cust_type.to_alipay_dict()
            else:
                params['cust_type'] = self.cust_type
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoanapplyBkamcAntauthsignConsultModel()
        if 'cust_id' in d:
            o.cust_id = d['cust_id']
        if 'cust_type' in d:
            o.cust_type = d['cust_type']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        return o


