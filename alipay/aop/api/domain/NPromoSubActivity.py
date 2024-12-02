#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NPromoSubActivity(object):

    def __init__(self):
        self._advanceable_time = None
        self._end_time = None
        self._period_no = None
        self._start_time = None
        self._status = None
        self._sub_activity_id = None
        self._target_trade_counts = None
        self._target_trade_days = None

    @property
    def advanceable_time(self):
        return self._advanceable_time

    @advanceable_time.setter
    def advanceable_time(self, value):
        self._advanceable_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def period_no(self):
        return self._period_no

    @period_no.setter
    def period_no(self, value):
        self._period_no = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_activity_id(self):
        return self._sub_activity_id

    @sub_activity_id.setter
    def sub_activity_id(self, value):
        self._sub_activity_id = value
    @property
    def target_trade_counts(self):
        return self._target_trade_counts

    @target_trade_counts.setter
    def target_trade_counts(self, value):
        self._target_trade_counts = value
    @property
    def target_trade_days(self):
        return self._target_trade_days

    @target_trade_days.setter
    def target_trade_days(self, value):
        self._target_trade_days = value


    def to_alipay_dict(self):
        params = dict()
        if self.advanceable_time:
            if hasattr(self.advanceable_time, 'to_alipay_dict'):
                params['advanceable_time'] = self.advanceable_time.to_alipay_dict()
            else:
                params['advanceable_time'] = self.advanceable_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.period_no:
            if hasattr(self.period_no, 'to_alipay_dict'):
                params['period_no'] = self.period_no.to_alipay_dict()
            else:
                params['period_no'] = self.period_no
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_activity_id:
            if hasattr(self.sub_activity_id, 'to_alipay_dict'):
                params['sub_activity_id'] = self.sub_activity_id.to_alipay_dict()
            else:
                params['sub_activity_id'] = self.sub_activity_id
        if self.target_trade_counts:
            if hasattr(self.target_trade_counts, 'to_alipay_dict'):
                params['target_trade_counts'] = self.target_trade_counts.to_alipay_dict()
            else:
                params['target_trade_counts'] = self.target_trade_counts
        if self.target_trade_days:
            if hasattr(self.target_trade_days, 'to_alipay_dict'):
                params['target_trade_days'] = self.target_trade_days.to_alipay_dict()
            else:
                params['target_trade_days'] = self.target_trade_days
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NPromoSubActivity()
        if 'advanceable_time' in d:
            o.advanceable_time = d['advanceable_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'period_no' in d:
            o.period_no = d['period_no']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'sub_activity_id' in d:
            o.sub_activity_id = d['sub_activity_id']
        if 'target_trade_counts' in d:
            o.target_trade_counts = d['target_trade_counts']
        if 'target_trade_days' in d:
            o.target_trade_days = d['target_trade_days']
        return o


