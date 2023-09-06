#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CompanyInfoRequestDTO(object):

    def __init__(self):
        self._company_code = None
        self._erp_instance = None
        self._ou_code = None

    @property
    def company_code(self):
        return self._company_code

    @company_code.setter
    def company_code(self, value):
        self._company_code = value
    @property
    def erp_instance(self):
        return self._erp_instance

    @erp_instance.setter
    def erp_instance(self, value):
        self._erp_instance = value
    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_code:
            if hasattr(self.company_code, 'to_alipay_dict'):
                params['company_code'] = self.company_code.to_alipay_dict()
            else:
                params['company_code'] = self.company_code
        if self.erp_instance:
            if hasattr(self.erp_instance, 'to_alipay_dict'):
                params['erp_instance'] = self.erp_instance.to_alipay_dict()
            else:
                params['erp_instance'] = self.erp_instance
        if self.ou_code:
            if hasattr(self.ou_code, 'to_alipay_dict'):
                params['ou_code'] = self.ou_code.to_alipay_dict()
            else:
                params['ou_code'] = self.ou_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompanyInfoRequestDTO()
        if 'company_code' in d:
            o.company_code = d['company_code']
        if 'erp_instance' in d:
            o.erp_instance = d['erp_instance']
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        return o


