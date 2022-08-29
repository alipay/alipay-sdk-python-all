#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZMGOCycleWithholdConfig(object):

    def __init__(self):
        self._deduct_plan = None
        self._exemption_period = None
        self._period = None
        self._period_type = None
        self._support_cycle_withhold_high_mode = None
        self._support_exemption_period = None
        self._withhold_mode = None

    @property
    def deduct_plan(self):
        return self._deduct_plan

    @deduct_plan.setter
    def deduct_plan(self, value):
        if isinstance(value, list):
            self._deduct_plan = list()
            for i in value:
                self._deduct_plan.append(i)
    @property
    def exemption_period(self):
        return self._exemption_period

    @exemption_period.setter
    def exemption_period(self, value):
        self._exemption_period = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value
    @property
    def support_cycle_withhold_high_mode(self):
        return self._support_cycle_withhold_high_mode

    @support_cycle_withhold_high_mode.setter
    def support_cycle_withhold_high_mode(self, value):
        self._support_cycle_withhold_high_mode = value
    @property
    def support_exemption_period(self):
        return self._support_exemption_period

    @support_exemption_period.setter
    def support_exemption_period(self, value):
        self._support_exemption_period = value
    @property
    def withhold_mode(self):
        return self._withhold_mode

    @withhold_mode.setter
    def withhold_mode(self, value):
        self._withhold_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.deduct_plan:
            if isinstance(self.deduct_plan, list):
                for i in range(0, len(self.deduct_plan)):
                    element = self.deduct_plan[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.deduct_plan[i] = element.to_alipay_dict()
            if hasattr(self.deduct_plan, 'to_alipay_dict'):
                params['deduct_plan'] = self.deduct_plan.to_alipay_dict()
            else:
                params['deduct_plan'] = self.deduct_plan
        if self.exemption_period:
            if hasattr(self.exemption_period, 'to_alipay_dict'):
                params['exemption_period'] = self.exemption_period.to_alipay_dict()
            else:
                params['exemption_period'] = self.exemption_period
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.period_type:
            if hasattr(self.period_type, 'to_alipay_dict'):
                params['period_type'] = self.period_type.to_alipay_dict()
            else:
                params['period_type'] = self.period_type
        if self.support_cycle_withhold_high_mode:
            if hasattr(self.support_cycle_withhold_high_mode, 'to_alipay_dict'):
                params['support_cycle_withhold_high_mode'] = self.support_cycle_withhold_high_mode.to_alipay_dict()
            else:
                params['support_cycle_withhold_high_mode'] = self.support_cycle_withhold_high_mode
        if self.support_exemption_period:
            if hasattr(self.support_exemption_period, 'to_alipay_dict'):
                params['support_exemption_period'] = self.support_exemption_period.to_alipay_dict()
            else:
                params['support_exemption_period'] = self.support_exemption_period
        if self.withhold_mode:
            if hasattr(self.withhold_mode, 'to_alipay_dict'):
                params['withhold_mode'] = self.withhold_mode.to_alipay_dict()
            else:
                params['withhold_mode'] = self.withhold_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZMGOCycleWithholdConfig()
        if 'deduct_plan' in d:
            o.deduct_plan = d['deduct_plan']
        if 'exemption_period' in d:
            o.exemption_period = d['exemption_period']
        if 'period' in d:
            o.period = d['period']
        if 'period_type' in d:
            o.period_type = d['period_type']
        if 'support_cycle_withhold_high_mode' in d:
            o.support_cycle_withhold_high_mode = d['support_cycle_withhold_high_mode']
        if 'support_exemption_period' in d:
            o.support_exemption_period = d['support_exemption_period']
        if 'withhold_mode' in d:
            o.withhold_mode = d['withhold_mode']
        return o


