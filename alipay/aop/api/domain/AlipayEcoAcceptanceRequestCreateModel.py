#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoAcceptanceRequestCreateModel(object):

    def __init__(self):
        self._accetor_id = None
        self._accetor_nick = None
        self._accetor_user_type = None
        self._case_id = None
        self._params = None
        self._task_id = None

    @property
    def accetor_id(self):
        return self._accetor_id

    @accetor_id.setter
    def accetor_id(self, value):
        self._accetor_id = value
    @property
    def accetor_nick(self):
        return self._accetor_nick

    @accetor_nick.setter
    def accetor_nick(self, value):
        self._accetor_nick = value
    @property
    def accetor_user_type(self):
        return self._accetor_user_type

    @accetor_user_type.setter
    def accetor_user_type(self, value):
        self._accetor_user_type = value
    @property
    def case_id(self):
        return self._case_id

    @case_id.setter
    def case_id(self, value):
        self._case_id = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.accetor_id:
            if hasattr(self.accetor_id, 'to_alipay_dict'):
                params['accetor_id'] = self.accetor_id.to_alipay_dict()
            else:
                params['accetor_id'] = self.accetor_id
        if self.accetor_nick:
            if hasattr(self.accetor_nick, 'to_alipay_dict'):
                params['accetor_nick'] = self.accetor_nick.to_alipay_dict()
            else:
                params['accetor_nick'] = self.accetor_nick
        if self.accetor_user_type:
            if hasattr(self.accetor_user_type, 'to_alipay_dict'):
                params['accetor_user_type'] = self.accetor_user_type.to_alipay_dict()
            else:
                params['accetor_user_type'] = self.accetor_user_type
        if self.case_id:
            if hasattr(self.case_id, 'to_alipay_dict'):
                params['case_id'] = self.case_id.to_alipay_dict()
            else:
                params['case_id'] = self.case_id
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
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
        o = AlipayEcoAcceptanceRequestCreateModel()
        if 'accetor_id' in d:
            o.accetor_id = d['accetor_id']
        if 'accetor_nick' in d:
            o.accetor_nick = d['accetor_nick']
        if 'accetor_user_type' in d:
            o.accetor_user_type = d['accetor_user_type']
        if 'case_id' in d:
            o.case_id = d['case_id']
        if 'params' in d:
            o.params = d['params']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


