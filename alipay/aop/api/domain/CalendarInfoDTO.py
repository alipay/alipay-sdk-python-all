#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CalendarInfoDTO(object):

    def __init__(self):
        self._calendar_type = None
        self._day_list = None

    @property
    def calendar_type(self):
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, value):
        self._calendar_type = value
    @property
    def day_list(self):
        return self._day_list

    @day_list.setter
    def day_list(self, value):
        if isinstance(value, list):
            self._day_list = list()
            for i in value:
                self._day_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.calendar_type:
            if hasattr(self.calendar_type, 'to_alipay_dict'):
                params['calendar_type'] = self.calendar_type.to_alipay_dict()
            else:
                params['calendar_type'] = self.calendar_type
        if self.day_list:
            if isinstance(self.day_list, list):
                for i in range(0, len(self.day_list)):
                    element = self.day_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.day_list[i] = element.to_alipay_dict()
            if hasattr(self.day_list, 'to_alipay_dict'):
                params['day_list'] = self.day_list.to_alipay_dict()
            else:
                params['day_list'] = self.day_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CalendarInfoDTO()
        if 'calendar_type' in d:
            o.calendar_type = d['calendar_type']
        if 'day_list' in d:
            o.day_list = d['day_list']
        return o


