#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgreementParams import AgreementParams


class AlipaySecurityDataSssModifyModel(object):

    def __init__(self):
        self._fff = None
        self._fr = None
        self._license_expiry_date = None
        self._xxx = None
        self._xxx_amount = None

    @property
    def fff(self):
        return self._fff

    @fff.setter
    def fff(self, value):
        if isinstance(value, AgreementParams):
            self._fff = value
        else:
            self._fff = AgreementParams.from_alipay_dict(value)
    @property
    def fr(self):
        return self._fr

    @fr.setter
    def fr(self, value):
        self._fr = value
    @property
    def license_expiry_date(self):
        return self._license_expiry_date

    @license_expiry_date.setter
    def license_expiry_date(self, value):
        self._license_expiry_date = value
    @property
    def xxx(self):
        return self._xxx

    @xxx.setter
    def xxx(self, value):
        self._xxx = value
    @property
    def xxx_amount(self):
        return self._xxx_amount

    @xxx_amount.setter
    def xxx_amount(self, value):
        self._xxx_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.fff:
            if hasattr(self.fff, 'to_alipay_dict'):
                params['fff'] = self.fff.to_alipay_dict()
            else:
                params['fff'] = self.fff
        if self.fr:
            if hasattr(self.fr, 'to_alipay_dict'):
                params['fr'] = self.fr.to_alipay_dict()
            else:
                params['fr'] = self.fr
        if self.license_expiry_date:
            if hasattr(self.license_expiry_date, 'to_alipay_dict'):
                params['license_expiry_date'] = self.license_expiry_date.to_alipay_dict()
            else:
                params['license_expiry_date'] = self.license_expiry_date
        if self.xxx:
            if hasattr(self.xxx, 'to_alipay_dict'):
                params['xxx'] = self.xxx.to_alipay_dict()
            else:
                params['xxx'] = self.xxx
        if self.xxx_amount:
            if hasattr(self.xxx_amount, 'to_alipay_dict'):
                params['xxx_amount'] = self.xxx_amount.to_alipay_dict()
            else:
                params['xxx_amount'] = self.xxx_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataSssModifyModel()
        if 'fff' in d:
            o.fff = d['fff']
        if 'fr' in d:
            o.fr = d['fr']
        if 'license_expiry_date' in d:
            o.license_expiry_date = d['license_expiry_date']
        if 'xxx' in d:
            o.xxx = d['xxx']
        if 'xxx_amount' in d:
            o.xxx_amount = d['xxx_amount']
        return o


