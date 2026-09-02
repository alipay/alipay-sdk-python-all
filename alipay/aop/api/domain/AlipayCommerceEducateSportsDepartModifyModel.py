#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSportsDepartModifyModel(object):

    def __init__(self):
        self._department_code = None
        self._name = None
        self._organization_code = None

    @property
    def department_code(self):
        return self._department_code

    @department_code.setter
    def department_code(self, value):
        self._department_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def organization_code(self):
        return self._organization_code

    @organization_code.setter
    def organization_code(self, value):
        self._organization_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.department_code:
            if hasattr(self.department_code, 'to_alipay_dict'):
                params['department_code'] = self.department_code.to_alipay_dict()
            else:
                params['department_code'] = self.department_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.organization_code:
            if hasattr(self.organization_code, 'to_alipay_dict'):
                params['organization_code'] = self.organization_code.to_alipay_dict()
            else:
                params['organization_code'] = self.organization_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSportsDepartModifyModel()
        if 'department_code' in d:
            o.department_code = d['department_code']
        if 'name' in d:
            o.name = d['name']
        if 'organization_code' in d:
            o.organization_code = d['organization_code']
        return o


