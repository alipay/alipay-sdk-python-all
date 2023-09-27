#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TaskQuery import TaskQuery


class AlipayBossBaseAnttaskTasksQueryModel(object):

    def __init__(self):
        self._auth_key = None
        self._date_time = None
        self._query = None
        self._signature = None

    @property
    def auth_key(self):
        return self._auth_key

    @auth_key.setter
    def auth_key(self, value):
        self._auth_key = value
    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, value):
        self._date_time = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        if isinstance(value, TaskQuery):
            self._query = value
        else:
            self._query = TaskQuery.from_alipay_dict(value)
    @property
    def signature(self):
        return self._signature

    @signature.setter
    def signature(self, value):
        self._signature = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_key:
            if hasattr(self.auth_key, 'to_alipay_dict'):
                params['auth_key'] = self.auth_key.to_alipay_dict()
            else:
                params['auth_key'] = self.auth_key
        if self.date_time:
            if hasattr(self.date_time, 'to_alipay_dict'):
                params['date_time'] = self.date_time.to_alipay_dict()
            else:
                params['date_time'] = self.date_time
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.signature:
            if hasattr(self.signature, 'to_alipay_dict'):
                params['signature'] = self.signature.to_alipay_dict()
            else:
                params['signature'] = self.signature
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossBaseAnttaskTasksQueryModel()
        if 'auth_key' in d:
            o.auth_key = d['auth_key']
        if 'date_time' in d:
            o.date_time = d['date_time']
        if 'query' in d:
            o.query = d['query']
        if 'signature' in d:
            o.signature = d['signature']
        return o


