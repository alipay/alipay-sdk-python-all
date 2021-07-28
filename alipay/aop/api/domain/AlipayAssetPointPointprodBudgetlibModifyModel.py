#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAssetPointPointprodBudgetlibModifyModel(object):

    def __init__(self):
        self._budget_code = None
        self._contract_pid = None
        self._end_time = None
        self._point_lib_id = None
        self._start_time = None

    @property
    def budget_code(self):
        return self._budget_code

    @budget_code.setter
    def budget_code(self, value):
        self._budget_code = value
    @property
    def contract_pid(self):
        return self._contract_pid

    @contract_pid.setter
    def contract_pid(self, value):
        self._contract_pid = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def point_lib_id(self):
        return self._point_lib_id

    @point_lib_id.setter
    def point_lib_id(self, value):
        self._point_lib_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget_code:
            if hasattr(self.budget_code, 'to_alipay_dict'):
                params['budget_code'] = self.budget_code.to_alipay_dict()
            else:
                params['budget_code'] = self.budget_code
        if self.contract_pid:
            if hasattr(self.contract_pid, 'to_alipay_dict'):
                params['contract_pid'] = self.contract_pid.to_alipay_dict()
            else:
                params['contract_pid'] = self.contract_pid
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.point_lib_id:
            if hasattr(self.point_lib_id, 'to_alipay_dict'):
                params['point_lib_id'] = self.point_lib_id.to_alipay_dict()
            else:
                params['point_lib_id'] = self.point_lib_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAssetPointPointprodBudgetlibModifyModel()
        if 'budget_code' in d:
            o.budget_code = d['budget_code']
        if 'contract_pid' in d:
            o.contract_pid = d['contract_pid']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'point_lib_id' in d:
            o.point_lib_id = d['point_lib_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


