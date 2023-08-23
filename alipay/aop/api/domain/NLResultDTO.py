#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NLResultDTO(object):

    def __init__(self):
        self._app_token = None
        self._data = None
        self._service_time_cost = None
        self._service_token_cost = None
        self._task_id = None
        self._task_msg = None
        self._task_status = None
        self._task_type = None

    @property
    def app_token(self):
        return self._app_token

    @app_token.setter
    def app_token(self, value):
        self._app_token = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def service_time_cost(self):
        return self._service_time_cost

    @service_time_cost.setter
    def service_time_cost(self, value):
        self._service_time_cost = value
    @property
    def service_token_cost(self):
        return self._service_token_cost

    @service_token_cost.setter
    def service_token_cost(self, value):
        self._service_token_cost = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_msg(self):
        return self._task_msg

    @task_msg.setter
    def task_msg(self, value):
        self._task_msg = value
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
        if self.app_token:
            if hasattr(self.app_token, 'to_alipay_dict'):
                params['app_token'] = self.app_token.to_alipay_dict()
            else:
                params['app_token'] = self.app_token
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.service_time_cost:
            if hasattr(self.service_time_cost, 'to_alipay_dict'):
                params['service_time_cost'] = self.service_time_cost.to_alipay_dict()
            else:
                params['service_time_cost'] = self.service_time_cost
        if self.service_token_cost:
            if hasattr(self.service_token_cost, 'to_alipay_dict'):
                params['service_token_cost'] = self.service_token_cost.to_alipay_dict()
            else:
                params['service_token_cost'] = self.service_token_cost
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.task_msg:
            if hasattr(self.task_msg, 'to_alipay_dict'):
                params['task_msg'] = self.task_msg.to_alipay_dict()
            else:
                params['task_msg'] = self.task_msg
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
        o = NLResultDTO()
        if 'app_token' in d:
            o.app_token = d['app_token']
        if 'data' in d:
            o.data = d['data']
        if 'service_time_cost' in d:
            o.service_time_cost = d['service_time_cost']
        if 'service_token_cost' in d:
            o.service_token_cost = d['service_token_cost']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_msg' in d:
            o.task_msg = d['task_msg']
        if 'task_status' in d:
            o.task_status = d['task_status']
        if 'task_type' in d:
            o.task_type = d['task_type']
        return o


