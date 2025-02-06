#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeductionPlanDataSyncRequest(object):

    def __init__(self):
        self._class_hours = None
        self._create_time = None
        self._deduction_amount = None
        self._deduction_plan_id = None
        self._deduction_plan_status = None
        self._original_amount = None
        self._period = None
        self._plan_deduction_time = None
        self._update_time = None

    @property
    def class_hours(self):
        return self._class_hours

    @class_hours.setter
    def class_hours(self, value):
        self._class_hours = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def deduction_amount(self):
        return self._deduction_amount

    @deduction_amount.setter
    def deduction_amount(self, value):
        self._deduction_amount = value
    @property
    def deduction_plan_id(self):
        return self._deduction_plan_id

    @deduction_plan_id.setter
    def deduction_plan_id(self, value):
        self._deduction_plan_id = value
    @property
    def deduction_plan_status(self):
        return self._deduction_plan_status

    @deduction_plan_status.setter
    def deduction_plan_status(self, value):
        self._deduction_plan_status = value
    @property
    def original_amount(self):
        return self._original_amount

    @original_amount.setter
    def original_amount(self, value):
        self._original_amount = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def plan_deduction_time(self):
        return self._plan_deduction_time

    @plan_deduction_time.setter
    def plan_deduction_time(self, value):
        self._plan_deduction_time = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.class_hours:
            if hasattr(self.class_hours, 'to_alipay_dict'):
                params['class_hours'] = self.class_hours.to_alipay_dict()
            else:
                params['class_hours'] = self.class_hours
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.deduction_amount:
            if hasattr(self.deduction_amount, 'to_alipay_dict'):
                params['deduction_amount'] = self.deduction_amount.to_alipay_dict()
            else:
                params['deduction_amount'] = self.deduction_amount
        if self.deduction_plan_id:
            if hasattr(self.deduction_plan_id, 'to_alipay_dict'):
                params['deduction_plan_id'] = self.deduction_plan_id.to_alipay_dict()
            else:
                params['deduction_plan_id'] = self.deduction_plan_id
        if self.deduction_plan_status:
            if hasattr(self.deduction_plan_status, 'to_alipay_dict'):
                params['deduction_plan_status'] = self.deduction_plan_status.to_alipay_dict()
            else:
                params['deduction_plan_status'] = self.deduction_plan_status
        if self.original_amount:
            if hasattr(self.original_amount, 'to_alipay_dict'):
                params['original_amount'] = self.original_amount.to_alipay_dict()
            else:
                params['original_amount'] = self.original_amount
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.plan_deduction_time:
            if hasattr(self.plan_deduction_time, 'to_alipay_dict'):
                params['plan_deduction_time'] = self.plan_deduction_time.to_alipay_dict()
            else:
                params['plan_deduction_time'] = self.plan_deduction_time
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeductionPlanDataSyncRequest()
        if 'class_hours' in d:
            o.class_hours = d['class_hours']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'deduction_amount' in d:
            o.deduction_amount = d['deduction_amount']
        if 'deduction_plan_id' in d:
            o.deduction_plan_id = d['deduction_plan_id']
        if 'deduction_plan_status' in d:
            o.deduction_plan_status = d['deduction_plan_status']
        if 'original_amount' in d:
            o.original_amount = d['original_amount']
        if 'period' in d:
            o.period = d['period']
        if 'plan_deduction_time' in d:
            o.plan_deduction_time = d['plan_deduction_time']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


