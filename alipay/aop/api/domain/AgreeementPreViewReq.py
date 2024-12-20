#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstitutionVO import InstitutionVO


class AgreeementPreViewReq(object):

    def __init__(self):
        self._agreement_version = None
        self._code = None
        self._fund_supplier = None

    @property
    def agreement_version(self):
        return self._agreement_version

    @agreement_version.setter
    def agreement_version(self, value):
        self._agreement_version = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def fund_supplier(self):
        return self._fund_supplier

    @fund_supplier.setter
    def fund_supplier(self, value):
        if isinstance(value, InstitutionVO):
            self._fund_supplier = value
        else:
            self._fund_supplier = InstitutionVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_version:
            if hasattr(self.agreement_version, 'to_alipay_dict'):
                params['agreement_version'] = self.agreement_version.to_alipay_dict()
            else:
                params['agreement_version'] = self.agreement_version
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.fund_supplier:
            if hasattr(self.fund_supplier, 'to_alipay_dict'):
                params['fund_supplier'] = self.fund_supplier.to_alipay_dict()
            else:
                params['fund_supplier'] = self.fund_supplier
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgreeementPreViewReq()
        if 'agreement_version' in d:
            o.agreement_version = d['agreement_version']
        if 'code' in d:
            o.code = d['code']
        if 'fund_supplier' in d:
            o.fund_supplier = d['fund_supplier']
        return o


