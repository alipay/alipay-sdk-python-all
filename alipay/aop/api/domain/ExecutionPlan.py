#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExecutionPlan(object):

    def __init__(self):
        self._execute_time = None
        self._latest_execute_time = None
        self._period_id = None
        self._single_amount = None

    @property
    def execute_time(self):
        return self._execute_time

    @execute_time.setter
    def execute_time(self, value):
        self._execute_time = value
    @property
    def latest_execute_time(self):
        return self._latest_execute_time

    @latest_execute_time.setter
    def latest_execute_time(self, value):
        self._latest_execute_time = value
    @property
    def period_id(self):
        return self._period_id

    @period_id.setter
    def period_id(self, value):
        self._period_id = value
    @property
    def single_amount(self):
        return self._single_amount

    @single_amount.setter
    def single_amount(self, value):
        self._single_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.execute_time:
            if hasattr(self.execute_time, 'to_alipay_dict'):
                params['execute_time'] = self.execute_time.to_alipay_dict()
            else:
                params['execute_time'] = self.execute_time
        if self.latest_execute_time:
            if hasattr(self.latest_execute_time, 'to_alipay_dict'):
                params['latest_execute_time'] = self.latest_execute_time.to_alipay_dict()
            else:
                params['latest_execute_time'] = self.latest_execute_time
        if self.period_id:
            if hasattr(self.period_id, 'to_alipay_dict'):
                params['period_id'] = self.period_id.to_alipay_dict()
            else:
                params['period_id'] = self.period_id
        if self.single_amount:
            if hasattr(self.single_amount, 'to_alipay_dict'):
                params['single_amount'] = self.single_amount.to_alipay_dict()
            else:
                params['single_amount'] = self.single_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExecutionPlan()
        if 'execute_time' in d:
            o.execute_time = d['execute_time']
        if 'latest_execute_time' in d:
            o.latest_execute_time = d['latest_execute_time']
        if 'period_id' in d:
            o.period_id = d['period_id']
        if 'single_amount' in d:
            o.single_amount = d['single_amount']
        return o


