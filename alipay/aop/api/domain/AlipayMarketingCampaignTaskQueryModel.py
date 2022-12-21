#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignTaskQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._task_cen_id = None
        self._task_ids = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def task_cen_id(self):
        return self._task_cen_id

    @task_cen_id.setter
    def task_cen_id(self, value):
        self._task_cen_id = value
    @property
    def task_ids(self):
        return self._task_ids

    @task_ids.setter
    def task_ids(self, value):
        if isinstance(value, list):
            self._task_ids = list()
            for i in value:
                self._task_ids.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.task_cen_id:
            if hasattr(self.task_cen_id, 'to_alipay_dict'):
                params['task_cen_id'] = self.task_cen_id.to_alipay_dict()
            else:
                params['task_cen_id'] = self.task_cen_id
        if self.task_ids:
            if isinstance(self.task_ids, list):
                for i in range(0, len(self.task_ids)):
                    element = self.task_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task_ids[i] = element.to_alipay_dict()
            if hasattr(self.task_ids, 'to_alipay_dict'):
                params['task_ids'] = self.task_ids.to_alipay_dict()
            else:
                params['task_ids'] = self.task_ids
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
        o = AlipayMarketingCampaignTaskQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'task_cen_id' in d:
            o.task_cen_id = d['task_cen_id']
        if 'task_ids' in d:
            o.task_ids = d['task_ids']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


