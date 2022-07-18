#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignTaskPrizeQueryModel(object):

    def __init__(self):
        self._end_time = None
        self._start_time = None
        self._task_cen_id = None
        self._user_id = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def task_cen_id(self):
        return self._task_cen_id

    @task_cen_id.setter
    def task_cen_id(self, value):
        self._task_cen_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.task_cen_id:
            if hasattr(self.task_cen_id, 'to_alipay_dict'):
                params['task_cen_id'] = self.task_cen_id.to_alipay_dict()
            else:
                params['task_cen_id'] = self.task_cen_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignTaskPrizeQueryModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'task_cen_id' in d:
            o.task_cen_id = d['task_cen_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


