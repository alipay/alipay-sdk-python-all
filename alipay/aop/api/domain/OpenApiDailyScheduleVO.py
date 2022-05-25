#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiDailyScheduleVO(object):

    def __init__(self):
        self._daily_schedule_id = None
        self._date = None
        self._name = None
        self._over_limit = None
        self._step_list = None

    @property
    def daily_schedule_id(self):
        return self._daily_schedule_id

    @daily_schedule_id.setter
    def daily_schedule_id(self, value):
        self._daily_schedule_id = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def over_limit(self):
        return self._over_limit

    @over_limit.setter
    def over_limit(self, value):
        self._over_limit = value
    @property
    def step_list(self):
        return self._step_list

    @step_list.setter
    def step_list(self, value):
        if isinstance(value, list):
            self._step_list = list()
            for i in value:
                self._step_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.daily_schedule_id:
            if hasattr(self.daily_schedule_id, 'to_alipay_dict'):
                params['daily_schedule_id'] = self.daily_schedule_id.to_alipay_dict()
            else:
                params['daily_schedule_id'] = self.daily_schedule_id
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.over_limit:
            if hasattr(self.over_limit, 'to_alipay_dict'):
                params['over_limit'] = self.over_limit.to_alipay_dict()
            else:
                params['over_limit'] = self.over_limit
        if self.step_list:
            if isinstance(self.step_list, list):
                for i in range(0, len(self.step_list)):
                    element = self.step_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.step_list[i] = element.to_alipay_dict()
            if hasattr(self.step_list, 'to_alipay_dict'):
                params['step_list'] = self.step_list.to_alipay_dict()
            else:
                params['step_list'] = self.step_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiDailyScheduleVO()
        if 'daily_schedule_id' in d:
            o.daily_schedule_id = d['daily_schedule_id']
        if 'date' in d:
            o.date = d['date']
        if 'name' in d:
            o.name = d['name']
        if 'over_limit' in d:
            o.over_limit = d['over_limit']
        if 'step_list' in d:
            o.step_list = d['step_list']
        return o


