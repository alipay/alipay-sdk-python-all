#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CampaignExtInfo(object):

    def __init__(self):
        self._interval_time = None
        self._month_limit = None
        self._threshold = None

    @property
    def interval_time(self):
        return self._interval_time

    @interval_time.setter
    def interval_time(self, value):
        self._interval_time = value
    @property
    def month_limit(self):
        return self._month_limit

    @month_limit.setter
    def month_limit(self, value):
        self._month_limit = value
    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        self._threshold = value


    def to_alipay_dict(self):
        params = dict()
        if self.interval_time:
            if hasattr(self.interval_time, 'to_alipay_dict'):
                params['interval_time'] = self.interval_time.to_alipay_dict()
            else:
                params['interval_time'] = self.interval_time
        if self.month_limit:
            if hasattr(self.month_limit, 'to_alipay_dict'):
                params['month_limit'] = self.month_limit.to_alipay_dict()
            else:
                params['month_limit'] = self.month_limit
        if self.threshold:
            if hasattr(self.threshold, 'to_alipay_dict'):
                params['threshold'] = self.threshold.to_alipay_dict()
            else:
                params['threshold'] = self.threshold
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CampaignExtInfo()
        if 'interval_time' in d:
            o.interval_time = d['interval_time']
        if 'month_limit' in d:
            o.month_limit = d['month_limit']
        if 'threshold' in d:
            o.threshold = d['threshold']
        return o


