#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserTaskCountingDto(object):

    def __init__(self):
        self._cycle_acc_count = None
        self._total_consecutive_count = None

    @property
    def cycle_acc_count(self):
        return self._cycle_acc_count

    @cycle_acc_count.setter
    def cycle_acc_count(self, value):
        self._cycle_acc_count = value
    @property
    def total_consecutive_count(self):
        return self._total_consecutive_count

    @total_consecutive_count.setter
    def total_consecutive_count(self, value):
        self._total_consecutive_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.cycle_acc_count:
            if hasattr(self.cycle_acc_count, 'to_alipay_dict'):
                params['cycle_acc_count'] = self.cycle_acc_count.to_alipay_dict()
            else:
                params['cycle_acc_count'] = self.cycle_acc_count
        if self.total_consecutive_count:
            if hasattr(self.total_consecutive_count, 'to_alipay_dict'):
                params['total_consecutive_count'] = self.total_consecutive_count.to_alipay_dict()
            else:
                params['total_consecutive_count'] = self.total_consecutive_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserTaskCountingDto()
        if 'cycle_acc_count' in d:
            o.cycle_acc_count = d['cycle_acc_count']
        if 'total_consecutive_count' in d:
            o.total_consecutive_count = d['total_consecutive_count']
        return o


