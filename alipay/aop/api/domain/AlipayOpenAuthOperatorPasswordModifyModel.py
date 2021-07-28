#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperatorQuery import OperatorQuery


class AlipayOpenAuthOperatorPasswordModifyModel(object):

    def __init__(self):
        self._new_password = None
        self._operator = None
        self._tenant_id = None

    @property
    def new_password(self):
        return self._new_password

    @new_password.setter
    def new_password(self, value):
        self._new_password = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        if isinstance(value, OperatorQuery):
            self._operator = value
        else:
            self._operator = OperatorQuery.from_alipay_dict(value)
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.new_password:
            if hasattr(self.new_password, 'to_alipay_dict'):
                params['new_password'] = self.new_password.to_alipay_dict()
            else:
                params['new_password'] = self.new_password
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAuthOperatorPasswordModifyModel()
        if 'new_password' in d:
            o.new_password = d['new_password']
        if 'operator' in d:
            o.operator = d['operator']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


