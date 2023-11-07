#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationDcsMerchantqrcodeQueryModel(object):

    def __init__(self):
        self._apply_merchant_pid = None
        self._isv_pid = None
        self._merchant_pid = None
        self._plan_id = None
        self._role_id = None

    @property
    def apply_merchant_pid(self):
        return self._apply_merchant_pid

    @apply_merchant_pid.setter
    def apply_merchant_pid(self, value):
        self._apply_merchant_pid = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def role_id(self):
        return self._role_id

    @role_id.setter
    def role_id(self, value):
        self._role_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_merchant_pid:
            if hasattr(self.apply_merchant_pid, 'to_alipay_dict'):
                params['apply_merchant_pid'] = self.apply_merchant_pid.to_alipay_dict()
            else:
                params['apply_merchant_pid'] = self.apply_merchant_pid
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.role_id:
            if hasattr(self.role_id, 'to_alipay_dict'):
                params['role_id'] = self.role_id.to_alipay_dict()
            else:
                params['role_id'] = self.role_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationDcsMerchantqrcodeQueryModel()
        if 'apply_merchant_pid' in d:
            o.apply_merchant_pid = d['apply_merchant_pid']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'role_id' in d:
            o.role_id = d['role_id']
        return o


