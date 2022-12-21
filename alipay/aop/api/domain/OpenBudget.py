#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenBudget(object):

    def __init__(self):
        self._alert_users = None
        self._budget_id = None
        self._mode = None
        self._monitor_biz_id = None
        self._monitor_template_code = None
        self._monitor_trigger_code = None
        self._thresholds = None
        self._value = None

    @property
    def alert_users(self):
        return self._alert_users

    @alert_users.setter
    def alert_users(self, value):
        if isinstance(value, list):
            self._alert_users = list()
            for i in value:
                self._alert_users.append(i)
    @property
    def budget_id(self):
        return self._budget_id

    @budget_id.setter
    def budget_id(self, value):
        self._budget_id = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def monitor_biz_id(self):
        return self._monitor_biz_id

    @monitor_biz_id.setter
    def monitor_biz_id(self, value):
        self._monitor_biz_id = value
    @property
    def monitor_template_code(self):
        return self._monitor_template_code

    @monitor_template_code.setter
    def monitor_template_code(self, value):
        self._monitor_template_code = value
    @property
    def monitor_trigger_code(self):
        return self._monitor_trigger_code

    @monitor_trigger_code.setter
    def monitor_trigger_code(self, value):
        self._monitor_trigger_code = value
    @property
    def thresholds(self):
        return self._thresholds

    @thresholds.setter
    def thresholds(self, value):
        if isinstance(value, list):
            self._thresholds = list()
            for i in value:
                self._thresholds.append(i)
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.alert_users:
            if isinstance(self.alert_users, list):
                for i in range(0, len(self.alert_users)):
                    element = self.alert_users[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.alert_users[i] = element.to_alipay_dict()
            if hasattr(self.alert_users, 'to_alipay_dict'):
                params['alert_users'] = self.alert_users.to_alipay_dict()
            else:
                params['alert_users'] = self.alert_users
        if self.budget_id:
            if hasattr(self.budget_id, 'to_alipay_dict'):
                params['budget_id'] = self.budget_id.to_alipay_dict()
            else:
                params['budget_id'] = self.budget_id
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.monitor_biz_id:
            if hasattr(self.monitor_biz_id, 'to_alipay_dict'):
                params['monitor_biz_id'] = self.monitor_biz_id.to_alipay_dict()
            else:
                params['monitor_biz_id'] = self.monitor_biz_id
        if self.monitor_template_code:
            if hasattr(self.monitor_template_code, 'to_alipay_dict'):
                params['monitor_template_code'] = self.monitor_template_code.to_alipay_dict()
            else:
                params['monitor_template_code'] = self.monitor_template_code
        if self.monitor_trigger_code:
            if hasattr(self.monitor_trigger_code, 'to_alipay_dict'):
                params['monitor_trigger_code'] = self.monitor_trigger_code.to_alipay_dict()
            else:
                params['monitor_trigger_code'] = self.monitor_trigger_code
        if self.thresholds:
            if isinstance(self.thresholds, list):
                for i in range(0, len(self.thresholds)):
                    element = self.thresholds[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.thresholds[i] = element.to_alipay_dict()
            if hasattr(self.thresholds, 'to_alipay_dict'):
                params['thresholds'] = self.thresholds.to_alipay_dict()
            else:
                params['thresholds'] = self.thresholds
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenBudget()
        if 'alert_users' in d:
            o.alert_users = d['alert_users']
        if 'budget_id' in d:
            o.budget_id = d['budget_id']
        if 'mode' in d:
            o.mode = d['mode']
        if 'monitor_biz_id' in d:
            o.monitor_biz_id = d['monitor_biz_id']
        if 'monitor_template_code' in d:
            o.monitor_template_code = d['monitor_template_code']
        if 'monitor_trigger_code' in d:
            o.monitor_trigger_code = d['monitor_trigger_code']
        if 'thresholds' in d:
            o.thresholds = d['thresholds']
        if 'value' in d:
            o.value = d['value']
        return o


