#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessId import BusinessId


class AlipayBossBaseAnttaskTaskRestartModel(object):

    def __init__(self):
        self._auth_key = None
        self._business_id = None
        self._date_time = None
        self._signature = None
        self._task_id = None

    @property
    def auth_key(self):
        return self._auth_key

    @auth_key.setter
    def auth_key(self, value):
        self._auth_key = value
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
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, value):
        self._date_time = value
    @property
    def signature(self):
        return self._signature

    @signature.setter
    def signature(self, value):
        self._signature = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_key:
            if hasattr(self.auth_key, 'to_alipay_dict'):
                params['auth_key'] = self.auth_key.to_alipay_dict()
            else:
                params['auth_key'] = self.auth_key
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.date_time:
            if hasattr(self.date_time, 'to_alipay_dict'):
                params['date_time'] = self.date_time.to_alipay_dict()
            else:
                params['date_time'] = self.date_time
        if self.signature:
            if hasattr(self.signature, 'to_alipay_dict'):
                params['signature'] = self.signature.to_alipay_dict()
            else:
                params['signature'] = self.signature
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
        o = AlipayBossBaseAnttaskTaskRestartModel()
        if 'auth_key' in d:
            o.auth_key = d['auth_key']
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'date_time' in d:
            o.date_time = d['date_time']
        if 'signature' in d:
            o.signature = d['signature']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


