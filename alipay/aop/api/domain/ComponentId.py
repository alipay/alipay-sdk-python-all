#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessId import BusinessId


class ComponentId(object):

    def __init__(self):
        self._business_id = None
        self._source_id = None
        self._system_type = None
        self._task_id = None

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        if isinstance(value, BusinessId):
            self._business_id = value
        else:
            self._business_id = BusinessId.from_alipay_dict(value)
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def system_type(self):
        return self._system_type

    @system_type.setter
    def system_type(self, value):
        self._system_type = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.system_type:
            if hasattr(self.system_type, 'to_alipay_dict'):
                params['system_type'] = self.system_type.to_alipay_dict()
            else:
                params['system_type'] = self.system_type
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ComponentId()
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'system_type' in d:
            o.system_type = d['system_type']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


