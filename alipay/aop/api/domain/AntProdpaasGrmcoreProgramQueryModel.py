#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntProdpaasGrmcoreProgramQueryModel(object):

    def __init__(self):
        self._env = None
        self._program_code = None
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
        o = AntProdpaasGrmcoreProgramQueryModel()
        if 'env' in d:
            o.env = d['env']
        if 'program_code' in d:
            o.program_code = d['program_code']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        return o


