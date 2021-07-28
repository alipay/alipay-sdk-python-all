#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TimePeriodConfig import TimePeriodConfig


class PreOrderConfigInfo(object):

    def __init__(self):
        self._pre_order_status = None
        self._time_before = None
        self._time_period_config_list = None

    @property
    def pre_order_status(self):
        return self._pre_order_status

    @pre_order_status.setter
    def pre_order_status(self, value):
        self._pre_order_status = value
    @property
    def time_before(self):
        return self._time_before

    @time_before.setter
    def time_before(self, value):
        self._time_before = value
    @property
    def time_period_config_list(self):
        return self._time_period_config_list

    @time_period_config_list.setter
    def time_period_config_list(self, value):
        if isinstance(value, list):
            self._time_period_config_list = list()
            for i in value:
                if isinstance(i, TimePeriodConfig):
                    self._time_period_config_list.append(i)
                else:
                    self._time_period_config_list.append(TimePeriodConfig.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.pre_order_status:
            if hasattr(self.pre_order_status, 'to_alipay_dict'):
                params['pre_order_status'] = self.pre_order_status.to_alipay_dict()
            else:
                params['pre_order_status'] = self.pre_order_status
        if self.time_before:
            if hasattr(self.time_before, 'to_alipay_dict'):
                params['time_before'] = self.time_before.to_alipay_dict()
            else:
                params['time_before'] = self.time_before
        if self.time_period_config_list:
            if isinstance(self.time_period_config_list, list):
                for i in range(0, len(self.time_period_config_list)):
                    element = self.time_period_config_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.time_period_config_list[i] = element.to_alipay_dict()
            if hasattr(self.time_period_config_list, 'to_alipay_dict'):
                params['time_period_config_list'] = self.time_period_config_list.to_alipay_dict()
            else:
                params['time_period_config_list'] = self.time_period_config_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PreOrderConfigInfo()
        if 'pre_order_status' in d:
            o.pre_order_status = d['pre_order_status']
        if 'time_before' in d:
            o.time_before = d['time_before']
        if 'time_period_config_list' in d:
            o.time_period_config_list = d['time_period_config_list']
        return o


