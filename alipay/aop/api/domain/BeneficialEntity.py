#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BeneficialEntity(object):

    def __init__(self):
        self._cert_effective_date = None
        self._cert_expiration_date = None
        self._cert_no = None
        self._cert_type = None
        self._name = None

    @property
    def cert_effective_date(self):
        return self._cert_effective_date

    @cert_effective_date.setter
    def cert_effective_date(self, value):
        self._cert_effective_date = value
    @property
    def cert_expiration_date(self):
        return self._cert_expiration_date

    @cert_expiration_date.setter
    def cert_expiration_date(self, value):
        self._cert_expiration_date = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_effective_date:
            if hasattr(self.cert_effective_date, 'to_alipay_dict'):
                params['cert_effective_date'] = self.cert_effective_date.to_alipay_dict()
            else:
                params['cert_effective_date'] = self.cert_effective_date
        if self.cert_expiration_date:
            if hasattr(self.cert_expiration_date, 'to_alipay_dict'):
                params['cert_expiration_date'] = self.cert_expiration_date.to_alipay_dict()
            else:
                params['cert_expiration_date'] = self.cert_expiration_date
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BeneficialEntity()
        if 'cert_effective_date' in d:
            o.cert_effective_date = d['cert_effective_date']
        if 'cert_expiration_date' in d:
            o.cert_expiration_date = d['cert_expiration_date']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'name' in d:
            o.name = d['name']
        return o


