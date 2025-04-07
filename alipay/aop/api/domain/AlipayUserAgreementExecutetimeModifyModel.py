#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAgreementExecutetimeModifyModel(object):

    def __init__(self):
        self._agreement_no = None
        self._deduct_permission = None
        self._execute_time = None
        self._modify_type = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def deduct_permission(self):
        return self._deduct_permission

    @deduct_permission.setter
    def deduct_permission(self, value):
        self._deduct_permission = value
    @property
    def execute_time(self):
        return self._execute_time

    @execute_time.setter
    def execute_time(self, value):
        self._execute_time = value
    @property
    def modify_type(self):
        return self._modify_type

    @modify_type.setter
    def modify_type(self, value):
        self._modify_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.deduct_permission:
            if hasattr(self.deduct_permission, 'to_alipay_dict'):
                params['deduct_permission'] = self.deduct_permission.to_alipay_dict()
            else:
                params['deduct_permission'] = self.deduct_permission
        if self.execute_time:
            if hasattr(self.execute_time, 'to_alipay_dict'):
                params['execute_time'] = self.execute_time.to_alipay_dict()
            else:
                params['execute_time'] = self.execute_time
        if self.modify_type:
            if hasattr(self.modify_type, 'to_alipay_dict'):
                params['modify_type'] = self.modify_type.to_alipay_dict()
            else:
                params['modify_type'] = self.modify_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementExecutetimeModifyModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'deduct_permission' in d:
            o.deduct_permission = d['deduct_permission']
        if 'execute_time' in d:
            o.execute_time = d['execute_time']
        if 'modify_type' in d:
            o.modify_type = d['modify_type']
        return o


