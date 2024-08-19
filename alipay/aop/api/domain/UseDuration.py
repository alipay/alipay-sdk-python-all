#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CanNoUseLimitDayInfo import CanNoUseLimitDayInfo
from alipay.aop.api.domain.LimitDayInfo import LimitDayInfo


class UseDuration(object):

    def __init__(self):
        self._can_no_use_date_list = None
        self._can_use_date_list = None
        self._use_time_type = None

    @property
    def can_no_use_date_list(self):
        return self._can_no_use_date_list

    @can_no_use_date_list.setter
    def can_no_use_date_list(self, value):
        if isinstance(value, list):
            self._can_no_use_date_list = list()
            for i in value:
                if isinstance(i, CanNoUseLimitDayInfo):
                    self._can_no_use_date_list.append(i)
                else:
                    self._can_no_use_date_list.append(CanNoUseLimitDayInfo.from_alipay_dict(i))
    @property
    def can_use_date_list(self):
        return self._can_use_date_list

    @can_use_date_list.setter
    def can_use_date_list(self, value):
        if isinstance(value, list):
            self._can_use_date_list = list()
            for i in value:
                if isinstance(i, LimitDayInfo):
                    self._can_use_date_list.append(i)
                else:
                    self._can_use_date_list.append(LimitDayInfo.from_alipay_dict(i))
    @property
    def use_time_type(self):
        return self._use_time_type

    @use_time_type.setter
    def use_time_type(self, value):
        self._use_time_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_no_use_date_list:
            if isinstance(self.can_no_use_date_list, list):
                for i in range(0, len(self.can_no_use_date_list)):
                    element = self.can_no_use_date_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.can_no_use_date_list[i] = element.to_alipay_dict()
            if hasattr(self.can_no_use_date_list, 'to_alipay_dict'):
                params['can_no_use_date_list'] = self.can_no_use_date_list.to_alipay_dict()
            else:
                params['can_no_use_date_list'] = self.can_no_use_date_list
        if self.can_use_date_list:
            if isinstance(self.can_use_date_list, list):
                for i in range(0, len(self.can_use_date_list)):
                    element = self.can_use_date_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.can_use_date_list[i] = element.to_alipay_dict()
            if hasattr(self.can_use_date_list, 'to_alipay_dict'):
                params['can_use_date_list'] = self.can_use_date_list.to_alipay_dict()
            else:
                params['can_use_date_list'] = self.can_use_date_list
        if self.use_time_type:
            if hasattr(self.use_time_type, 'to_alipay_dict'):
                params['use_time_type'] = self.use_time_type.to_alipay_dict()
            else:
                params['use_time_type'] = self.use_time_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UseDuration()
        if 'can_no_use_date_list' in d:
            o.can_no_use_date_list = d['can_no_use_date_list']
        if 'can_use_date_list' in d:
            o.can_use_date_list = d['can_use_date_list']
        if 'use_time_type' in d:
            o.use_time_type = d['use_time_type']
        return o


