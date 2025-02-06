#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NSalesSubActivity(object):

    def __init__(self):
        self._end_time = None
        self._fulfill_amount = None
        self._fulfill_status = None
        self._period_no = None
        self._refer_trade_count = None
        self._refer_trade_days = None
        self._start_time = None
        self._sub_activity_id = None
        self._sub_activity_status = None
        self._target_trade_count = None
        self._target_trade_days = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def fulfill_amount(self):
        return self._fulfill_amount

    @fulfill_amount.setter
    def fulfill_amount(self, value):
        self._fulfill_amount = value
    @property
    def fulfill_status(self):
        return self._fulfill_status

    @fulfill_status.setter
    def fulfill_status(self, value):
        self._fulfill_status = value
    @property
    def period_no(self):
        return self._period_no

    @period_no.setter
    def period_no(self, value):
        self._period_no = value
    @property
    def refer_trade_count(self):
        return self._refer_trade_count

    @refer_trade_count.setter
    def refer_trade_count(self, value):
        self._refer_trade_count = value
    @property
    def refer_trade_days(self):
        return self._refer_trade_days

    @refer_trade_days.setter
    def refer_trade_days(self, value):
        self._refer_trade_days = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def sub_activity_id(self):
        return self._sub_activity_id

    @sub_activity_id.setter
    def sub_activity_id(self, value):
        self._sub_activity_id = value
    @property
    def sub_activity_status(self):
        return self._sub_activity_status

    @sub_activity_status.setter
    def sub_activity_status(self, value):
        self._sub_activity_status = value
    @property
    def target_trade_count(self):
        return self._target_trade_count

    @target_trade_count.setter
    def target_trade_count(self, value):
        self._target_trade_count = value
    @property
    def target_trade_days(self):
        return self._target_trade_days

    @target_trade_days.setter
    def target_trade_days(self, value):
        self._target_trade_days = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.fulfill_amount:
            if hasattr(self.fulfill_amount, 'to_alipay_dict'):
                params['fulfill_amount'] = self.fulfill_amount.to_alipay_dict()
            else:
                params['fulfill_amount'] = self.fulfill_amount
        if self.fulfill_status:
            if hasattr(self.fulfill_status, 'to_alipay_dict'):
                params['fulfill_status'] = self.fulfill_status.to_alipay_dict()
            else:
                params['fulfill_status'] = self.fulfill_status
        if self.period_no:
            if hasattr(self.period_no, 'to_alipay_dict'):
                params['period_no'] = self.period_no.to_alipay_dict()
            else:
                params['period_no'] = self.period_no
        if self.refer_trade_count:
            if hasattr(self.refer_trade_count, 'to_alipay_dict'):
                params['refer_trade_count'] = self.refer_trade_count.to_alipay_dict()
            else:
                params['refer_trade_count'] = self.refer_trade_count
        if self.refer_trade_days:
            if hasattr(self.refer_trade_days, 'to_alipay_dict'):
                params['refer_trade_days'] = self.refer_trade_days.to_alipay_dict()
            else:
                params['refer_trade_days'] = self.refer_trade_days
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.sub_activity_id:
            if hasattr(self.sub_activity_id, 'to_alipay_dict'):
                params['sub_activity_id'] = self.sub_activity_id.to_alipay_dict()
            else:
                params['sub_activity_id'] = self.sub_activity_id
        if self.sub_activity_status:
            if hasattr(self.sub_activity_status, 'to_alipay_dict'):
                params['sub_activity_status'] = self.sub_activity_status.to_alipay_dict()
            else:
                params['sub_activity_status'] = self.sub_activity_status
        if self.target_trade_count:
            if hasattr(self.target_trade_count, 'to_alipay_dict'):
                params['target_trade_count'] = self.target_trade_count.to_alipay_dict()
            else:
                params['target_trade_count'] = self.target_trade_count
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
        o = NSalesSubActivity()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'fulfill_amount' in d:
            o.fulfill_amount = d['fulfill_amount']
        if 'fulfill_status' in d:
            o.fulfill_status = d['fulfill_status']
        if 'period_no' in d:
            o.period_no = d['period_no']
        if 'refer_trade_count' in d:
            o.refer_trade_count = d['refer_trade_count']
        if 'refer_trade_days' in d:
            o.refer_trade_days = d['refer_trade_days']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'sub_activity_id' in d:
            o.sub_activity_id = d['sub_activity_id']
        if 'sub_activity_status' in d:
            o.sub_activity_status = d['sub_activity_status']
        if 'target_trade_count' in d:
            o.target_trade_count = d['target_trade_count']
        if 'target_trade_days' in d:
            o.target_trade_days = d['target_trade_days']
        return o


