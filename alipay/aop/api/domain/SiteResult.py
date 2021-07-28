#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SiteItem import SiteItem
from alipay.aop.api.domain.SitePlanItem import SitePlanItem


class SiteResult(object):

    def __init__(self):
        self._code = None
        self._data = None
        self._message = None
        self._task_list = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, SiteItem):
                    self._data.append(i)
                else:
                    self._data.append(SiteItem.from_alipay_dict(i))
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def task_list(self):
        return self._task_list

    @task_list.setter
    def task_list(self, value):
        if isinstance(value, list):
            self._task_list = list()
            for i in value:
                if isinstance(i, SitePlanItem):
                    self._task_list.append(i)
                else:
                    self._task_list.append(SitePlanItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.data:
            if isinstance(self.data, list):
                for i in range(0, len(self.data)):
                    element = self.data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data[i] = element.to_alipay_dict()
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.message:
            if hasattr(self.message, 'to_alipay_dict'):
                params['message'] = self.message.to_alipay_dict()
            else:
                params['message'] = self.message
        if self.task_list:
            if isinstance(self.task_list, list):
                for i in range(0, len(self.task_list)):
                    element = self.task_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task_list[i] = element.to_alipay_dict()
            if hasattr(self.task_list, 'to_alipay_dict'):
                params['task_list'] = self.task_list.to_alipay_dict()
            else:
                params['task_list'] = self.task_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SiteResult()
        if 'code' in d:
            o.code = d['code']
        if 'data' in d:
            o.data = d['data']
        if 'message' in d:
            o.message = d['message']
        if 'task_list' in d:
            o.task_list = d['task_list']
        return o


