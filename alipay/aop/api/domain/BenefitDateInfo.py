#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitDateInfo(object):

    def __init__(self):
        self._benefit_active_time = None
        self._benefit_expired_time = None
        self._benefit_issue_time = None

    @property
    def benefit_active_time(self):
        return self._benefit_active_time

    @benefit_active_time.setter
    def benefit_active_time(self, value):
        self._benefit_active_time = value
    @property
    def benefit_expired_time(self):
        return self._benefit_expired_time

    @benefit_expired_time.setter
    def benefit_expired_time(self, value):
        self._benefit_expired_time = value
    @property
    def benefit_issue_time(self):
        return self._benefit_issue_time

    @benefit_issue_time.setter
    def benefit_issue_time(self, value):
        self._benefit_issue_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_active_time:
            if hasattr(self.benefit_active_time, 'to_alipay_dict'):
                params['benefit_active_time'] = self.benefit_active_time.to_alipay_dict()
            else:
                params['benefit_active_time'] = self.benefit_active_time
        if self.benefit_expired_time:
            if hasattr(self.benefit_expired_time, 'to_alipay_dict'):
                params['benefit_expired_time'] = self.benefit_expired_time.to_alipay_dict()
            else:
                params['benefit_expired_time'] = self.benefit_expired_time
        if self.benefit_issue_time:
            if hasattr(self.benefit_issue_time, 'to_alipay_dict'):
                params['benefit_issue_time'] = self.benefit_issue_time.to_alipay_dict()
            else:
                params['benefit_issue_time'] = self.benefit_issue_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitDateInfo()
        if 'benefit_active_time' in d:
            o.benefit_active_time = d['benefit_active_time']
        if 'benefit_expired_time' in d:
            o.benefit_expired_time = d['benefit_expired_time']
        if 'benefit_issue_time' in d:
            o.benefit_issue_time = d['benefit_issue_time']
        return o


