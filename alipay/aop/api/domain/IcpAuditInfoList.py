#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IcpAuditInfoList(object):

    def __init__(self):
        self._audit_material = None
        self._audit_number = None
        self._audit_type = None

    @property
    def audit_material(self):
        return self._audit_material

    @audit_material.setter
    def audit_material(self, value):
        self._audit_material = value
    @property
    def audit_number(self):
        return self._audit_number

    @audit_number.setter
    def audit_number(self, value):
        self._audit_number = value
    @property
    def audit_type(self):
        return self._audit_type

    @audit_type.setter
    def audit_type(self, value):
        self._audit_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_material:
            if hasattr(self.audit_material, 'to_alipay_dict'):
                params['audit_material'] = self.audit_material.to_alipay_dict()
            else:
                params['audit_material'] = self.audit_material
        if self.audit_number:
            if hasattr(self.audit_number, 'to_alipay_dict'):
                params['audit_number'] = self.audit_number.to_alipay_dict()
            else:
                params['audit_number'] = self.audit_number
        if self.audit_type:
            if hasattr(self.audit_type, 'to_alipay_dict'):
                params['audit_type'] = self.audit_type.to_alipay_dict()
            else:
                params['audit_type'] = self.audit_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IcpAuditInfoList()
        if 'audit_material' in d:
            o.audit_material = d['audit_material']
        if 'audit_number' in d:
            o.audit_number = d['audit_number']
        if 'audit_type' in d:
            o.audit_type = d['audit_type']
        return o


