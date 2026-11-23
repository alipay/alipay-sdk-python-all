#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EvalInfo(object):

    def __init__(self):
        self._custom_queries = None
        self._eval_desc = None
        self._eval_name = None
        self._preset_queries = None

    @property
    def custom_queries(self):
        return self._custom_queries

    @custom_queries.setter
    def custom_queries(self, value):
        if isinstance(value, list):
            self._custom_queries = list()
            for i in value:
                self._custom_queries.append(i)
    @property
    def eval_desc(self):
        return self._eval_desc

    @eval_desc.setter
    def eval_desc(self, value):
        self._eval_desc = value
    @property
    def eval_name(self):
        return self._eval_name

    @eval_name.setter
    def eval_name(self, value):
        self._eval_name = value
    @property
    def preset_queries(self):
        return self._preset_queries

    @preset_queries.setter
    def preset_queries(self, value):
        if isinstance(value, list):
            self._preset_queries = list()
            for i in value:
                self._preset_queries.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.custom_queries:
            if isinstance(self.custom_queries, list):
                for i in range(0, len(self.custom_queries)):
                    element = self.custom_queries[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.custom_queries[i] = element.to_alipay_dict()
            if hasattr(self.custom_queries, 'to_alipay_dict'):
                params['custom_queries'] = self.custom_queries.to_alipay_dict()
            else:
                params['custom_queries'] = self.custom_queries
        if self.eval_desc:
            if hasattr(self.eval_desc, 'to_alipay_dict'):
                params['eval_desc'] = self.eval_desc.to_alipay_dict()
            else:
                params['eval_desc'] = self.eval_desc
        if self.eval_name:
            if hasattr(self.eval_name, 'to_alipay_dict'):
                params['eval_name'] = self.eval_name.to_alipay_dict()
            else:
                params['eval_name'] = self.eval_name
        if self.preset_queries:
            if isinstance(self.preset_queries, list):
                for i in range(0, len(self.preset_queries)):
                    element = self.preset_queries[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.preset_queries[i] = element.to_alipay_dict()
            if hasattr(self.preset_queries, 'to_alipay_dict'):
                params['preset_queries'] = self.preset_queries.to_alipay_dict()
            else:
                params['preset_queries'] = self.preset_queries
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EvalInfo()
        if 'custom_queries' in d:
            o.custom_queries = d['custom_queries']
        if 'eval_desc' in d:
            o.eval_desc = d['eval_desc']
        if 'eval_name' in d:
            o.eval_name = d['eval_name']
        if 'preset_queries' in d:
            o.preset_queries = d['preset_queries']
        return o


