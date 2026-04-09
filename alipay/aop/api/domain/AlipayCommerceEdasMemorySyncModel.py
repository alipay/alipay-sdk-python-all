#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEdasMemorySyncModel(object):

    def __init__(self):
        self._data_scene_code = None
        self._industry_id = None
        self._inst_id = None
        self._open_id = None
        self._query = None
        self._task_id = None
        self._user_id = None

    @property
    def data_scene_code(self):
        return self._data_scene_code

    @data_scene_code.setter
    def data_scene_code(self, value):
        self._data_scene_code = value
    @property
    def industry_id(self):
        return self._industry_id

    @industry_id.setter
    def industry_id(self, value):
        self._industry_id = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_scene_code:
            if hasattr(self.data_scene_code, 'to_alipay_dict'):
                params['data_scene_code'] = self.data_scene_code.to_alipay_dict()
            else:
                params['data_scene_code'] = self.data_scene_code
        if self.industry_id:
            if hasattr(self.industry_id, 'to_alipay_dict'):
                params['industry_id'] = self.industry_id.to_alipay_dict()
            else:
                params['industry_id'] = self.industry_id
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
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
        o = AlipayCommerceEdasMemorySyncModel()
        if 'data_scene_code' in d:
            o.data_scene_code = d['data_scene_code']
        if 'industry_id' in d:
            o.industry_id = d['industry_id']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'query' in d:
            o.query = d['query']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


