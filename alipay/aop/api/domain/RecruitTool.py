#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PidShopInfo import PidShopInfo


class RecruitTool(object):

    def __init__(self):
        self._end_time = None
        self._exclude_constraint_shops = None
        self._pid_shops = None
        self._start_time = None

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
    def pid_shops(self):
        return self._pid_shops

    @pid_shops.setter
    def pid_shops(self, value):
        if isinstance(value, list):
            self._pid_shops = list()
            for i in value:
                if isinstance(i, PidShopInfo):
                    self._pid_shops.append(i)
                else:
                    self._pid_shops.append(PidShopInfo.from_alipay_dict(i))
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


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
        if self.pid_shops:
            if isinstance(self.pid_shops, list):
                for i in range(0, len(self.pid_shops)):
                    element = self.pid_shops[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pid_shops[i] = element.to_alipay_dict()
            if hasattr(self.pid_shops, 'to_alipay_dict'):
                params['pid_shops'] = self.pid_shops.to_alipay_dict()
            else:
                params['pid_shops'] = self.pid_shops
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitTool()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'exclude_constraint_shops' in d:
            o.exclude_constraint_shops = d['exclude_constraint_shops']
        if 'pid_shops' in d:
            o.pid_shops = d['pid_shops']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


