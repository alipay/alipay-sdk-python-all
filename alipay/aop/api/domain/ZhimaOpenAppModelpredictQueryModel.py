#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaOpenAppModelpredictQueryModel(object):

    def __init__(self):
        self._model = None
        self._query = None

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value


    def to_alipay_dict(self):
        params = dict()
        if self.model:
            if hasattr(self.model, 'to_alipay_dict'):
                params['model'] = self.model.to_alipay_dict()
            else:
                params['model'] = self.model
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaOpenAppModelpredictQueryModel()
        if 'model' in d:
            o.model = d['model']
        if 'query' in d:
            o.query = d['query']
        return o


