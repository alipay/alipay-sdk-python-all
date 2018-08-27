#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ModelMeta(object):

    def __init__(self):
        self._model_desc = None
        self._model_name = None
        self._model_uk = None
        self._query_key = None

    @property
    def model_desc(self):
        return self._model_desc

    @model_desc.setter
    def model_desc(self, value):
        self._model_desc = value
    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, value):
        self._model_name = value
    @property
    def model_uk(self):
        return self._model_uk

    @model_uk.setter
    def model_uk(self, value):
        self._model_uk = value
    @property
    def query_key(self):
        return self._query_key

    @query_key.setter
    def query_key(self, value):
        if isinstance(value, list):
            self._query_key = list()
            for i in value:
                self._query_key.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.model_desc:
            if hasattr(self.model_desc, 'to_alipay_dict'):
                params['model_desc'] = self.model_desc.to_alipay_dict()
            else:
                params['model_desc'] = self.model_desc
        if self.model_name:
            if hasattr(self.model_name, 'to_alipay_dict'):
                params['model_name'] = self.model_name.to_alipay_dict()
            else:
                params['model_name'] = self.model_name
        if self.model_uk:
            if hasattr(self.model_uk, 'to_alipay_dict'):
                params['model_uk'] = self.model_uk.to_alipay_dict()
            else:
                params['model_uk'] = self.model_uk
        if self.query_key:
            if isinstance(self.query_key, list):
                for i in range(0, len(self.query_key)):
                    element = self.query_key[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.query_key[i] = element.to_alipay_dict()
            if hasattr(self.query_key, 'to_alipay_dict'):
                params['query_key'] = self.query_key.to_alipay_dict()
            else:
                params['query_key'] = self.query_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ModelMeta()
        if 'model_desc' in d:
            o.model_desc = d['model_desc']
        if 'model_name' in d:
            o.model_name = d['model_name']
        if 'model_uk' in d:
            o.model_uk = d['model_uk']
        if 'query_key' in d:
            o.query_key = d['query_key']
        return o


