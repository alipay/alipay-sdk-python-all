#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ModifyQuotaDetails(object):

    def __init__(self):
        self._quota_amount = None
        self._quota_dimension = None
        self._role = None

    @property
    def quota_amount(self):
        return self._quota_amount

    @quota_amount.setter
    def quota_amount(self, value):
        self._quota_amount = value
    @property
    def quota_dimension(self):
        return self._quota_dimension

    @quota_dimension.setter
    def quota_dimension(self, value):
        self._quota_dimension = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value


    def to_alipay_dict(self):
        params = dict()
        if self.quota_amount:
            if hasattr(self.quota_amount, 'to_alipay_dict'):
                params['quota_amount'] = self.quota_amount.to_alipay_dict()
            else:
                params['quota_amount'] = self.quota_amount
        if self.quota_dimension:
            if hasattr(self.quota_dimension, 'to_alipay_dict'):
                params['quota_dimension'] = self.quota_dimension.to_alipay_dict()
            else:
                params['quota_dimension'] = self.quota_dimension
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ModifyQuotaDetails()
        if 'quota_amount' in d:
            o.quota_amount = d['quota_amount']
        if 'quota_dimension' in d:
            o.quota_dimension = d['quota_dimension']
        if 'role' in d:
            o.role = d['role']
        return o


