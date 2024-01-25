#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BookingLimit(object):

    def __init__(self):
        self._breakfast_policy = None
        self._children_policy = None
        self._pet_info = None
        self._time = None

    @property
    def breakfast_policy(self):
        return self._breakfast_policy

    @breakfast_policy.setter
    def breakfast_policy(self, value):
        self._breakfast_policy = value
    @property
    def children_policy(self):
        return self._children_policy

    @children_policy.setter
    def children_policy(self, value):
        self._children_policy = value
    @property
    def pet_info(self):
        return self._pet_info

    @pet_info.setter
    def pet_info(self, value):
        self._pet_info = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.breakfast_policy:
            if hasattr(self.breakfast_policy, 'to_alipay_dict'):
                params['breakfast_policy'] = self.breakfast_policy.to_alipay_dict()
            else:
                params['breakfast_policy'] = self.breakfast_policy
        if self.children_policy:
            if hasattr(self.children_policy, 'to_alipay_dict'):
                params['children_policy'] = self.children_policy.to_alipay_dict()
            else:
                params['children_policy'] = self.children_policy
        if self.pet_info:
            if hasattr(self.pet_info, 'to_alipay_dict'):
                params['pet_info'] = self.pet_info.to_alipay_dict()
            else:
                params['pet_info'] = self.pet_info
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BookingLimit()
        if 'breakfast_policy' in d:
            o.breakfast_policy = d['breakfast_policy']
        if 'children_policy' in d:
            o.children_policy = d['children_policy']
        if 'pet_info' in d:
            o.pet_info = d['pet_info']
        if 'time' in d:
            o.time = d['time']
        return o


