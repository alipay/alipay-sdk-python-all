#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignTaskResult(object):

    def __init__(self):
        self._biz_id = None
        self._sign_enter_url = None
        self._task_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def sign_enter_url(self):
        return self._sign_enter_url

    @sign_enter_url.setter
    def sign_enter_url(self, value):
        self._sign_enter_url = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.sign_enter_url:
            if hasattr(self.sign_enter_url, 'to_alipay_dict'):
                params['sign_enter_url'] = self.sign_enter_url.to_alipay_dict()
            else:
                params['sign_enter_url'] = self.sign_enter_url
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
        o = SignTaskResult()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'sign_enter_url' in d:
            o.sign_enter_url = d['sign_enter_url']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


