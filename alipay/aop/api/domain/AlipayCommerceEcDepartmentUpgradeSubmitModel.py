#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcDepartmentUpgradeSubmitModel(object):

    def __init__(self):
        self._department_id = None
        self._enterprise_id = None
        self._sub_enterprise_name = None
        self._sub_identity = None
        self._sub_identity_open_id = None
        self._sub_identity_type = None

    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def sub_enterprise_name(self):
        return self._sub_enterprise_name

    @sub_enterprise_name.setter
    def sub_enterprise_name(self, value):
        self._sub_enterprise_name = value
    @property
    def sub_identity(self):
        return self._sub_identity

    @sub_identity.setter
    def sub_identity(self, value):
        self._sub_identity = value
    @property
    def sub_identity_open_id(self):
        return self._sub_identity_open_id

    @sub_identity_open_id.setter
    def sub_identity_open_id(self, value):
        self._sub_identity_open_id = value
    @property
    def sub_identity_type(self):
        return self._sub_identity_type

    @sub_identity_type.setter
    def sub_identity_type(self, value):
        self._sub_identity_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.department_id:
            if hasattr(self.department_id, 'to_alipay_dict'):
                params['department_id'] = self.department_id.to_alipay_dict()
            else:
                params['department_id'] = self.department_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.sub_enterprise_name:
            if hasattr(self.sub_enterprise_name, 'to_alipay_dict'):
                params['sub_enterprise_name'] = self.sub_enterprise_name.to_alipay_dict()
            else:
                params['sub_enterprise_name'] = self.sub_enterprise_name
        if self.sub_identity:
            if hasattr(self.sub_identity, 'to_alipay_dict'):
                params['sub_identity'] = self.sub_identity.to_alipay_dict()
            else:
                params['sub_identity'] = self.sub_identity
        if self.sub_identity_open_id:
            if hasattr(self.sub_identity_open_id, 'to_alipay_dict'):
                params['sub_identity_open_id'] = self.sub_identity_open_id.to_alipay_dict()
            else:
                params['sub_identity_open_id'] = self.sub_identity_open_id
        if self.sub_identity_type:
            if hasattr(self.sub_identity_type, 'to_alipay_dict'):
                params['sub_identity_type'] = self.sub_identity_type.to_alipay_dict()
            else:
                params['sub_identity_type'] = self.sub_identity_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcDepartmentUpgradeSubmitModel()
        if 'department_id' in d:
            o.department_id = d['department_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'sub_enterprise_name' in d:
            o.sub_enterprise_name = d['sub_enterprise_name']
        if 'sub_identity' in d:
            o.sub_identity = d['sub_identity']
        if 'sub_identity_open_id' in d:
            o.sub_identity_open_id = d['sub_identity_open_id']
        if 'sub_identity_type' in d:
            o.sub_identity_type = d['sub_identity_type']
        return o


