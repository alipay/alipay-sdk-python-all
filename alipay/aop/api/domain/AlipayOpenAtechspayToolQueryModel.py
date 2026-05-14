#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAtechspayToolQueryModel(object):

    def __init__(self):
        self._end_time = None
        self._env = None
        self._keyword = None
        self._start_time = None
        self._tool = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self, value):
        self._keyword = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def tool(self):
        return self._tool

    @tool.setter
    def tool(self, value):
        self._tool = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.keyword:
            if hasattr(self.keyword, 'to_alipay_dict'):
                params['keyword'] = self.keyword.to_alipay_dict()
            else:
                params['keyword'] = self.keyword
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.tool:
            if hasattr(self.tool, 'to_alipay_dict'):
                params['tool'] = self.tool.to_alipay_dict()
            else:
                params['tool'] = self.tool
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAtechspayToolQueryModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'env' in d:
            o.env = d['env']
        if 'keyword' in d:
            o.keyword = d['keyword']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'tool' in d:
            o.tool = d['tool']
        return o


