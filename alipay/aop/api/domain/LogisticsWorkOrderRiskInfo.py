#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticsWorkOrderRiskInfo(object):

    def __init__(self):
        self._check_time = None
        self._fail_reason = None

    @property
    def check_time(self):
        return self._check_time

    @check_time.setter
    def check_time(self, value):
        self._check_time = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_time:
            if hasattr(self.check_time, 'to_alipay_dict'):
                params['check_time'] = self.check_time.to_alipay_dict()
            else:
                params['check_time'] = self.check_time
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsWorkOrderRiskInfo()
        if 'check_time' in d:
            o.check_time = d['check_time']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        return o


