#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContinuousPlan(object):

    def __init__(self):
        self._continuous_finish_time = None
        self._continuous_grace_time = None
        self._continuous_start_time = None
        self._currency = None
        self._pay_trade_no = None
        self._phase = None
        self._plan_index = None
        self._plan_no = None
        self._premium = None
        self._renewal_status = None

    @property
    def continuous_finish_time(self):
        return self._continuous_finish_time

    @continuous_finish_time.setter
    def continuous_finish_time(self, value):
        self._continuous_finish_time = value
    @property
    def continuous_grace_time(self):
        return self._continuous_grace_time

    @continuous_grace_time.setter
    def continuous_grace_time(self, value):
        self._continuous_grace_time = value
    @property
    def continuous_start_time(self):
        return self._continuous_start_time

    @continuous_start_time.setter
    def continuous_start_time(self, value):
        self._continuous_start_time = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def pay_trade_no(self):
        return self._pay_trade_no

    @pay_trade_no.setter
    def pay_trade_no(self, value):
        self._pay_trade_no = value
    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, value):
        self._phase = value
    @property
    def plan_index(self):
        return self._plan_index

    @plan_index.setter
    def plan_index(self, value):
        self._plan_index = value
    @property
    def plan_no(self):
        return self._plan_no

    @plan_no.setter
    def plan_no(self, value):
        self._plan_no = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def renewal_status(self):
        return self._renewal_status

    @renewal_status.setter
    def renewal_status(self, value):
        self._renewal_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.continuous_finish_time:
            if hasattr(self.continuous_finish_time, 'to_alipay_dict'):
                params['continuous_finish_time'] = self.continuous_finish_time.to_alipay_dict()
            else:
                params['continuous_finish_time'] = self.continuous_finish_time
        if self.continuous_grace_time:
            if hasattr(self.continuous_grace_time, 'to_alipay_dict'):
                params['continuous_grace_time'] = self.continuous_grace_time.to_alipay_dict()
            else:
                params['continuous_grace_time'] = self.continuous_grace_time
        if self.continuous_start_time:
            if hasattr(self.continuous_start_time, 'to_alipay_dict'):
                params['continuous_start_time'] = self.continuous_start_time.to_alipay_dict()
            else:
                params['continuous_start_time'] = self.continuous_start_time
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.pay_trade_no:
            if hasattr(self.pay_trade_no, 'to_alipay_dict'):
                params['pay_trade_no'] = self.pay_trade_no.to_alipay_dict()
            else:
                params['pay_trade_no'] = self.pay_trade_no
        if self.phase:
            if hasattr(self.phase, 'to_alipay_dict'):
                params['phase'] = self.phase.to_alipay_dict()
            else:
                params['phase'] = self.phase
        if self.plan_index:
            if hasattr(self.plan_index, 'to_alipay_dict'):
                params['plan_index'] = self.plan_index.to_alipay_dict()
            else:
                params['plan_index'] = self.plan_index
        if self.plan_no:
            if hasattr(self.plan_no, 'to_alipay_dict'):
                params['plan_no'] = self.plan_no.to_alipay_dict()
            else:
                params['plan_no'] = self.plan_no
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.renewal_status:
            if hasattr(self.renewal_status, 'to_alipay_dict'):
                params['renewal_status'] = self.renewal_status.to_alipay_dict()
            else:
                params['renewal_status'] = self.renewal_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContinuousPlan()
        if 'continuous_finish_time' in d:
            o.continuous_finish_time = d['continuous_finish_time']
        if 'continuous_grace_time' in d:
            o.continuous_grace_time = d['continuous_grace_time']
        if 'continuous_start_time' in d:
            o.continuous_start_time = d['continuous_start_time']
        if 'currency' in d:
            o.currency = d['currency']
        if 'pay_trade_no' in d:
            o.pay_trade_no = d['pay_trade_no']
        if 'phase' in d:
            o.phase = d['phase']
        if 'plan_index' in d:
            o.plan_index = d['plan_index']
        if 'plan_no' in d:
            o.plan_no = d['plan_no']
        if 'premium' in d:
            o.premium = d['premium']
        if 'renewal_status' in d:
            o.renewal_status = d['renewal_status']
        return o


