#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeductionPlanInfo(object):

    def __init__(self):
        self._certificate_serial_no = None
        self._deduction_amount = None
        self._deduction_plan_status = None
        self._original_amount = None
        self._period = None
        self._plan_deduction_time = None

    @property
    def certificate_serial_no(self):
        return self._certificate_serial_no

    @certificate_serial_no.setter
    def certificate_serial_no(self, value):
        self._certificate_serial_no = value
    @property
    def deduction_amount(self):
        return self._deduction_amount

    @deduction_amount.setter
    def deduction_amount(self, value):
        self._deduction_amount = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_serial_no:
            if hasattr(self.certificate_serial_no, 'to_alipay_dict'):
                params['certificate_serial_no'] = self.certificate_serial_no.to_alipay_dict()
            else:
                params['certificate_serial_no'] = self.certificate_serial_no
        if self.deduction_amount:
            if hasattr(self.deduction_amount, 'to_alipay_dict'):
                params['deduction_amount'] = self.deduction_amount.to_alipay_dict()
            else:
                params['deduction_amount'] = self.deduction_amount
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeductionPlanInfo()
        if 'certificate_serial_no' in d:
            o.certificate_serial_no = d['certificate_serial_no']
        if 'deduction_amount' in d:
            o.deduction_amount = d['deduction_amount']
        if 'deduction_plan_status' in d:
            o.deduction_plan_status = d['deduction_plan_status']
        if 'original_amount' in d:
            o.original_amount = d['original_amount']
        if 'period' in d:
            o.period = d['period']
        if 'plan_deduction_time' in d:
            o.plan_deduction_time = d['plan_deduction_time']
        return o


