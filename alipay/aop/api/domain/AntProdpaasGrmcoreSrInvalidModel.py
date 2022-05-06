#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntProdpaasGrmcoreSrInvalidModel(object):

    def __init__(self):
        self._env = None
        self._program_code = None
        self._sr_nos = None
        self._suppliers = None
        self._tenant_code = None

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def program_code(self):
        return self._program_code

    @program_code.setter
    def program_code(self, value):
        self._program_code = value
    @property
    def sr_nos(self):
        return self._sr_nos

    @sr_nos.setter
    def sr_nos(self, value):
        if isinstance(value, list):
            self._sr_nos = list()
            for i in value:
                self._sr_nos.append(i)
    @property
    def suppliers(self):
        return self._suppliers

    @suppliers.setter
    def suppliers(self, value):
        if isinstance(value, list):
            self._suppliers = list()
            for i in value:
                self._suppliers.append(i)
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.program_code:
            if hasattr(self.program_code, 'to_alipay_dict'):
                params['program_code'] = self.program_code.to_alipay_dict()
            else:
                params['program_code'] = self.program_code
        if self.sr_nos:
            if isinstance(self.sr_nos, list):
                for i in range(0, len(self.sr_nos)):
                    element = self.sr_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sr_nos[i] = element.to_alipay_dict()
            if hasattr(self.sr_nos, 'to_alipay_dict'):
                params['sr_nos'] = self.sr_nos.to_alipay_dict()
            else:
                params['sr_nos'] = self.sr_nos
        if self.suppliers:
            if isinstance(self.suppliers, list):
                for i in range(0, len(self.suppliers)):
                    element = self.suppliers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.suppliers[i] = element.to_alipay_dict()
            if hasattr(self.suppliers, 'to_alipay_dict'):
                params['suppliers'] = self.suppliers.to_alipay_dict()
            else:
                params['suppliers'] = self.suppliers
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntProdpaasGrmcoreSrInvalidModel()
        if 'env' in d:
            o.env = d['env']
        if 'program_code' in d:
            o.program_code = d['program_code']
        if 'sr_nos' in d:
            o.sr_nos = d['sr_nos']
        if 'suppliers' in d:
            o.suppliers = d['suppliers']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        return o


