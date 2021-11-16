#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityBenefit(object):

    def __init__(self):
        self._benefit_rule = None
        self._out_benefit_id = None
        self._priority = None
        self._status = None

    @property
    def benefit_rule(self):
        return self._benefit_rule

    @benefit_rule.setter
    def benefit_rule(self, value):
        self._benefit_rule = value
    @property
    def out_benefit_id(self):
        return self._out_benefit_id

    @out_benefit_id.setter
    def out_benefit_id(self, value):
        self._out_benefit_id = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_rule:
            if hasattr(self.benefit_rule, 'to_alipay_dict'):
                params['benefit_rule'] = self.benefit_rule.to_alipay_dict()
            else:
                params['benefit_rule'] = self.benefit_rule
        if self.out_benefit_id:
            if hasattr(self.out_benefit_id, 'to_alipay_dict'):
                params['out_benefit_id'] = self.out_benefit_id.to_alipay_dict()
            else:
                params['out_benefit_id'] = self.out_benefit_id
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityBenefit()
        if 'benefit_rule' in d:
            o.benefit_rule = d['benefit_rule']
        if 'out_benefit_id' in d:
            o.out_benefit_id = d['out_benefit_id']
        if 'priority' in d:
            o.priority = d['priority']
        if 'status' in d:
            o.status = d['status']
        return o


