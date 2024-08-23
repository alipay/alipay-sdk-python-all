#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LiveSubTaskList import LiveSubTaskList


class LiveTaskList(object):

    def __init__(self):
        self._date = None
        self._date_formate = None
        self._live_sub_task_list = None
        self._task_status = None
        self._task_type = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def date_formate(self):
        return self._date_formate

    @date_formate.setter
    def date_formate(self, value):
        self._date_formate = value
    @property
    def live_sub_task_list(self):
        return self._live_sub_task_list

    @live_sub_task_list.setter
    def live_sub_task_list(self, value):
        if isinstance(value, list):
            self._live_sub_task_list = list()
            for i in value:
                if isinstance(i, LiveSubTaskList):
                    self._live_sub_task_list.append(i)
                else:
                    self._live_sub_task_list.append(LiveSubTaskList.from_alipay_dict(i))
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.date_formate:
            if hasattr(self.date_formate, 'to_alipay_dict'):
                params['date_formate'] = self.date_formate.to_alipay_dict()
            else:
                params['date_formate'] = self.date_formate
        if self.live_sub_task_list:
            if isinstance(self.live_sub_task_list, list):
                for i in range(0, len(self.live_sub_task_list)):
                    element = self.live_sub_task_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.live_sub_task_list[i] = element.to_alipay_dict()
            if hasattr(self.live_sub_task_list, 'to_alipay_dict'):
                params['live_sub_task_list'] = self.live_sub_task_list.to_alipay_dict()
            else:
                params['live_sub_task_list'] = self.live_sub_task_list
        if self.task_status:
            if hasattr(self.task_status, 'to_alipay_dict'):
                params['task_status'] = self.task_status.to_alipay_dict()
            else:
                params['task_status'] = self.task_status
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LiveTaskList()
        if 'date' in d:
            o.date = d['date']
        if 'date_formate' in d:
            o.date_formate = d['date_formate']
        if 'live_sub_task_list' in d:
            o.live_sub_task_list = d['live_sub_task_list']
        if 'task_status' in d:
            o.task_status = d['task_status']
        if 'task_type' in d:
            o.task_type = d['task_type']
        return o


