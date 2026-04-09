#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssignFinanceDetail(object):

    def __init__(self):
        self._alipay_account = None
        self._alipay_pid = None
        self._apply_type_str = None
        self._format_available_amount = None
        self._format_benefit_amount = None
        self._format_credit_amount = None
        self._format_marketing_amount = None
        self._format_principal_amount = None
        self._principal_id = None
        self._principal_name = None
        self._remark = None
        self._scene_code_str = None
        self._time = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def alipay_pid(self):
        return self._alipay_pid

    @alipay_pid.setter
    def alipay_pid(self, value):
        self._alipay_pid = value
    @property
    def apply_type_str(self):
        return self._apply_type_str

    @apply_type_str.setter
    def apply_type_str(self, value):
        self._apply_type_str = value
    @property
    def format_available_amount(self):
        return self._format_available_amount

    @format_available_amount.setter
    def format_available_amount(self, value):
        self._format_available_amount = value
    @property
    def format_benefit_amount(self):
        return self._format_benefit_amount

    @format_benefit_amount.setter
    def format_benefit_amount(self, value):
        self._format_benefit_amount = value
    @property
    def format_credit_amount(self):
        return self._format_credit_amount

    @format_credit_amount.setter
    def format_credit_amount(self, value):
        self._format_credit_amount = value
    @property
    def format_marketing_amount(self):
        return self._format_marketing_amount

    @format_marketing_amount.setter
    def format_marketing_amount(self, value):
        self._format_marketing_amount = value
    @property
    def format_principal_amount(self):
        return self._format_principal_amount

    @format_principal_amount.setter
    def format_principal_amount(self, value):
        self._format_principal_amount = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_name(self):
        return self._principal_name

    @principal_name.setter
    def principal_name(self, value):
        self._principal_name = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def scene_code_str(self):
        return self._scene_code_str

    @scene_code_str.setter
    def scene_code_str(self, value):
        self._scene_code_str = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.alipay_pid:
            if hasattr(self.alipay_pid, 'to_alipay_dict'):
                params['alipay_pid'] = self.alipay_pid.to_alipay_dict()
            else:
                params['alipay_pid'] = self.alipay_pid
        if self.apply_type_str:
            if hasattr(self.apply_type_str, 'to_alipay_dict'):
                params['apply_type_str'] = self.apply_type_str.to_alipay_dict()
            else:
                params['apply_type_str'] = self.apply_type_str
        if self.format_available_amount:
            if hasattr(self.format_available_amount, 'to_alipay_dict'):
                params['format_available_amount'] = self.format_available_amount.to_alipay_dict()
            else:
                params['format_available_amount'] = self.format_available_amount
        if self.format_benefit_amount:
            if hasattr(self.format_benefit_amount, 'to_alipay_dict'):
                params['format_benefit_amount'] = self.format_benefit_amount.to_alipay_dict()
            else:
                params['format_benefit_amount'] = self.format_benefit_amount
        if self.format_credit_amount:
            if hasattr(self.format_credit_amount, 'to_alipay_dict'):
                params['format_credit_amount'] = self.format_credit_amount.to_alipay_dict()
            else:
                params['format_credit_amount'] = self.format_credit_amount
        if self.format_marketing_amount:
            if hasattr(self.format_marketing_amount, 'to_alipay_dict'):
                params['format_marketing_amount'] = self.format_marketing_amount.to_alipay_dict()
            else:
                params['format_marketing_amount'] = self.format_marketing_amount
        if self.format_principal_amount:
            if hasattr(self.format_principal_amount, 'to_alipay_dict'):
                params['format_principal_amount'] = self.format_principal_amount.to_alipay_dict()
            else:
                params['format_principal_amount'] = self.format_principal_amount
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.principal_name:
            if hasattr(self.principal_name, 'to_alipay_dict'):
                params['principal_name'] = self.principal_name.to_alipay_dict()
            else:
                params['principal_name'] = self.principal_name
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.scene_code_str:
            if hasattr(self.scene_code_str, 'to_alipay_dict'):
                params['scene_code_str'] = self.scene_code_str.to_alipay_dict()
            else:
                params['scene_code_str'] = self.scene_code_str
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssignFinanceDetail()
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'alipay_pid' in d:
            o.alipay_pid = d['alipay_pid']
        if 'apply_type_str' in d:
            o.apply_type_str = d['apply_type_str']
        if 'format_available_amount' in d:
            o.format_available_amount = d['format_available_amount']
        if 'format_benefit_amount' in d:
            o.format_benefit_amount = d['format_benefit_amount']
        if 'format_credit_amount' in d:
            o.format_credit_amount = d['format_credit_amount']
        if 'format_marketing_amount' in d:
            o.format_marketing_amount = d['format_marketing_amount']
        if 'format_principal_amount' in d:
            o.format_principal_amount = d['format_principal_amount']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_name' in d:
            o.principal_name = d['principal_name']
        if 'remark' in d:
            o.remark = d['remark']
        if 'scene_code_str' in d:
            o.scene_code_str = d['scene_code_str']
        if 'time' in d:
            o.time = d['time']
        return o


