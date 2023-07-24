#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsTaskcenterBatchqueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._open_id = None
        self._task_group_id = None
        self._task_id_list = None
        self._user_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def task_group_id(self):
        return self._task_group_id

    @task_group_id.setter
    def task_group_id(self, value):
        self._task_group_id = value
    @property
    def task_id_list(self):
        return self._task_id_list

    @task_id_list.setter
    def task_id_list(self, value):
        if isinstance(value, list):
            self._task_id_list = list()
            for i in value:
                self._task_id_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.task_group_id:
            if hasattr(self.task_group_id, 'to_alipay_dict'):
                params['task_group_id'] = self.task_group_id.to_alipay_dict()
            else:
                params['task_group_id'] = self.task_group_id
        if self.task_id_list:
            if isinstance(self.task_id_list, list):
                for i in range(0, len(self.task_id_list)):
                    element = self.task_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task_id_list[i] = element.to_alipay_dict()
            if hasattr(self.task_id_list, 'to_alipay_dict'):
                params['task_id_list'] = self.task_id_list.to_alipay_dict()
            else:
                params['task_id_list'] = self.task_id_list
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
        o = AlipayCommerceSportsTaskcenterBatchqueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'task_group_id' in d:
            o.task_group_id = d['task_group_id']
        if 'task_id_list' in d:
            o.task_id_list = d['task_id_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


