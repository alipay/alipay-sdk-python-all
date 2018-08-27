#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecruitInfo(object):

    def __init__(self):
        self._end_time = None
        self._exclude_constraint_shops = None
        self._plan_id = None
        self._start_time = None
        self._status = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def exclude_constraint_shops(self):
        return self._exclude_constraint_shops

    @exclude_constraint_shops.setter
    def exclude_constraint_shops(self, value):
        self._exclude_constraint_shops = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.exclude_constraint_shops:
            if hasattr(self.exclude_constraint_shops, 'to_alipay_dict'):
                params['exclude_constraint_shops'] = self.exclude_constraint_shops.to_alipay_dict()
            else:
                params['exclude_constraint_shops'] = self.exclude_constraint_shops
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitInfo()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'exclude_constraint_shops' in d:
            o.exclude_constraint_shops = d['exclude_constraint_shops']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        return o


