#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoantradeRepayBudgetQueryModel(object):

    def __init__(self):
        self._apply_repay_prin = None
        self._budget_type = None
        self._can_repay_flag = None
        self._ext_data = None
        self._ip_id = None
        self._ip_role_id = None
        self._loan_ar_no = None
        self._repay_scene = None

    @property
    def apply_repay_prin(self):
        return self._apply_repay_prin

    @apply_repay_prin.setter
    def apply_repay_prin(self, value):
        self._apply_repay_prin = value
    @property
    def budget_type(self):
        return self._budget_type

    @budget_type.setter
    def budget_type(self, value):
        self._budget_type = value
    @property
    def can_repay_flag(self):
        return self._can_repay_flag

    @can_repay_flag.setter
    def can_repay_flag(self, value):
        self._can_repay_flag = value
    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        self._ext_data = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def loan_ar_no(self):
        return self._loan_ar_no

    @loan_ar_no.setter
    def loan_ar_no(self, value):
        self._loan_ar_no = value
    @property
    def repay_scene(self):
        return self._repay_scene

    @repay_scene.setter
    def repay_scene(self, value):
        self._repay_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_repay_prin:
            if hasattr(self.apply_repay_prin, 'to_alipay_dict'):
                params['apply_repay_prin'] = self.apply_repay_prin.to_alipay_dict()
            else:
                params['apply_repay_prin'] = self.apply_repay_prin
        if self.budget_type:
            if hasattr(self.budget_type, 'to_alipay_dict'):
                params['budget_type'] = self.budget_type.to_alipay_dict()
            else:
                params['budget_type'] = self.budget_type
        if self.can_repay_flag:
            if hasattr(self.can_repay_flag, 'to_alipay_dict'):
                params['can_repay_flag'] = self.can_repay_flag.to_alipay_dict()
            else:
                params['can_repay_flag'] = self.can_repay_flag
        if self.ext_data:
            if hasattr(self.ext_data, 'to_alipay_dict'):
                params['ext_data'] = self.ext_data.to_alipay_dict()
            else:
                params['ext_data'] = self.ext_data
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.loan_ar_no:
            if hasattr(self.loan_ar_no, 'to_alipay_dict'):
                params['loan_ar_no'] = self.loan_ar_no.to_alipay_dict()
            else:
                params['loan_ar_no'] = self.loan_ar_no
        if self.repay_scene:
            if hasattr(self.repay_scene, 'to_alipay_dict'):
                params['repay_scene'] = self.repay_scene.to_alipay_dict()
            else:
                params['repay_scene'] = self.repay_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeRepayBudgetQueryModel()
        if 'apply_repay_prin' in d:
            o.apply_repay_prin = d['apply_repay_prin']
        if 'budget_type' in d:
            o.budget_type = d['budget_type']
        if 'can_repay_flag' in d:
            o.can_repay_flag = d['can_repay_flag']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'loan_ar_no' in d:
            o.loan_ar_no = d['loan_ar_no']
        if 'repay_scene' in d:
            o.repay_scene = d['repay_scene']
        return o


