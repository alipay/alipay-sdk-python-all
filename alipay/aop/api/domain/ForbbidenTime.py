#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ForbbidenTime(object):

    def __init__(self):
        self._days = None

    @property
    def days(self):
        return self._days

    @days.setter
    def days(self, value):
        self._days = value


    def to_alipay_dict(self):
        params = dict()
        if self.days:
            if hasattr(self.days, 'to_alipay_dict'):
                params['days'] = self.days.to_alipay_dict()
            else:
                params['days'] = self.days
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ForbbidenTime()
        if 'days' in d:
            o.days = d['days']
        return o


