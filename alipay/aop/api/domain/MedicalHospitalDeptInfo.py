#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalHospitalDeptInfo(object):

    def __init__(self):
        self._code = None
        self._location = None
        self._name = None
        self._parent_name = None
        self._partner_code = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def parent_name(self):
        return self._parent_name

    @parent_name.setter
    def parent_name(self, value):
        self._parent_name = value
    @property
    def partner_code(self):
        return self._partner_code

    @partner_code.setter
    def partner_code(self, value):
        self._partner_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.parent_name:
            if hasattr(self.parent_name, 'to_alipay_dict'):
                params['parent_name'] = self.parent_name.to_alipay_dict()
            else:
                params['parent_name'] = self.parent_name
        if self.partner_code:
            if hasattr(self.partner_code, 'to_alipay_dict'):
                params['partner_code'] = self.partner_code.to_alipay_dict()
            else:
                params['partner_code'] = self.partner_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalHospitalDeptInfo()
        if 'code' in d:
            o.code = d['code']
        if 'location' in d:
            o.location = d['location']
        if 'name' in d:
            o.name = d['name']
        if 'parent_name' in d:
            o.parent_name = d['parent_name']
        if 'partner_code' in d:
            o.partner_code = d['partner_code']
        return o


