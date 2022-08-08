#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FundPlanForm(object):

    def __init__(self):
        self._amount = None
        self._calendar_type = None
        self._date = None
        self._incremental_amount = None
        self._out_biz_no = None
        self._plan_mode = None
        self._plan_times = None
        self._remark = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def calendar_type(self):
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, value):
        self._calendar_type = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def incremental_amount(self):
        return self._incremental_amount

    @incremental_amount.setter
    def incremental_amount(self, value):
        self._incremental_amount = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def plan_mode(self):
        return self._plan_mode

    @plan_mode.setter
    def plan_mode(self, value):
        self._plan_mode = value
    @property
    def plan_times(self):
        return self._plan_times

    @plan_times.setter
    def plan_times(self, value):
        self._plan_times = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.calendar_type:
            if hasattr(self.calendar_type, 'to_alipay_dict'):
                params['calendar_type'] = self.calendar_type.to_alipay_dict()
            else:
                params['calendar_type'] = self.calendar_type
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.incremental_amount:
            if hasattr(self.incremental_amount, 'to_alipay_dict'):
                params['incremental_amount'] = self.incremental_amount.to_alipay_dict()
            else:
                params['incremental_amount'] = self.incremental_amount
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.plan_mode:
            if hasattr(self.plan_mode, 'to_alipay_dict'):
                params['plan_mode'] = self.plan_mode.to_alipay_dict()
            else:
                params['plan_mode'] = self.plan_mode
        if self.plan_times:
            if hasattr(self.plan_times, 'to_alipay_dict'):
                params['plan_times'] = self.plan_times.to_alipay_dict()
            else:
                params['plan_times'] = self.plan_times
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundPlanForm()
        if 'amount' in d:
            o.amount = d['amount']
        if 'calendar_type' in d:
            o.calendar_type = d['calendar_type']
        if 'date' in d:
            o.date = d['date']
        if 'incremental_amount' in d:
            o.incremental_amount = d['incremental_amount']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'plan_mode' in d:
            o.plan_mode = d['plan_mode']
        if 'plan_times' in d:
            o.plan_times = d['plan_times']
        if 'remark' in d:
            o.remark = d['remark']
        return o


