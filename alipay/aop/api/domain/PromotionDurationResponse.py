#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromotionDurationResponse(object):

    def __init__(self):
        self._hour_list = None
        self._week_list = None

    @property
    def hour_list(self):
        return self._hour_list

    @hour_list.setter
    def hour_list(self, value):
        if isinstance(value, list):
            self._hour_list = list()
            for i in value:
                self._hour_list.append(i)
    @property
    def week_list(self):
        return self._week_list

    @week_list.setter
    def week_list(self, value):
        if isinstance(value, list):
            self._week_list = list()
            for i in value:
                self._week_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.hour_list:
            if isinstance(self.hour_list, list):
                for i in range(0, len(self.hour_list)):
                    element = self.hour_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hour_list[i] = element.to_alipay_dict()
            if hasattr(self.hour_list, 'to_alipay_dict'):
                params['hour_list'] = self.hour_list.to_alipay_dict()
            else:
                params['hour_list'] = self.hour_list
        if self.week_list:
            if isinstance(self.week_list, list):
                for i in range(0, len(self.week_list)):
                    element = self.week_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.week_list[i] = element.to_alipay_dict()
            if hasattr(self.week_list, 'to_alipay_dict'):
                params['week_list'] = self.week_list.to_alipay_dict()
            else:
                params['week_list'] = self.week_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromotionDurationResponse()
        if 'hour_list' in d:
            o.hour_list = d['hour_list']
        if 'week_list' in d:
            o.week_list = d['week_list']
        return o


