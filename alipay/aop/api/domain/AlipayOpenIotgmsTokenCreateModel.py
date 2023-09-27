#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QueryParam import QueryParam


class AlipayOpenIotgmsTokenCreateModel(object):

    def __init__(self):
        self._functions = None
        self._open_id = None
        self._query_list = None
        self._scene = None
        self._user_id = None

    @property
    def functions(self):
        return self._functions

    @functions.setter
    def functions(self, value):
        if isinstance(value, list):
            self._functions = list()
            for i in value:
                self._functions.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def query_list(self):
        return self._query_list

    @query_list.setter
    def query_list(self, value):
        if isinstance(value, list):
            self._query_list = list()
            for i in value:
                if isinstance(i, QueryParam):
                    self._query_list.append(i)
                else:
                    self._query_list.append(QueryParam.from_alipay_dict(i))
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.functions:
            if isinstance(self.functions, list):
                for i in range(0, len(self.functions)):
                    element = self.functions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.functions[i] = element.to_alipay_dict()
            if hasattr(self.functions, 'to_alipay_dict'):
                params['functions'] = self.functions.to_alipay_dict()
            else:
                params['functions'] = self.functions
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.query_list:
            if isinstance(self.query_list, list):
                for i in range(0, len(self.query_list)):
                    element = self.query_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.query_list[i] = element.to_alipay_dict()
            if hasattr(self.query_list, 'to_alipay_dict'):
                params['query_list'] = self.query_list.to_alipay_dict()
            else:
                params['query_list'] = self.query_list
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
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
        o = AlipayOpenIotgmsTokenCreateModel()
        if 'functions' in d:
            o.functions = d['functions']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'query_list' in d:
            o.query_list = d['query_list']
        if 'scene' in d:
            o.scene = d['scene']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


